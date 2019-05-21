# Redis Queue Length Metrics Exporter

##  Run locally:

    git clone https://github.com/ashishtiwari1993/redis-queue-length-prometheus-exporter.git
    pip install prometheus_client
    pip install redis
    python llen.py
    
## Run via Docker:

    git clone https://github.com/ashishtiwari1993/redis-queue-length-prometheus-exporter.git
    cd redis_queue_length_exporter
    docker build -t "redis_queue_length_exporter" .
    docker run  -d --name 'redis_queue_length_exporter' -p 8000:8000 redis_queue_length_exporter
    

## Test on browser:
    localhost:8000

## Edit `queue.json`:

	{  
	  "queue_type":{  
		"queue_group1":[  
		  "q1",
		  "q2",
		  . 
		  .
		],
		"queue_group2":[  
		  "q1",
		  "q2",
		  . 
	 	  .
		],
		"queue_group3":[  
		  "q1",
		  "q2",
		  . 
	 	  .
		],
		"queue_group4":[  
		  "q1",
		  "q2",
		  . 
	 	  .
		]
	  },
	  "hosts":{  
		"host1.example.com:6379":[  
		  "queue_group1",
		  "queue_group2"
		],
		"host2.example.com:6379":[  
		  "queue_group3",
		  "queue_group4"
		]
	  }
	}

## What's exported?

Queue length from the LLEN command are exported, See https://redis.io/commands/llen for more details.
