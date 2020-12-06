# openfood api docs

## open urls
* api/v1/organization
	* get:
		* params: name
		* return: Oranization opbject with properties: "id",  "name",  "pubkey",  "raddress"
	* post:
		* params: Oranization opbject with properties: "id",  "name",  "pubkey",  "raddress"
		* return: id
	* head:
		* params: name
		* return: only the metadata
	* options:
		* params: nothing
		* return: get, post, head, options
* api/v1/organization-detail
	* get: 
		* params: name
		* return: an Organization object opbject with properties: "id",  "name",  "pubkey",  "raddress", only a location object is added with properties: "location":  [  {  "raddress",  "pubkey",  "name"}  ], certificates with properties: "certificate":  [  {  "rule":  [],  "name",  "raddress",  "pubkey":,  "date_issue",  "date_expiry",  "issuer",  "identifier" }  ], and batches with properties: "batch":  [  {  "raddress",  "pubkey",  "identifier",  "jds",  "jde",  "date_production_start",  "date_best_before",  "origin_country" }  ]
	* post: 
		* params: an Organization object opbject with properties: "id",  "name",  "pubkey",  "raddress", only a location object is added with properties: "location":  [  {  "raddress",  "pubkey",  "name"}  ], certificates with properties: "certificate":  [  {  "rule":  [],  "name",  "raddress",  "pubkey":,  "date_issue",  "date_expiry",  "issuer",  "identifier" }  ], and batches with properties: "batch":  [  {  "raddress",  "pubkey",  "identifier",  "jds",  "jde",  "date_production_start",  "date_best_before",  "origin_country" }  ]
		* return: id
	* head:
		* params: name
		* return: only the metadata
	* options:
		* params: nothing
		* return: get, post, head, options
* api/v1/location
	* get: 
		* params: id
		* return: a location object with properties: "location":  [  {  "raddress",  "pubkey",  "name"}  ]
	* post:
		* params: a location object with properties: "location":  [  {  "raddress",  "pubkey",  "name"}  ]
		* return: id
	* put:
		* params: a location object with properties: "location":  [  {  "raddress",  "pubkey",  "name"}  ]
		* return: id
	* patch:
		* params: a location object with properties: "location":  [  {  "raddress",  "pubkey",  "name"}  ]
		* return: id
	* delete:
		* params: id
		* return: nothing
	* head:
		* params: id
		* return: only the metadata
	* options:
		* params: nothing
		* return: get, post, put, delete, patch, head, options
* api/v1/certificate
	* get:
		* params: id
		* return: a certificate object with properties: "certificate":  [  {  "rule":  [],  "name",  "raddress",  "pubkey":,  "date_issue",  "date_expiry",  "issuer",  "identifier" }  ]
	* post:
		* params: a certificate object with properties: "certificate":  [  {  "rule":  [],  "name",  "raddress",  "pubkey":,  "date_issue",  "date_expiry",  "issuer",  "identifier" }  ]
		* return: id
	* head:
		* params: a certificate object with properties: "certificate":  [  {  "rule":  [],  "name",  "raddress",  "pubkey":,  "date_issue",  "date_expiry",  "issuer",  "identifier" }  ]
		* return: only metadata
	* options:
		* params: nothing
		* return: get, post, head, options
* api/v1/certificate-rule
	* get:
		* params: id
		* return:  a certifucate rule object with properties:  {  "id",  "name",  "condition",  "pubkey",  "raddress",  "certificate"}
	* post:
		* params: a certifucate rule object with properties:  {  "id",  "name",  "condition",  "pubkey",  "raddress",  "certificate"}
		* return: id
	* head:
		* params: a certifucate rule object with properties:  {  "id",  "name",  "condition",  "pubkey",  "raddress",  "certificate"}
		* return: only metadata
	* options:
		* params: nothing
		* return: get, post, head, options
* api/v1/batch
	* get:
		* params: id
		* return: batches with properties: "batch":  [  {  "raddress",  "pubkey",  "identifier",  "jds",  "jde",  "date_production_start",  "date_best_before",  "origin_country" }  ]
	* post:
		* params: batches with properties: "batch":  [  {  "raddress",  "pubkey",  "identifier",  "jds",  "jde",  "date_production_start",  "date_best_before",  "origin_country" }  ]
		* return: id
	* head: 
		* params: id
		* return: only metadata
	* options:
		* params: nothing
		* return: get, post, head, options
* api/v1/organization/(?P<id>\\d+)/location
	* get:
		* params:  nothing		
		 * return: location objects with properties: "location":  [  {  "raddress",  "pubkey",  "name"}  ] that have the organization as organization that is selected in the url
	* head:
		* params: nothing
		* return: only metadata
	* options:
		* params: nothing
		* return: get, head, options
* api/v1/organization/(?P<id>\\d+)/certificate
	* get:
		* params: nothing
		* return: a certificate object with properties: "certificate":  [  {  "rule":  [],  "name",  "raddress",  "pubkey":,  "date_issue",  "date_expiry",  "issuer",  "identifier" }  ] and has the organization selected as organization
	* head:
		* params: nothing
		* return: only metadata
	* options:
		* params: nothing
		* return: post, head, options


