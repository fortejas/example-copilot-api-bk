from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'hello': 'world'}


@app.get('/health')
def read_health():
    return {'status': 'ok'}
