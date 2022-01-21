from pydantic import BaseModel, validator


class CreateMeetResponse(BaseModel):
    join_code: str


class CreateMeetIn(BaseModel):
    username: str

    @validator('username')
    def validate_username(cls, value: str):
        if len(value) <= 2 or len(value) > 33:
            raise ValueError('username must be from 3 to 32 symbols')
        return value
