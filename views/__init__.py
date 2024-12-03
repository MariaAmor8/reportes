from fastapi import APIRouter

from views import reportes_view

API_PREFIX = "/api"
router = APIRouter()

router.include_router(reportes_view.router, prefix="/reportes")