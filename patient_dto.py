from enum import Enum

from pydantic import BaseModel


class Patient(BaseModel):
    age: int
    sex: str
    chestPainType: str
    restingBP: int
    cholesterol: int
    fastingBS: int
    restingECG: str
    maxHR: int
    exerciseAngina: str
    oldpeak: float
    sTSlope: str

    class Config:
        use_enum_values = True
