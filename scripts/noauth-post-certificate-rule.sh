#!/bin/bash
# API_HOST="http://172.29.0.5:8999/"
API_HOST="http://juicychain-api.thenewfork.staging.do.unchain.io/"
API_VER="api/v1/"


curl -s -X POST -H 'Content-Type: application/json' ${API_HOST}${API_VER}certificate-rule/ -d '{ "name": "NEW CERT RULE", "condition": "condition name 1", "certificate": 58, "pubkey": "", "raddress": ""}'
