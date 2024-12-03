from fastapi import APIRouter

from . import reportes_view

API_PREFIX = "/api"
router = APIRouter()

router.include_router(reportes_view.router, prefix="/reportes")