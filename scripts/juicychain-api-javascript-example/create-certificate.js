const axios = require('axios')

const BASE_URL="http://juicychain-api.thenewfork.staging.do.unchain.io/"
const API_VER="api/v1/"
const CREATE_CERTIFICATE="certificate/"
const CREATE_CERTIFICATE_URL=BASE_URL + API_VER + CREATE_CERTIFICATE

console.log(CREATE_CERTIFICATE_URL)
/*
curl -s -X POST -H 'Content-Type: application/json' http://juicychain-api.thenewfork.staging.do.unchain.io/api/v1/certificate/ -d '{ "name": "CERT MYLO", "issuer": "ISSUER MYLO.COM", "identifier": "C-233200777", "date_issue": "2020-01-11", "date_expiry": "2020-12-20", "organization": 35, "pubkey": "", "raddress": ""}'
 */
let request_data = { name: "JS CERT", issuer: "ISSUER JS", identifier: "C-233201777", date_issue: "2020-01-11", date_expiry: "2020-12-20", organization: 35, pubkey: "", raddress: ""}
let response = sendRequest(CREATE_CERTIFICATE_URL, request_data)

function sendRequest(url, requestData) {
	return axios.post(url, requestData)
		.then(res => {
			console.log(res.data)
			/* example response
			{
			  id: 66,
			  name: 'JS CERT',
			  date_issue: '2020-01-11',
			  date_expiry: '2020-12-20',
			  issuer: 'ISSUER JS',
			  identifier: 'C-233201777',
			  pubkey: '',
			  raddress: '',
			  organization: 35
			}
			*/

			return res.data
		})
		.catch(err => console.error(err))
}
