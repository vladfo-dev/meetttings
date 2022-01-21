from fastapi import APIRouter
from backend.app.controllers import ready

router_ready = APIRouter(prefix='/api')
router_ready.include_router(ready.ready_route, tags=['ready'])