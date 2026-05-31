from fastapi import APIRouter

from fastapi.responses import Response

from app.monitoring.metrics import (
    get_metrics
)

router = APIRouter()


@router.get("/metrics")

def metrics():

    return Response(
        content=get_metrics(),
        media_type="text/plain"
    )