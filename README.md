# flasklate
A code template to start Flask projects


## Without Docker

```
virtualenv -p python3 my_app
cd my_app
. bin/activate
git clone https://github.com/eon01/flasklate.git app
cd app
pip install -r requirements.txt
export FLASK_APP=app.py
flask run
```


## With Docker

```
git clone https://github.com/eon01/flasklate.git app
cd app
docker build -t my_app . 
docker run -it --name my_app -p 80:5000 my_app
```

