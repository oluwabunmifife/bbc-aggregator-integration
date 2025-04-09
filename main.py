import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# bbc_client functions
from bbc_client import initiate_subscription, unsubscribe_user, send_ussd_response, send_mt_sms

# Models
from models import (
    MTNDatasyncCallback, 
    AirtelDatasyncCallback, 
    UnsubscribeRequest, 
    USSDResponse, 
    USSDRequestNotification, 
    MTSMSRequest

)
app = FastAPI()

class SubscriptionRequest(BaseModel):
    msisdn: str
    service_id: str
    product_id: str
    channel_id: int
    transaction_id: str
    amount: float = None

@app.post("/subscribe")
async def subscribe_user(request: SubscriptionRequest):
    try:
        response = await initiate_subscription(
            msisdn=request.msisdn,
            service_id=request.service_id,
            product_id=request.product_id,
            channel_id=request.channel_id,
            transaction_id=request.transaction_id,
            amount=request.amount
        )
        return response
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/callbacks/mtn/subscription")
async def handle_mtn_subscription_callback(payload: MTNDatasyncCallback):
    # Log or process the callback
    print("MTN Datasync Callback Received:", payload.dict())


    return {
        "status": "received",
        "transactionId": payload.transactionId
    }


@app.post("/callbacks/airtel/subscription")
async def handle_airtel_subscription_callback(payload: AirtelDatasyncCallback):
    print("Airtel Datasync Callback Received:", payload.dict())
    return {"status": "received", "transactionId": payload.transactionId}


@app.post("/unsubscribe")
async def unsubscribe_user_route(request: UnsubscribeRequest):
    try:
        response = await unsubscribe_user(
            msisdn=request.msisdn,
            product_id=request.product_id,
            service_id=request.service_id,
            transaction_id=request.transaction_id
        )
        return response
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/ussd/response")
async def ussd_response_route(response: USSDResponse):
    try:
        result = await send_ussd_response(response)
        return result
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/callbacks/ussd/request")
async def handle_ussd_request(payload: USSDRequestNotification):
    print("Incoming USSD Request:", payload.dict())

    return {"status": "received", "sessionId": payload.sessionId}


@app.post("/sms/send")
async def send_sms_route(sms: MTSMSRequest):
    try:
        result = await send_mt_sms(sms)
        return result
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))