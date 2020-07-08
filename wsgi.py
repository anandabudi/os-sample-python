from flask import Flask
from flask_api import FlaskAPI

api = FlaskAPI(__name__)

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/transactions/get_all_transactions")
def get_all_transactions():
    return "Return all transactions"

@application.route("/transactions/get_transaction/<transaction_id>")
def get_transaction(transaction_id=None):
	return "Return " + transaction_id

@app.route('/example/')
def example():
    return {'hello': 'world'}

if __name__ == "__main__":
    application.run()
    api.run(debug=True)

