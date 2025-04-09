# FastAPI BBC Aggregator Integration

This project integrates with the **BBC Aggregator JSON API** and provides endpoints for various telecommunication services like **MTN**, **Airtel**, and **USSD** services. The application is built using **FastAPI** and supports interaction with APIs like subscription, unsubscription, callback handling, and SMS services.

## Features
- Handle MTN Datasync Subscription & Callback
- Handle Airtel Datasync Callback & Unsubscription
- USSD Response & Request Notifications
- MT-SMS API Integration
- MO-SMS Callback Integration

## Prerequisites

To run this application on your local machine, ensure you have the following installed:

- Python 3.9+
- pip (Python package manager)
- Virtual environment (optional, but recommended)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/oluwabunmifife/bbc-aggregator-integration.git
   cd bbc-aggregator-integration
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python3 -m venv bbc
   source bbc/bin/activate # On Windows: bbc\Scripts\activate

3. Install dependencies:
   ```
    pip install -r requirements.txt # Or pip3 install -r requirements.txt
   ```

4. Create a .env file in the root directory with your API credentials. Example .env content:
   ```
    BBC_API_BASE_URL=https://api.broadbased.xyz
    SP_ID=your_sp_id
    PASSWORD=your_password
    SENDER_NAME=BBC
    MT_SMS_URL=http://41.76.198.1:6211/app/json/vas
    AIRTEL_CALLBACK_TOKEN=some_token
    MTN_CALLBACK_TOKEN=some_other_token
   ```

## Running the application

1. Start the FastAPI server:
   ```
    uvicorn main:app --reload
   ```

2. The application should now be running at http://127.0.0.1:8000. You can access the API documentation at:
   ```
    http://127.0.0.1:8000/docs
   ```

## Exposing Local Server via Ngrok
If you want to expose your local FastAPI server to the public internet (for example, to test with an external service like BBC Aggregator), you can use **ngrok**.


1. Visit https://ngrok.com/download

2. Run ngrok on the port FastAPI is running (default: 8000):
   ```
    ngrok http 8000
   ```

3. ngrok will provide a public URL like:
   ```
    https://abcd1234.ngrok.io
   ```

4. Use this public URL to send requests to your local FastAPI server, especially when interacting with external APIs that need a public endpoint.

Make sure to update your environment variables (e.g., callback URLs) with the ngrok URL for proper testing.