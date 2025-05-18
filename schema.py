from pydantic import BaseModel



class EmailBody(BaseModel):
    message:str
    user_email:str
    subject:str
    correllation_id: str
