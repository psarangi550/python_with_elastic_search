import pprint  # importing the pprint module
from elasticsearch import Elasticsearch  # importing the Elasticsearch class from elasticsearch module
es = Elasticsearch([{"host": "localhost", "port": 9200, "http_auth": ["elastic", "pratik123"]}])
# checking the connection status
print(es.ping())
# writing the multi_match query in here
query = {
    "query": {
        "multi_match": {
            "query": "intoduction to elasticsearch",
            "fields": ["title", "tags"]
        }
    }
}
if __name__=="__main__":
    # now searching the same using the search() on the elasticsearch object as
    fetched_docs = es.search(index="blogposts", body=query)
    # then iterating over the hots as
    for doc in fetched_docs["hits"]["hits"]:
        pprint.pprint(doc)
