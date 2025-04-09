from pydantic import BaseModel

class MTNDatasyncCallback(BaseModel):
    msisdn: str
    serviceId: str
    productId: str
    status: str
    message: str
    transactionId: str


class AirtelDatasyncCallback(BaseModel):
    msisdn: str
    productId: str
    serviceId: str
    status: str
    message: str
    transactionId: str

class UnsubscribeRequest(BaseModel):
    msisdn: str
    product_id: str
    service_id: str
    transaction_id: str

class USSDResponse(BaseModel):
    msisdn: str
    serviceCode: str
    text: str
    sessionId: str
    responseType: str


class USSDRequestNotification(BaseModel):
    msisdn: str
    serviceCode: str
    text: str
    sessionId: str

class MTSMSRequest(BaseModel):
    msisdn: str
    message: str
    sender: str