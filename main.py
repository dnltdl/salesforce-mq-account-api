from flask import Flask, jsonify
from src.salesforce_connector import get_salesforce_connection, query_accounts
from src.transformer import transform_accounts
from src.jms_sender import send_to_jms_queue

app = Flask(__name__)

@app.route('/retrieve-and-send', methods=['GET'])
def retrieve_and_send():
    try:
        # Connect to Salesforce
        sf = get_salesforce_connection()

        # Query Salesforce Account object
        accounts = query_accounts(sf)

        # Transform the response
        transformed_accounts = transform_accounts(accounts)

        # Send to JMS Queue
        send_to_jms_queue(transformed_accounts)

        return jsonify({"message": "Data retrieved and sent to JMS queue successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)