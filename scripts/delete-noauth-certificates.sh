#!/bin/bash
#API_HOST="http://172.29.0.4:8777/"
API_HOST="http://localhost:8101/api/v1/"

get=$(curl -s ${API_HOST}certificate/)
for id in $(echo $get | jq -r '.[].id')
do
    echo "Deleting $id"
    curl -X DELETE ${API_HOST}certificate/$id/
done

