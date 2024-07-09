import httpx
from fastapi import HTTPException
from datetime import  datetime
from core.config import settings
from core.db import MongoDB
from core.models import ConversionRecord
from schemas.convertor import ConvertUSDArg


class ConvertorService:
    def __init__(self, db):
        self.db: MongoDB = db

    async def convert_usd(self, convert_data : ConvertUSDArg) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://v6.exchangerate-api.com/v6/{settings.EXCHANGERATE_API_KEY}/latest/USD")

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error fetching exchange rates")

        exchangerate_api_data: dict = response.json().get("conversion_rates")

        for currency, rate  in exchangerate_api_data.items():
            exchangerate_api_data.update({currency: round(rate * convert_data.dollars, 2)})

        exchangerate_api_data.pop("USD")

        new_log = ConversionRecord(date=datetime.now(), usd_amount=convert_data.dollars)
        await self.db.insert_record(new_log)

        print(await self.db.find_all_records()) #проверяем добавилась ли запись

        return exchangerate_api_data
