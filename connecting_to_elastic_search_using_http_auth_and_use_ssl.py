from elasticsearch import Elasticsearch  # importing the Elasticsearch class from elasticsearch module
# connecting using the http_auth attribute
# es = Elasticsearch([{"host": "localhost", "port": 9200, "http_auth": ["elastic", "pratik123"]}])
# Connecting to the Bonsai Elasticsearch
# here we need to use the use_ssl option in order to connect to bonsai elasticsearch
es = Elasticsearch([{"host": "elasticcluster-7057601656.us-east-1.bonsaisearch.net", "port": 443,
                     "http_auth": ["gmuk8a4rkt", "7g6yr22bfl"], "use_ssl": True}])
# checking the connection status
print(es.ping())
