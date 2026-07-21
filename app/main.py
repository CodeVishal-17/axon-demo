from fastapi import FastAPI, Depends, Header, HTTPException, Request
from fastapi.responses import Response
from app.settings import settings
import logging
from app.auth import verify_jwt_token

logging.basicConfig(filename='app.log', level=logging.INFO)

app = FastAPI()

def verify_token(authorization: str = Header(default="")):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="Invalid token")
    token = authorization.split(" ")[1]
    if not verify_jwt_token(token, settings.JWT_SECRET):
        raise HTTPException(status_code=403, detail="Invalid token")
    return token

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    return await call_next(request)

@app.get("/health")
def health_check():
    return Response(content="<status>ok</status>", media_type="application/xml")

@app.get("/v1/users", dependencies=[Depends(verify_token)])
def get_users():
    xml_data = "<users><user><id>1</id><name>Alice</name></user></users>"
    return Response(content=xml_data, media_type="application/xml")
