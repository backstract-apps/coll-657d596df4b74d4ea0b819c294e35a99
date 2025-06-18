from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id')
async def get_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(id: int, name: Annotated[str, Query(max_length=100)], contact_details: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_users_id(db, id, name, contact_details)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id')
async def delete_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/services/')
async def get_services(db: Session = Depends(get_db)):
    try:
        return await service.get_services(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/services/id')
async def get_services_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_services_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/services/')
async def post_services(raw_data: schemas.PostServices, db: Session = Depends(get_db)):
    try:
        return await service.post_services(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/services/id/')
async def put_services_id(id: int, name: Annotated[str, Query(max_length=100)], duration: int, cost: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_services_id(db, id, name, duration, cost)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/services/id')
async def delete_services_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_services_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/appointments/')
async def get_appointments(db: Session = Depends(get_db)):
    try:
        return await service.get_appointments(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/appointments/id')
async def get_appointments_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_appointments_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/appointments/')
async def post_appointments(raw_data: schemas.PostAppointments, db: Session = Depends(get_db)):
    try:
        return await service.post_appointments(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/appointments/id/')
async def put_appointments_id(id: int, scheduled_time: Annotated[str, Query(max_length=100)], user_id: int, service_id: int, calendar_event_id: Annotated[str, Query(max_length=100)], db: Session = Depends(get_db)):
    try:
        return await service.put_appointments_id(db, id, scheduled_time, user_id, service_id, calendar_event_id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/appointments/id')
async def delete_appointments_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_appointments_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

