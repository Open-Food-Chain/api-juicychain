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

# MYLO
```
docker stop simple-working_db_1
docker rm simple-working_db_1
sudo find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
sudo find . -path "*/migrations/*.pyc"  -delete
cd ../..
docker-compose -f docker-compose.yaml.all up -d --remove-orphans db
cd juicychain-api/src
docker exec -i -t simple-working_juicychain-api_1 python manage.py makemigrations
docker exec -i -t simple-working_juicychain-api_1 python manage.py migrate
```
