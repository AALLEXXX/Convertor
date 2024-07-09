from typing import List

from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings
from core.models import ConversionRecord


class MongoDB:
    def __init__(self):
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(settings.MONGODB_URL)
        self.db = self.client[settings.MONGODB_DATABASE]
        self.collection_conversion_records = self.db["conversion_records"]

    async def insert_record(self, record: ConversionRecord):
        await self.collection_conversion_records.insert_one(record.dict())

    async def find_all_records(self) -> List[ConversionRecord]:
        records = []
        async for record_data in self.collection_conversion_records.find():
            record = ConversionRecord(
                date=record_data['date'],
                usd_amount=record_data['usd_amount']
            )
            records.append(record)
        return records

db = MongoDB()