import connexion

options = {"swagger_ui": True}
app = connexion.App(__name__, specification_dir='swagger/', options=options, server='gevent')
app.add_api('api.yaml')
app.run(port=8080)