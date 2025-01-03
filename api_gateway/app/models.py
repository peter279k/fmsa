from pydantic import BaseModel


class RegisterAccount(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str

class LoginAccount(BaseModel):
    username: str
    password: str
 
