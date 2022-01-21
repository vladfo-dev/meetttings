import logging
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from backend.app.crud import meet as crud_meet
from backend.app.schemas import meet as schema_meet
from backend.app.utils.get_db import get_db_func
meet_route = APIRouter()
log = logging.getLogger(__name__)


@meet_route.post(
    '/create',
    tags=['meet'],
    response_model=None,
    summary='Create meet'
)
def create_meet(create_info: schema_meet.CreateMeetIn, db: Session = Depends(get_db_func)):
    """
    Creates a meet and responses with code to join it
    Returns:
        response with code to join it
    """
    log.info("Started POST /meet/create")
    return crud_meet.create_meet(username=create_info.username, db=db)
