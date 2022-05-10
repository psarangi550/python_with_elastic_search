from elasticsearch import Elasticsearch  # importing the ElasticSearch class  from elasticsearch module

# now here we need to create the elasticsearch object which is the object of ElasticSearch class
# es = Elasticsearch("http://elastic:pratik123@localhost:9200")
#or we can connect it as below
es=Elasticsearch(hosts="http://elastic:pratik123@localhost:9200")
# checking the ping by ping() on the elasticsearch object
print(es.ping())
