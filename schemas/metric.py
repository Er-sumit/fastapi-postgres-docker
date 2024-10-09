from pydantic import BaseModel
from pydantic import root_validator


class ListData(BaseModel):
    data: list


class SingleMetricValue(BaseModel):
    value: int


class DictMetric(BaseModel):
    data: dict


class AssetLiabilityRatio(BaseModel):
    value: str
    ratio: str
    assets_value: int
    liabilities_value: int
    metric_ratio: float
    metric_percent: float
