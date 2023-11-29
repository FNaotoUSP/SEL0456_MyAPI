# SEL0456_MyAPI
API usando arquivo jason como input

Para funcionar são necessários dois terminais rodnado simultaneamente.
- O primeiro deve rodar o arquivo python "main_flask.py";
- O segundo deve rodar o comando "curl -X POST -H "Content-Type: application/json" -d @payload.json http://localhost:5000/myapi", isso considerando que o servidor está sendo executado na porta 5000.
