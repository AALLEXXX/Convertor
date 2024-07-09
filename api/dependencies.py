from core.db import db
from services.convertor import ConvertorService
def get_convertor_service():
    return ConvertorService(db)