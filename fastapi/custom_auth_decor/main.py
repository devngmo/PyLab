from optparse import Option
from fastapi import FastAPI, HTTPException, Body, Header, Depends

app = FastAPI(title='API using Custom Authentication Decorator')

REQUIRE_AUTHORIZATION = True

def OptionalAuthorization(func):
    if REQUIRE_AUTHORIZATION:
        def wrapper():
            func(Header(alias='token'))
        return wrapper
    else:
        def wrapper():
            func(Header(alias='apikey'))
        return wrapper


@app.get('/')
def welcome():
    return 'welcome'

@OptionalAuthorization
@app.get('/secured/secret')
def secured_secret(token):
    return f'my secret here => {token}'