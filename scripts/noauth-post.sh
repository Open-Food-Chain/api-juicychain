#!/bin/bash
curl -X POST -H "Content-Type: application/json" http://localhost:8888/batches/v1dev/refresco/ -d '{ "anfp": "1","dfp": "1","bnfp": "1","pds": "2020-08-05","pde": "2020-08-28","jds": 5,"jde": 28,"bbd": "2020-10-28","pc": "1","pl": "1","rmn": "1","pon": "1","pop": "1"}'
