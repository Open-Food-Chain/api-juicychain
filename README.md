# juicychain-api

1. Clone repo
2. Create virtual env
3. Activate venv
4. Install requirements
5. Run dev server
6. In another terminal post some data using script

```
git clone repo_url
cd repo
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cd src
python manage.py runserver 8888
```
Another terminal, edit file as required
```
cd scripts
./noauth-post.sh
```

# RPC to blockchain
* http://url:8888/rpc/v1dev/getinfo

# API
* http://url:8888/batches/v1dev
* http://url:8888/certificates/v1dev
* http://url:8888/product-journey/v1dev
