from enum import Enum, IntEnum

from pydantic import BaseModel, conint, confloat


class SexEnum(Enum):
    M = 'M'
    F = 'F'


class ChesPainTypeEnum(Enum):
    TypicalAngina = 'TA'
    AtypicalAngina = 'ATA'
    NonAnginalPain = 'NAP'
    Asymptomatic = 'ASY'


class FastingBsEnum(IntEnum):
    T = 1
    F = 0


class RestingECGEnum(Enum):
    Normal = 'Normal'
    ST = 'ST'
    LVH = 'LVH'


class ExerciseAnginaEnum(Enum):
    Yes = 'Y'
    No = 'N'


class STSlopeEnum(Enum):
    Up = 'Up'
    Flat = 'Flat'
    Down = 'Down'


class Patient(BaseModel):
    age: conint(gt=0)
    sex: SexEnum
    chestPainType: ChesPainTypeEnum
    restingBP: confloat(ge=0.0)
    cholesterol: confloat(ge=0.0)
    fastingBS: FastingBsEnum
    restingECG: RestingECGEnum
    maxHR: conint(ge=60, le=202)
    exerciseAngina: ExerciseAnginaEnum
    oldpeak: float
    sTSlope: STSlopeEnum

    class Config:
        use_enum_values = True
