from app.routers import *

from fastapi import FastAPI


description = '''
Data Analysis Service is used to calculate statistics value
'''
app = FastAPI(
    title='Data Analysis Service',
    description=description,
    version='1.0',
    contact={
        'name': 'Peter',
        'email': 'peter279k@gmail.com',
    }
)

app.include_router(analysis_router)
