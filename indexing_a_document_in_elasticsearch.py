from elasticsearch import Elasticsearch  # importing the Elasticsearch class from elasticsearch module

# connecting using the http_auth attribute
es = Elasticsearch([{"host": "localhost", "port": 9200, "http_auth": ["elastic", "pratik123"]}])
# Connecting to the Bonsai Elasticsearch
# here we need to use the use_ssl option in order to connect to bonsai elasticsearch
# es = Elasticsearch([{"host": "elasticcluster-7057601656.us-east-1.bonsaisearch.net", "port": 443,
#                      "http_auth": ["gmuk8a4rkt", "7g6yr22bfl"], "use_ssl": True}])
# checking the connection status
print(es.ping())
# creating the index with name as customer using the es.indices.create()
resp = es.indices.create(index="customer", ignore=[400, 401])
# printing the response
print(resp)
# using the json format to index the document
cust1 = {
    "name": "Accounting 101",
    "room": "E3",
    "professor": {
        "name": "Thomas Baszo",
        "department": "finance",
        "facutly_type": "part-time",
        "email": "baszot@onuni.com"
    },
    "students_enrolled": 27,
    "course_publish_date": "2015-01-19",
    "course_description": "Act 101 is a course from the business school on the introduction to accounting that teaches students how to read and compose basic financial statements"
}

cust2 = {
    "name": "Marketing 101",
    "room": "E4",
    "professor": {
        "name": "William Smith",
        "department": "finance",
        "facutly_type": "part-time",
        "email": "wills@onuni.com"
    },
    "students_enrolled": 18,
    "course_publish_date": "2015-06-21",
    "course_description": "Mkt 101 is a course from the business school on the introduction to marketing that teaches students the fundamentals of market analysis, customer retention and online advertisements"
}

# in order to index a document to elasticsearch we need to use index() on elasticsearch Object
resp1 = es.index(index="customer", doc_type="_doc", id=1, body=cust1)
# indexing one more dicument into elasticsearch
resp2 = es.index(index="customer", doc_type="_doc", id=2, body=cust2)
# printing the responses
print(resp1)
print(resp2)
