# from flask import Flask
from flask_api import FlaskAPI

application = FlaskAPI(__name__)

# application = Flask(__name__)

@application.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@application.route("/transactions/get_all_transactions", methods=['GET'])
def get_all_transactions():
    return "Return all transactions"

@application.route("/transactions/get_transaction/<transaction_id>", methods=['GET', 'POST'])
def get_transaction(transaction_id=None):
	return "Return " + transaction_id

@application.route('/example', methods=['GET'])
def example():
    return {'hello': 'world'}

@application.route('/example2', methods=['GET'])
def example2():
	return {'hello': 'dunia'}

if __name__ == "__main__":
    # application.run()
    application.run(debug=True)

