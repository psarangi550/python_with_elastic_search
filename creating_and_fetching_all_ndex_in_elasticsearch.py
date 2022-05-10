from elasticsearch import Elasticsearch  # importing the ElasticSearch  class from the elasticsearch module
# connecting to the elasticsearch by using the Elasticsearch class object
es = Elasticsearch(hosts="http://elastic:pratik123@localhost:9200")
# checking the connection by ping()
print(es.ping())
# creating the index named as ecomm
es.indices.create(index="ecomm")
# fetching all the indices in the elasticsearch using the get_alias method
all_indices = es.indices.get_alias("*")  # here * means all the indexes
# iterating over it to fetch all the index
for num, index in enumerate(all_indices):  # using the enumerate function over here
    print(f'{num}-->{index}')
