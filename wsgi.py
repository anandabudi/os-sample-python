from flask import Flask
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

if __name__ == "__main__":
    application.run()

