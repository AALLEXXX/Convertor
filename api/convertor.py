from typing import Dict

from fastapi import APIRouter
from fastapi import Depends

from api.dependencies import get_convertor_service
from schemas.convertor import ConvertUSDArg
from services.convertor import ConvertorService

convertor_router = APIRouter(
    prefix="/convertor",
    tags=["convertor"],
)

@convertor_router.get("/USD")
async def convert_usd(convert_data : ConvertUSDArg = Depends(),
                      ConvertorService: ConvertorService = Depends(get_convertor_service)) -> Dict[str, float]:
    return await ConvertorService.convert_usd(convert_data)
