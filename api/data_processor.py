from fastapi import APIRouter, Depends
from configuration.config import DataProcessingService, ServerSettings


router = APIRouter()


def build_config():
    return DataProcessingService()


def fetch_config():
    return ServerSettings()


@router.get('/')
async def root(config: DataProcessingService = Depends(build_config),
               fconfig: ServerSettings = Depends(fetch_config)):
    return {'project_name': config.application,
            'webmaster': config.webmaster,
            'created': config.created,
            'development_server': fconfig.development_server,
            }
