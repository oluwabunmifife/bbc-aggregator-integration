import httpx
import os
import hashlib
from dotenv import load_dotenv
from datetime import datetime

from models import USSDResponse, MTSMSRequest

# Load environment variables
load_dotenv()
SP_ID = os.getenv("SP_ID")
PASSWORD = os.getenv("PASSWORD")
BASE_URL = os.getenv("BASE_URL")

async def initiate_subscription(msisdn: str, service_id: str, product_id: str, channel_id: int, transaction_id: str, amount: float = None):
    # Generate timeStamp in UTC
    time_stamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    
    # Generate spPassword
    sp_password = hashlib.md5(f"{SP_ID}{PASSWORD}{time_stamp}".encode()).hexdigest()
    
    # Headers
    headers = {
        "spId": SP_ID,
        "spPassword": sp_password,
        "timeStamp": time_stamp
    }
    
    # Payload
    payload = {
        "msisdn": msisdn,
        "serviceId": service_id,
        "productId": product_id,
        "channelId": channel_id,
        "transactionId": transaction_id
    }
    
    if amount is not None:
        payload["amount"] = amount
    
    # Endpoint URL
    url = f"{BASE_URL}/initiateSubscription"
    
    # Make the request
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
    
    # Handle response
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# Unsubscribe Function
async def unsubscribe_user(msisdn: str, product_id: str, service_id: str, transaction_id: str):
    time_stamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    sp_password = hashlib.md5(f"{SP_ID}{PASSWORD}{time_stamp}".encode()).hexdigest()

    headers = {
        "spId": SP_ID,
        "spPassword": sp_password,
        "timeStamp": time_stamp
    }

    payload = {
        "msisdn": msisdn,
        "productId": product_id,
        "serviceId": service_id,
        "transactionId": transaction_id
    }

    url = f"{BASE_URL}/unsubscribe"

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


async def send_ussd_response(ussd_response: USSDResponse):
    url = f"{BASE_URL}/ussd/response"

    headers = {
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=ussd_response.dict(), headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


async def send_mt_sms(sms: MTSMSRequest):
    url = f"{BASE_URL}/sms/send"
    headers = {"Content-Type": "application/json"}

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=sms.dict(), headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()