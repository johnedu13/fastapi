from fastapi import FastAPI
from routers.product import router as product_router

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hola":"Mundo"}

app.include_router(product_router)


