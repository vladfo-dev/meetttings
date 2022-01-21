import logging
from sqlalchemy.orm import Session
from backend.app.models.meet import Meet, MeetUser
from backend.app.models.users import Users
from backend.app.utils.gen_code import generate_code
log = logging.getLogger(__name__)


def create_meet(username: str, db: Session):
    join_code = generate_code(length=8)
    new_meet = Meet(join_code=join_code)
    new_user = Users(username=username)
    db.add_all([new_meet, new_user])
    db.commit()

    new_user_meet = MeetUser(meet_id=new_meet.id, user_id=new_user.id)
    db.add(new_user_meet)
    db.commit()
    return join_code
