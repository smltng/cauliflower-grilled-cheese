# This is the entry point for this application

import connexion

options = {"swagger_ui": True}
app = connexion.App(__name__, specification_dir='swagger/', options=options, server='gevent')
app.add_api('api.yaml')

if __name__ == "__main__":
    app.run(port=8080)
