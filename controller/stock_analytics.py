from fastapi import APIRouter

router = APIRouter()


@router.get('/stock-analytics/{platform_id}')
def access_portal(platform_id: int):
    return {'message': 'Stock Analytics Platform'}
