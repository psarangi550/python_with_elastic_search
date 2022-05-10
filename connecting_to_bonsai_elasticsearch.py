from elasticsearch import Elasticsearch  # importing the ElasticSearch class  from elasticsearch module

# for this we need to downgrade the elasticsearch to 7.14 and less version
# here creating the ElasticSearch class object
es = Elasticsearch(hosts="https://gmuk8a4rkt:7g6yr22bfl@elasticcluster-7057601656.us-east-1.bonsaisearch.net:443")
# using the ping ()
print(es.ping())
