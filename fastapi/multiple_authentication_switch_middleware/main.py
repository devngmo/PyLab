from optparse import Option
from typing import Union
from fastapi import FastAPI, HTTPException, Body, Header, Depends, Request, Response

app = FastAPI(title='API using Multiple Authentication with Dependencies')

SECURE_MODE_JWT = 'jwt'
SECURE_MODE_ALLOW_ANONYMOUS = 'anonymous'
SECURE_MODE = SECURE_MODE_JWT

@app.middleware('http')
async def auto_switch_auth(request:Request, call_next):

    if SECURE_MODE == SECURE_MODE_JWT:
        apiEndpointPrefix = f"{request.base_url}api"
        if str(request.url).startswith(apiEndpointPrefix):
            print(request.base_url)
            if 'jwt-token' in request.headers:
                jwtToken = request.headers['jwt-token']
                if jwtToken != 'secret':
                    return Response(status_code=404)
                request.state.user_id = 'admin'
            else:
                return Response(status_code=404)
    else:
        request.state.user_id = 'anonymous'
    response = await call_next(request)
    return response

@app.get('/')
def welcome():
    return 'welcome'

@app.get('/api/secured/secret')
def secured_secret(request:Request, jwt_token:Union[str, None]=Header(None)):
    user_id = request.state.user_id
    return f'my secret here => {user_id}'