* Links
	* CORS - https://stackoverflow.com/questions/26980713/solve-cross-origin-resource-sharing-with-flask
	* AdWords API Client Libraries - https://developers.google.com/adwords/api/docs/clientlibraries

* TODO 
	* Fix CORS so not *

```
pip install -r requirements.txt

export FLASK_APP=server.py
flask run

curl -i "http://localhost:5000/"
curl -i "http://localhost:5000/api/v1.0/query?query=None&my_param=abc"
```
