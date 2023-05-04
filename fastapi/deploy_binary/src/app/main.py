from optparse import Option
from fastapi import FastAPI, HTTPException, Body, Header, Depends

app = FastAPI(title='Simple API to test deploy binary')

@app.get('/')
def welcome():
    return 'Congratulation! Your binary deployment success'