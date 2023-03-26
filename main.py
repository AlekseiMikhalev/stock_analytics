from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from loguru import logger
from uuid import uuid4

from api.data_fetcher import router as data_fetching_router
from api.data_analyst import router as data_analytics_router
from api.data_processor import router as data_processing_router

tags_metadata = [
    {
        "name": "Stock Analytics Platform",
        "description": "Platform that make stock data analysis and price prediction"
    },
    {
        "name": "Data Fetching Service",
        "description": "Collecting data about stock from vaious resources.",
    },
    {
        "name": "Data Processing Service",
        "description": "Processing raw data by cleaning and formatting for analysis",
    },
    {
        "name": "Data Analysis Service",
        "description": "Analyse, find pattern and insights from stock data",
    },
]

app = FastAPI(title='Stock Analytics Platform', openapi_tags=tags_metadata)

logger.add('logs/info.log', format='Log: [{extra[log_id]}: {time} - {level} - {message}', level='INFO',
           colorize=True, enqueue=True)
logger.add('logs/debug.log', format='Log: [{extra[log_id]}: {time} - {level} - {message}', level='DEBUG',
           colorize=True, enqueue=True)
logger.add('logs/trace.log', format='Log: [{extra[log_id]}: {time} - {level} - {message}', level='TRACE',
           colorize=True, enqueue=True)
logger.add('logs/error.log', format='Log: [{extra[log_id]}: {time} - {level} - {message}', level='ERROR',
           colorize=True, enqueue=True)


app.include_router(data_fetching_router,
                   prefix='/data-fetching', tags=['Data Fetching Service'])
app.include_router(data_processing_router,
                   prefix='/data-processing', tags=['Data Processing Service'])
app.include_router(data_analytics_router,
                   prefix='/data-analytics', tags=['Data Analysis Service'])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware('http')
async def log_middleware(request: Request, call_next):
    log_id = str(uuid4())
    with logger.contextualize(log_id=log_id):
        logger.info('Request to access ' + request.url.path)
        try:
            response = await call_next(request)
        except Exception as ex:
            logger.error(f'Request to ' + request.url.path + ' failed: {ex}')
            response = JSONResponse(
                content={'success': False}, status_code=500)
        finally:
            logger.info('Successfully accessed ' + request.url.path)
            return response


@app.get('/', tags=['Stock Analytics Platform'])
def access_platform():
    return {'message': 'Stock Analytics Platform'}
