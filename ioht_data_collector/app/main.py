from app.routers import *

from fastapi import FastAPI


description = '''
IOHT Data Collector is used to collect IOHT datasets
'''
app = FastAPI(
    title='IOHT Data Collector',
    description=description,
    version='1.0',
    contact={
        'name': 'Peter',
        'email': 'peter279k@gmail.com',
    }
)
