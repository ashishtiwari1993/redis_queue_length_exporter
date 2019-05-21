from prometheus_client import make_wsgi_app, Gauge
from wsgiref.simple_server import make_server
import redis,sys,json

with open('queue.json', 'r') as data_file:
        json_data = data_file.read()

data = json.loads(json_data)

host = data['hosts']
g = Gauge('redis_queue_length', 'Length of queues', ['host','queue_name','queue_type'])

def generate():
    for h, q_type in host.items():
        s = h.split(':')
        r = redis.Redis(host=s[0], port=s[1])

        try:
            r.ping()            
        except redis.ConnectionError:
            print("Cannot make connection to " +s[0]+":"+s[1])
            continue

        for q in q_type:
            qlist = data['queue_type'][q]
        
            for qname in qlist:
                a = r.llen(qname)
                g.labels(h,qname,q).set(a)


metrics_app = make_wsgi_app()

def my_app(environ, start_fn):
    if environ['PATH_INFO'] == '/metrics':
        generate()
        return metrics_app(environ, start_fn)

httpd = make_server('', 8000, my_app)
httpd.serve_forever()
