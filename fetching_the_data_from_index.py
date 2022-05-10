from elasticsearch import Elasticsearch  # importing the Elasticsearch class from elasticsearch module
# connecting using the http_auth attribute
es = Elasticsearch([{"host": "localhost", "port": 9200, "http_auth": ["elastic", "pratik123"]}])
# now checking the connection been successful or not
print(es.ping())
# for fetching the data from the elasticsearch we need to use the get() on them
# fetching the 2nd document from the index is
response = es.get(index="customer", doc_type="_doc", id=2)
# fetching the response from the same as
# print(response)
# fetching only the document data using the source attribute
print(response["_source"])
