from pydantic import BaseModel


class RegisterAccount(BaseModel):
    username: str
    password: str
