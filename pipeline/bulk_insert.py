from elasticsearch import Elasticsearch

es = Elasticsearch(host="localhost", port=9200 , http_auth=('elastic', 'changeme'))

# data = [
#     {
#         'name':'yassine'
#     },
#     {'name':'yassine02'}
# ]

def read_and_transform(txt_file):
    d = dict()
    data = list()
    with open(txt_file , 'r' , encoding='UTF8') as f:
        tmp = f.readlines()
        f.close()
    for x in tmp:
        d['text'] = x.split(';')[0]
        d['label'] = ((x.split(';')[1]).replace('\n' , '')).upper()
        dictionary_copy = d.copy()
        data.append(dictionary_copy)
    return data

def create_index(index):
    es.indices.create(index=index, ignore=400)

def insert_one_data(_index, data , id):
    res = es.index(index=_index, doc_type='authors', id=id, body=data)
    """EXMPLE:
    {'_index': 'test-index', '_type': 'authors', '_id': '5', '_version': 1, 'result': 'created', '_shards': {'total': 2, 's
uccessful': 1, 'failed': 0}, '_seq_no': 4, '_primary_term': 1}
    """


if __name__ == '__main__':
    index = "fake_news"
    data = read_and_transform('../scrapping/FakeNews.txt')
    print(data)
    create_index(index)
    for num , d in enumerate(data):
        insert_one_data(index, d , num)