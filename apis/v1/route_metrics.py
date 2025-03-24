from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status as fstatus
from sqlalchemy.orm import Session

from business.compute_metrics import liabilities_near_qtr
from business.compute_metrics import total_assets
from business.compute_metrics import total_liabilities
from business.compute_metrics import total_cash

from core.config import log
from db.session import get_db
from schemas.metric import AssetLiabilityRatio
from schemas.metric import DictMetric
from schemas.metric import SingleMetricValue

router = APIRouter()


@router.get("/metric/assets", response_model=SingleMetricValue)
def get_assets_value(db: Session = Depends(get_db)):
    value = total_assets(db)
    if not value:
        value = 0
    return {"value": value}


@router.get("/metric/liabilities", response_model=SingleMetricValue)
def get_liabilities_value(db: Session = Depends(get_db)):
    value = total_liabilities(db)
    if not value:
        value = 0
    return {"value": value}


@router.get("/metric/asset_liabilities_ratio", response_model=AssetLiabilityRatio)
def get_asset_liability_ratio(db: Session = Depends(get_db)):
    assets = total_assets(db) if total_assets(db) else 0
    liabilities = total_liabilities(db) if total_liabilities(db) else 0
    value = (assets / liabilities).as_integer_ratio()
    ratio_value = f"{value[0]}:{value[1]}"
    return {
        "value": f"{int(assets/1000)} / {int(liabilities/1000)}",
        "ratio": ratio_value,
        "liabilities_value": liabilities,
        "assets_value": assets,
        "metric_ratio": round((assets / liabilities), 2),
        "metric_percent": round((assets / liabilities * 100), 2),
    }


@router.get("/metric/liabilities/qtly", response_model=DictMetric)
def get_qtly_liability_metrics(db: Session = Depends(get_db)):
    data = liabilities_near_qtr(db)
    log.info(data)
    return {"data": data}


@router.get("/metric/liabilities/qtlys")
def flake8_handler_():
    raise HTTPException(status_code=fstatus.HTTP_200_OK)

@router.get("/metric/total_cash", response_model=SingleMetricValue)
def get_total_cash(db: Session = Depends(get_db)):
    value = total_cash(db)
    return {"value": value}