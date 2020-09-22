const axios = require('axios')

const BASE_URL="http://juicychain-api.thenewfork.staging.do.unchain.io/"
const API_VER="api/v1/"
const CREATE_CERTIFICATE_RULE="certificate-rule/"
const CREATE_CERTIFICATE_RULE_URL=BASE_URL + API_VER + CREATE_CERTIFICATE_RULE

console.log(CREATE_CERTIFICATE_RULE_URL)
/*

curl -s -X POST -H 'Content-Type: application/json' http://juicychain-api.thenewfork.staging.do.unchain.io/api/v1/certificate-rule/ -d '{ "name": "Match Material 1004021003","pubkey": "","raddress": "", "condition": "1004021003", "certificate": 66}'


*/
let request_data = { name: "Match Material 1004021003",pubkey: "",raddress: "", condition: "1004021003", certificate: 66}
let response = sendRequest(CREATE_CERTIFICATE_RULE_URL, request_data)

function sendRequest(url, requestData) {
	return axios.post(url, requestData)
		.then(res => {
			console.log(res.data)
			/* example response
			{
			  id: 77,
			  name: 'Match Material 1004021003',
			  condition: '1004021003',
			  pubkey: '',
			  raddress: '',
			  certificate: 66
			}
			*/

			return res.data
		})
		.catch(err => console.error(err))
}
