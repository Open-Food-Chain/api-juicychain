#!/bin/bash
API_HOST="http://172.29.0.5:8999/"
API_HOST="http://juicychain-api.thenewfork.staging.do.unchain.io/"
API_VER="api/v1/"

for i in {1..2}
do

        # DATES
        RANDOM_START_DAY=$(cat /dev/urandom | tr -dc '1-2' | fold -w 2 | head -n 1)
        RANDOM_1D=$(cat /dev/urandom | tr -dc '1-9' | fold -w 1 | head -n 1)
        RANDOM_3D=$(cat /dev/urandom | tr -dc '0-9' | fold -w 3 | head -n 1)
        RANDOM_2D=$(cat /dev/urandom | tr -dc '1-9' | fold -w 2 | head -n 1)
        RANDOM_9D=$(cat /dev/urandom | tr -dc '0-9' | fold -w 9 | head -n 1)
        RANDOM_33H=$(cat /dev/urandom | tr -dc 'A-F0-9' | fold -w 33 | head -n 1)
        RANDOM_64H=$(cat /dev/urandom | tr -dc 'A-F0-9' | fold -w 64 | head -n 1)
        END_DAY=$((RANDOM_START_DAY + RANDOM_1D))
        START_MONTH="01"
	END_MONTH="12"
        YEAR="2020"

        # DATA
        RANDOM_ORG_NAME="ORG ${RANDOM_3D}"
	RANDOM_PUBKEY="02${RANDOM_64H}"
	RANDOM_RADDRESS="R${RANDOM_33H}"
	RANDOM_CERT_ID="C-${RANDOM_9D}"
	CERT_ISSUE_DATE="${START_MONTH}-${RANDOM_START_DAY}-${YEAR}"
	CERT_EXPIRY_DATE="${END_MONTH}-${RANDOM_START_DAY}-${YEAR}"
	LOCATION_1="LOCATION A${RANDOM_2D}"
	LOCATION_2="LOCATION B${RANDOM_3D}"

	echo "Create organization ${RANDOM_ORG_NAME}"
	ORG_ID=$(curl -s -X POST -H "Content-Type: application/json" ${API_HOST}${API_VER}organization/ -d "{ \"name\": \"${RANDOM_ORG_NAME}\",\"pubkey\": \"${RANDOM_PUBKEY}\",\"raddress\": \"${RANDOM_RADDRESS}\"}" | jq '.id')
	echo ${ORG_ID}


	echo "Create locations"
        RANDOM_64H=$(cat /dev/urandom | tr -dc 'A-F0-9' | fold -w 64 | head -n 1)
	RANDOM_PUBKEY="02${RANDOM_64H}"
        RANDOM_33H=$(cat /dev/urandom | tr -dc 'A-F0-9' | fold -w 33 | head -n 1)
	RANDOM_RADDRESS="R${RANDOM_33H}"
	LOCATION_1_RADDRESS=${RANDOM_RADDRESS}

	LOC_1_ID=$(curl -s -X POST -H "Content-Type: application/json" ${API_HOST}${API_VER}location/ -d "{ \"name\": \"${LOCATION_1}\",\"pubkey\": \"${RANDOM_PUBKEY}\",\"raddress\": \"${RANDOM_RADDRESS}\", \"organization\": ${ORG_ID}}" | jq '.id')
	echo ${LOC_1_ID}

        RANDOM_64H=$(cat /dev/urandom | tr -dc 'A-F0-9' | fold -w 64 | head -n 1)
	RANDOM_PUBKEY="02${RANDOM_64H}"
        RANDOM_33H=$(cat /dev/urandom | tr -dc 'A-F0-9' | fold -w 33 | head -n 1)
	RANDOM_RADDRESS="R${RANDOM_33H}"
	LOCATION_2_RADDRESS=${RANDOM_RADDRESS}

	LOC_2_ID=$(curl -s -X POST -H "Content-Type: application/json" ${API_HOST}${API_VER}location/ -d "{ \"name\": \"${LOCATION_2}\",\"pubkey\": \"${RANDOM_PUBKEY}\",\"raddress\": \"${RANDOM_RADDRESS}\", \"organization\": ${ORG_ID}}" | jq '.id')
	echo ${LOC_2_ID}

	echo "Create certificates"
        RANDOM_START_DAY=$(cat /dev/urandom | tr -dc '1-2' | fold -w 2 | head -n 1)
        END_DAY=$((RANDOM_START_DAY + RANDOM_1D))
        RANDOM_3D=$(cat /dev/urandom | tr -dc '0-9' | fold -w 3 | head -n 1)
        RANDOM_CERT_NAME="CERT ${RANDOM_3D}"
        RANDOM_5A=$(cat /dev/urandom | tr -dc 'A-Z' | fold -w 5 | head -n 1)
        RANDOM_ISSUER_NAME="ISSUER ${RANDOM_5A}"
        RANDOM_64H=$(cat /dev/urandom | tr -dc 'A-F0-9' | fold -w 64 | head -n 1)
	RANDOM_PUBKEY="02${RANDOM_64H}"
        RANDOM_33H=$(cat /dev/urandom | tr -dc 'A-F0-9' | fold -w 33 | head -n 1)
	RANDOM_RADDRESS="R${RANDOM_33H}"
        RANDOM_9D=$(cat /dev/urandom | tr -dc '0-9' | fold -w 9 | head -n 1)
	RANDOM_CERT_ID="C-${RANDOM_9D}"
	CERT_ISSUE_DATE="${YEAR}-${START_MONTH}-${RANDOM_START_DAY}"
	CERT_EXPIRY_DATE="${YEAR}-${END_MONTH}-${END_DAY}"
	CERT_1_ID=$(curl -s -X POST -H "Content-Type: application/json" ${API_HOST}${API_VER}certificate/ -d "{ \"name\": \"${RANDOM_CERT_NAME}\",\"pubkey\": \"${RANDOM_PUBKEY}\",\"raddress\": \"${RANDOM_RADDRESS}\", \"issuer\": \"${RANDOM_ISSUER_NAME}\", \"identifier\": \"${RANDOM_CERT_ID}\", \"date_issue\": \"${CERT_ISSUE_DATE}\", \"date_expiry\": \"${CERT_EXPIRY_DATE}\", \"organization\": ${ORG_ID}}" | jq '.id')
	echo ${CERT_1_ID}

        RANDOM_START_DAY=$(cat /dev/urandom | tr -dc '1-2' | fold -w 2 | head -n 1)
        END_DAY=$((RANDOM_START_DAY + RANDOM_1D))
        RANDOM_3D=$(cat /dev/urandom | tr -dc '0-9' | fold -w 3 | head -n 1)
        RANDOM_CERT_NAME="CERT ${RANDOM_3D}"
        RANDOM_5A=$(cat /dev/urandom | tr -dc 'A-Z' | fold -w 5 | head -n 1)
        RANDOM_ISSUER_NAME="ISSUER ${RANDOM_5A}"
        RANDOM_64H=$(cat /dev/urandom | tr -dc 'A-F0-9' | fold -w 64 | head -n 1)
	RANDOM_PUBKEY="02${RANDOM_64H}"
        RANDOM_33H=$(cat /dev/urandom | tr -dc 'A-F0-9' | fold -w 33 | head -n 1)
	RANDOM_RADDRESS="R${RANDOM_33H}"
        RANDOM_9D=$(cat /dev/urandom | tr -dc '0-9' | fold -w 9 | head -n 1)
	RANDOM_CERT_ID="C-${RANDOM_9D}"
	CERT_ISSUE_DATE="${YEAR}-${START_MONTH}-${RANDOM_START_DAY}"
	CERT_EXPIRY_DATE="${YEAR}-${END_MONTH}-${END_DAY}"
	CERT_2_ID=$(curl -s -X POST -H "Content-Type: application/json" ${API_HOST}${API_VER}certificate/ -d "{ \"name\": \"${RANDOM_CERT_NAME}\",\"pubkey\": \"${RANDOM_PUBKEY}\",\"raddress\": \"${RANDOM_RADDRESS}\", \"issuer\": \"${RANDOM_ISSUER_NAME}\", \"identifier\": \"${RANDOM_CERT_ID}\", \"date_issue\": \"${CERT_ISSUE_DATE}\", \"date_expiry\": \"${CERT_EXPIRY_DATE}\", \"organization\": ${ORG_ID}}" | jq '.id')
	echo ${CERT_2_ID}

	echo "Create cert rules"
	CONDITION=${LOCATION_1_RADDRESS}
	CERT_1_RULE_NAME="Match Location ${LOCATION_1}"
        RANDOM_64H=$(cat /dev/urandom | tr -dc 'A-F0-9' | fold -w 64 | head -n 1)
	RANDOM_PUBKEY="02${RANDOM_64H}"
        RANDOM_33H=$(cat /dev/urandom | tr -dc 'A-F0-9' | fold -w 33 | head -n 1)
	RANDOM_RADDRESS="R${RANDOM_33H}"
	CERT_1_RULE_1_ID=$(curl -s -X POST -H "Content-Type: application/json" ${API_HOST}${API_VER}certificate-rule/ -d "{ \"name\": \"${CERT_1_RULE_NAME}\",\"pubkey\": \"${RANDOM_PUBKEY}\",\"raddress\": \"${RANDOM_RADDRESS}\", \"condition\": \"${CONDITION}\", \"certificate\": ${CERT_1_ID}}" | jq '.id')
	echo ${CERT_1_RULE_1_ID}

	CONDITION=${LOCATION_2_RADDRESS}
	CERT_2_RULE_NAME="Match Location ${LOCATION_2}"
        RANDOM_64H=$(cat /dev/urandom | tr -dc 'A-F0-9' | fold -w 64 | head -n 1)
	RANDOM_PUBKEY="02${RANDOM_64H}"
        RANDOM_33H=$(cat /dev/urandom | tr -dc 'A-F0-9' | fold -w 33 | head -n 1)
	RANDOM_RADDRESS="R${RANDOM_33H}"
	CERT_2_RULE_1_ID=$(curl -s -X POST -H "Content-Type: application/json" ${API_HOST}${API_VER}certificate-rule/ -d "{ \"name\": \"${CERT_2_RULE_NAME}\",\"pubkey\": \"${RANDOM_PUBKEY}\",\"raddress\": \"${RANDOM_RADDRESS}\", \"condition\": \"${CONDITION}\", \"certificate\": ${CERT_2_ID}}" | jq '.id')
	echo ${CERT_2_RULE_1_ID}

        RANDOM_1D=$(cat /dev/urandom | tr -dc '1-3' | fold -w 1 | head -n 1)
	CONDITION="100402100${RANDOM_1D}"
	CERT_2_RULE_NAME="Match Material ${CONDITION}"
        RANDOM_64H=$(cat /dev/urandom | tr -dc 'A-F0-9' | fold -w 64 | head -n 1)
	RANDOM_PUBKEY="02${RANDOM_64H}"
        RANDOM_33H=$(cat /dev/urandom | tr -dc 'A-F0-9' | fold -w 33 | head -n 1)
	RANDOM_RADDRESS="R${RANDOM_33H}"
	CERT_2_RULE_2_ID=$(curl -s -X POST -H "Content-Type: application/json" ${API_HOST}${API_VER}certificate-rule/ -d "{ \"name\": \"${CERT_2_RULE_NAME}\",\"pubkey\": \"${RANDOM_PUBKEY}\",\"raddress\": \"${RANDOM_RADDRESS}\", \"condition\": \"${CONDITION}\", \"certificate\": ${CERT_2_ID}}" | jq '.id')
	echo ${CERT_2_RULE_2_ID}
done
