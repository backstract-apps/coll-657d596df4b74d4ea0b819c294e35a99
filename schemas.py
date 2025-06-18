from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Users(BaseModel):
    id: Any
    name: str
    contact_details: str


class ReadUsers(BaseModel):
    id: Any
    name: str
    contact_details: str
    class Config:
        from_attributes = True


class Services(BaseModel):
    id: Any
    name: str
    duration: int
    cost: float


class ReadServices(BaseModel):
    id: Any
    name: str
    duration: int
    cost: float
    class Config:
        from_attributes = True


class Appointments(BaseModel):
    id: Any
    scheduled_time: Any
    user_id: int
    service_id: int
    calendar_event_id: str


class ReadAppointments(BaseModel):
    id: Any
    scheduled_time: Any
    user_id: int
    service_id: int
    calendar_event_id: str
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    id: int = Field(...)
    name: str = Field(..., max_length=100)
    contact_details: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostServices(BaseModel):
    id: int = Field(...)
    name: str = Field(..., max_length=100)
    duration: int = Field(...)
    cost: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostAppointments(BaseModel):
    id: int = Field(...)
    scheduled_time: str = Field(..., max_length=100)
    user_id: int = Field(...)
    service_id: int = Field(...)
    calendar_event_id: str = Field(..., max_length=100)

    class Config:
        from_attributes = True

