import pprint  # importing the pprint module
from elasticsearch import Elasticsearch  # importing the Elasticsearch class from elasticsearch module
# here creating the es elasticsearch object using the Elasticsearch class
es = Elasticsearch([{"host": "localhost", "port": 9200, "http_auth": ["elastic", "pratik123"]}])
# checking the connection status
print(es.ping())
# now searching with the match and multi_match query
query = {
    "query": {
        "match": {
            "title": {
                "query": "introduction to elasticsearch"
            }
        }
    }
}

# now searching the same using the search() on the elasticsearch object as
fetched_docs = es.search(index="blogposts", body=query)
# then iterating over the hots as
for doc in fetched_docs["hits"]["hits"]:
    pprint.pprint(doc)
