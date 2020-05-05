# ElasticSearch with Tornado

## Start Web Server

```bash
# source env/bin/activate
# python3 web.py
./start.sh
```

## Initiate ElasticSearch Container

```bash
docker run -it --rm -e "discovery.type=single-node" -p 9200:9200 -p 9300:9300 elasticsearch:7.4.2
```

## ElasticSearch Hands-On - Python API

```python
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host':'127.0.0.1','port':9200}])
es.search(index='logstash-2015.08.20', q='http_status_code:5* AND server_name:"web1"', from_='124119')
```
