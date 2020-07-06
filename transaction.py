from flask import Flask
application = Flask(__name__)

@application.route("/get_all_transactions", method=["GET"])
def get_all_transactions():
    return "Return all transactions"

@application.route("/get_transaction/<transaction_id>")
def get_transaction(transaction_id=None)
	return "Return " + transaction_id


if __name__ == "__main__":
    application.run()
