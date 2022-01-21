from fastapi import APIRouter
from backend.app.controllers import ready
from backend.app.controllers import meet

router_ready = APIRouter(prefix='/api')
router_ready.include_router(ready.ready_route, tags=['ready'])

router_meet = APIRouter(prefix='/meet')
router_meet.include_router(meet.meet_route, tags=['meet'])