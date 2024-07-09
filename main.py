from fastapi import FastAPI, HTTPException
from api.convertor import convertor_router
from core.db import db

app = FastAPI()

app.include_router(convertor_router)


@app.on_event("startup")
def startup_db_client():
    mongodb_client = db.client
    try:
        mongodb_client.server_info()
        print("Connected to MongoDB!")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to connect to MongoDB: {str(e)}")


@app.on_event("shutdown")
def shutdown_db_client():
    db.client.close()
