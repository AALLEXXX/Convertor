from datetime import datetime

from pydantic import BaseModel, Field

class ConversionRecord(BaseModel):
    date: datetime = Field(..., description='date')
    usd_amount: float = Field(..., description='USD amount')

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "date": "2024-07-09T12:30:45Z",
                "usd_amount": 100.50
            }
        }

    def __repr__(self):
        return f"ConversionRecord(date={self.date}, usd_amount={self.usd_amount})"