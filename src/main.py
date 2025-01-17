from fastapi import FastAPI
import uvicorn
from src.api.all_routers import all_routers

app = FastAPI(
    title="Библиотечный каталог"
)

for router in all_routers:
    app.include_router(router)






if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)
