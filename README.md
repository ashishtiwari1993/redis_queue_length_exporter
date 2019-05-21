# Redis Queue Length Metrics Exporter

##  Run locally:

    git clone https://github.com/ashishtiwari1993/redis_queue_length_exporter.git
    pip install prometheus_client
    pip install redis
    python llen.py
    
## Run via Docker:

    git clone https://github.com/ashishtiwari1993/redis_queue_length_exporter.git
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

Define queue group in `queue_type` object. Queue group has array of all queue name (q1, q2) of same behaviour. Map Queue group with host in `host` object. It will export queue length accroding to `queue.json ` file and It will assign queue labels in prometheus while storing data.

Here is the sample file.


## What's exported?

Queue length from the LLEN command are exported, See https://redis.io/commands/llen for more details.

## What else?

* Need to add grafana dashboard.
* Open an issue if you have more suggestions or ideas about what to add.



