from fastapi import APIRouter, Depends
from configuration.config import DataAnalyticsService, ServerSettings


router = APIRouter()


def build_config():
    return DataAnalyticsService()


def fetch_config():
    return ServerSettings()


@router.get('/')
async def root(config: DataAnalyticsService = Depends(build_config),
               fconfig: ServerSettings = Depends(fetch_config)):
    return {'project_name': config.application,
            'webmaster': config.webmaster,
            'created': config.created,
            'development_server': fconfig.development_server,
            }
