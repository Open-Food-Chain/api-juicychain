#!/bin/bash
API_HOST="http://172.29.0.5:8999/"
API_HOST="http://juicychain-api.thenewfork.staging.do.unchain.io/"
API_VER="api/v1/"

RANDOM_33H=$(cat /dev/urandom | tr -dc 'A-F0-9' | fold -w 33 | head -n 1)
RANDOM_RADDRESS="R${RANDOM_33H}"
curl -s -X PATCH -H "Content-Type: application/json" ${API_HOST}${API_VER}certificate/66/ -d "{ \"raddress\": \"${RANDOM_RADDRESS}\"}"
