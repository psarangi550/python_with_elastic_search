from elasticsearch import Elasticsearch  # importing the Elasticsearch class from elasticsearch module
import pprint  # importing the pprint module
# creating the connection object using the Elasticsearch class
es = Elasticsearch([{"host": "localhost", "port": 9200, "http_auth": ["elastic", "pratik123"]}])
# checking the connection created successfully or not
print(es.ping())
# now searching all the document in the index as
total_doc = es.search(index="customer", body={"query": {"match_all": {}}})
# checking the return value
# pprint.pprint(total_doc, sort_dicts=False)
# fetching the hots value from the search
# pprint.pprint(total_doc["hits"]["hits"],sort_dicts=False)
# iterating through all the doc
for doc in total_doc["hits"]["hits"]:
    pprint.pprint(doc, sort_dicts=False)
