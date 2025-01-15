import logging.config

from fastapi import FastAPI
import uvicorn
from src.api.all_routers import all_routers
from src.settings.logging.logging_settings import logging_config

app = FastAPI(
    title="Библиотечный каталог"
)

for router in all_routers:
    app.include_router(router)



# logging.config.dictConfig(logging_config)

if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)
