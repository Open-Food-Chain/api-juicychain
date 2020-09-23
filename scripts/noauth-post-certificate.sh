#!/bin/bash
API_HOST="http://172.29.0.5:8999/"
# API_HOST="http://juicychain-api.thenewfork.staging.do.unchain.io/"
API_VER="api/v1/"


curl -s -X POST -H 'Content-Type: application/json' ${API_HOST}${API_VER}certificate/ -d '{ "name": "NEW CERT", "issuer": "ISSUER MYLO.COM", "identifier": "C-233200777", "date_issue": "2020-01-11", "date_expiry": "2020-12-20", "organization": 1, "pubkey": "", "raddress": ""}'
