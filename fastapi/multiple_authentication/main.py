from optparse import Option
from fastapi import FastAPI, HTTPException, Body, Header, Depends

app = FastAPI(title='API using Multiple Authentication with Dependencies')

AUTH_JWT = 'jwt'
AUTH_USERID = 'userid'
AUTH_APIKEY = 'apikey'
SUPPORT_AUTHENTICATIONS = [AUTH_APIKEY, AUTH_JWT, AUTH_USERID]

@app.get('/')
def welcome():
    return 'welcome'

async def ApikeyCheck(apikey=Header(None)):
    if AUTH_APIKEY in SUPPORT_AUTHENTICATIONS:
        if not apikey:
            return None
        
        if apikey == 'secret':
            return { 'client':'tester' }
        return None
    return None

async def UserIDCheck(user_id=Header(None)):
    if AUTH_USERID in SUPPORT_AUTHENTICATIONS:
        if not user_id:
            return None
        
        return { 'client':user_id }
    return None

@app.get('/secured/secret', dependencies=[Depends(ApikeyCheck), Depends(UserIDCheck)])
def secured_secret(user_id):
    return f'my secret here => {user_id}'