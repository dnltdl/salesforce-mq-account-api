# MuleSoft Salesforce Project

This project connects to Salesforce, retrieves Account information, transforms the data, and sends it to an ActiveMQ queue. It exposes this functionality as a Flask REST API.

## Setup

1. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

2. Update the `config/dev.yaml` file with your Salesforce credentials.

3. Run the Flask API:
    ```bash
    python main.py
    ```

4. Access the API endpoint:
    ```
    GET http://localhost:5000/retrieve-and-send
    ```

## Project Structure