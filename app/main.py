from fastapi import FastAPI, Depends, Header, HTTPException, Request
from fastapi.responses import Response
from app.settings import settings
import logging

# File logging
logging.basicConfig(filename='app.log', level=logging.INFO)

app = FastAPI()

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != settings.APP_SECRET:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return x_api_key

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    # Simulated rate limit check: 100 requests/minute
    return await call_next(request)

@app.get("/health")
def health_check():
    return Response(content="<status>ok</status>", media_type="application/xml")

@app.get("/v1/users", dependencies=[Depends(verify_api_key)])
def get_users():
    xml_data = "<users><user><id>1</id><name>Alice</name></user></users>"
    return Response(content=xml_data, media_type="application/xml")
