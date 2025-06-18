from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
from pathlib import Path


async def get_users(db: Session):

    query = db.query(models.Users)

    users_all = query.all()
    users_all = (
        [new_data.to_dict() for new_data in users_all] if users_all else users_all
    )
    res = {
        "users_all": users_all,
    }
    return res


async def get_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    users_one = query.first()

    users_one = (
        (users_one.to_dict() if hasattr(users_one, "to_dict") else vars(users_one))
        if users_one
        else users_one
    )

    res = {
        "users_one": users_one,
    }
    return res


async def post_users(db: Session, raw_data: schemas.PostUsers):
    id: int = raw_data.id
    name: str = raw_data.name
    contact_details: str = raw_data.contact_details

    record_to_be_added = {"id": id, "name": name, "contact_details": contact_details}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        "users_inserted_record": users_inserted_record,
    }
    return res


async def put_users_id(db: Session, id: int, name: str, contact_details: str):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))
    users_edited_record = query.first()

    if users_edited_record:
        for key, value in {
            "id": id,
            "name": name,
            "contact_details": contact_details,
        }.items():
            setattr(users_edited_record, key, value)

        db.commit()
        db.refresh(users_edited_record)

        users_edited_record = (
            users_edited_record.to_dict()
            if hasattr(users_edited_record, "to_dict")
            else vars(users_edited_record)
        )
    res = {
        "users_edited_record": users_edited_record,
    }
    return res


async def delete_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict()
    else:
        users_deleted = record_to_delete
    res = {
        "users_deleted": users_deleted,
    }
    return res


async def get_services(db: Session):

    query = db.query(models.Services)

    services_all = query.all()
    services_all = (
        [new_data.to_dict() for new_data in services_all]
        if services_all
        else services_all
    )
    res = {
        "services_all": services_all,
    }
    return res


async def get_services_id(db: Session, id: int):

    query = db.query(models.Services)
    query = query.filter(and_(models.Services.id == id))

    services_one = query.first()

    services_one = (
        (
            services_one.to_dict()
            if hasattr(services_one, "to_dict")
            else vars(services_one)
        )
        if services_one
        else services_one
    )

    res = {
        "services_one": services_one,
    }
    return res


async def post_services(db: Session, raw_data: schemas.PostServices):
    id: int = raw_data.id
    name: str = raw_data.name
    duration: int = raw_data.duration
    cost: str = raw_data.cost

    record_to_be_added = {"id": id, "cost": cost, "name": name, "duration": duration}
    new_services = models.Services(**record_to_be_added)
    db.add(new_services)
    db.commit()
    db.refresh(new_services)
    services_inserted_record = new_services.to_dict()

    res = {
        "services_inserted_record": services_inserted_record,
    }
    return res


async def put_services_id(db: Session, id: int, name: str, duration: int, cost: str):

    query = db.query(models.Services)
    query = query.filter(and_(models.Services.id == id))
    services_edited_record = query.first()

    if services_edited_record:
        for key, value in {
            "id": id,
            "cost": cost,
            "name": name,
            "duration": duration,
        }.items():
            setattr(services_edited_record, key, value)

        db.commit()
        db.refresh(services_edited_record)

        services_edited_record = (
            services_edited_record.to_dict()
            if hasattr(services_edited_record, "to_dict")
            else vars(services_edited_record)
        )
    res = {
        "services_edited_record": services_edited_record,
    }
    return res


async def delete_services_id(db: Session, id: int):

    query = db.query(models.Services)
    query = query.filter(and_(models.Services.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        services_deleted = record_to_delete.to_dict()
    else:
        services_deleted = record_to_delete
    res = {
        "services_deleted": services_deleted,
    }
    return res


async def get_appointments(db: Session):

    query = db.query(models.Appointments)

    appointments_all = query.all()
    appointments_all = (
        [new_data.to_dict() for new_data in appointments_all]
        if appointments_all
        else appointments_all
    )
    res = {
        "appointments_all": appointments_all,
    }
    return res


async def get_appointments_id(db: Session, id: int):

    query = db.query(models.Appointments)
    query = query.filter(and_(models.Appointments.id == id))

    appointments_one = query.first()

    appointments_one = (
        (
            appointments_one.to_dict()
            if hasattr(appointments_one, "to_dict")
            else vars(appointments_one)
        )
        if appointments_one
        else appointments_one
    )

    res = {
        "appointments_one": appointments_one,
    }
    return res


async def post_appointments(db: Session, raw_data: schemas.PostAppointments):
    id: int = raw_data.id
    scheduled_time: str = raw_data.scheduled_time
    user_id: int = raw_data.user_id
    service_id: int = raw_data.service_id
    calendar_event_id: str = raw_data.calendar_event_id

    record_to_be_added = {
        "id": id,
        "user_id": user_id,
        "service_id": service_id,
        "scheduled_time": scheduled_time,
        "calendar_event_id": calendar_event_id,
    }
    new_appointments = models.Appointments(**record_to_be_added)
    db.add(new_appointments)
    db.commit()
    db.refresh(new_appointments)
    appointments_inserted_record = new_appointments.to_dict()

    res = {
        "appointments_inserted_record": appointments_inserted_record,
    }
    return res


async def put_appointments_id(
    db: Session,
    id: int,
    scheduled_time: str,
    user_id: int,
    service_id: int,
    calendar_event_id: str,
):

    query = db.query(models.Appointments)
    query = query.filter(and_(models.Appointments.id == id))
    appointments_edited_record = query.first()

    if appointments_edited_record:
        for key, value in {
            "id": id,
            "user_id": user_id,
            "service_id": service_id,
            "scheduled_time": scheduled_time,
            "calendar_event_id": calendar_event_id,
        }.items():
            setattr(appointments_edited_record, key, value)

        db.commit()
        db.refresh(appointments_edited_record)

        appointments_edited_record = (
            appointments_edited_record.to_dict()
            if hasattr(appointments_edited_record, "to_dict")
            else vars(appointments_edited_record)
        )
    res = {
        "appointments_edited_record": appointments_edited_record,
    }
    return res


async def delete_appointments_id(db: Session, id: int):

    query = db.query(models.Appointments)
    query = query.filter(and_(models.Appointments.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        appointments_deleted = record_to_delete.to_dict()
    else:
        appointments_deleted = record_to_delete
    res = {
        "appointments_deleted": appointments_deleted,
    }
    return res
