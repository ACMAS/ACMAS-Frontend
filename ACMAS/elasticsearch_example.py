from datetime import datetime
from elasticsearch import Elasticsearch
import os

ELASTIC_ADDRESS = os.environ.get('ELASTIC_ADDRESS', 'https://localhost:9200')
ELASTIC_USER = os.environ.get('ELASTIC_USER', 'elastic')
ELASTIC_PASSWORD = os.environ.get('ELASTIC_PASSWORD')

es = Elasticsearch(
    hosts=[ELASTIC_ADDRESS],
    basic_auth=[ELASTIC_USER, ELASTIC_PASSWORD],
    verify_certs=False
)

question1 = {
    'questionId': 1,
    'questionText': 'QUESTION 1 TEXT',
}
resp = es.index(index="question-index", id=question1['questionId'], document=question1)

question2 = {
    'questionId': 2,
    'questionText': 'QUESTION 2 TEXT',
}
resp = es.index(index="question-index", id=question2['questionId'], document=question2)

print(resp['result'])

resp = es.get(index="question-index", id=1)
print(resp['_source'])

es.indices.refresh(index="question-index")

resp = es.search(index="question-index", query={"match_all": {}})
print("Got %d Hits:" % resp['hits']['total']['value'])
for hit in resp['hits']['hits']:
    print("%(questionId)s %(questionText)s" % hit["_source"])
