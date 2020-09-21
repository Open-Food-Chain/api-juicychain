#!/bin/bash
API_HOST="http://172.29.0.5:8999/"
API_HOST="http://juicychain-api.thenewfork.staging.do.unchain.io/"
API_VER="api/v1/"

for i in {1..1}
do

curl -s -X DELETE  ${API_HOST}${API_VER}organization-detail/27/

done
