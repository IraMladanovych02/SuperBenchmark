import os

from typing import List
from datetime import datetime
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session


from db.engine import SessionLocal, engine
from db.models import Base, BenchmarkingResult
from serializers import BenchmarkingResultSerializer, AverageStatisticsSerializer
from utils.data_loader import load_json_data

app = FastAPI()

DEBUG = os.getenv("SUPERBENCHMARK_DEBUG", "True").lower() == "true"
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


test_data = load_json_data("superbenchmark_db_data.json") if DEBUG else None


@app.get("/results/average", response_model=AverageStatisticsSerializer)
def get_average_results(db: Session = Depends(get_db)):
    """Повертає середню статистику для всіх записів."""
    results = (
        test_data["benchmarking_results"]
        if DEBUG
        else db.query(BenchmarkingResult).all()
    )

    if not results:
        return {
            "average_token_count": 0,
            "average_time_to_first_token": 0,
            "average_time_per_output_token": 0,
            "average_total_generation_time": 0,
        }

    averages = {
        "average_token_count": sum(r["token_count"] for r in results) / len(results),
        "average_time_to_first_token": sum(r["time_to_first_token"] for r in results)
        / len(results),
        "average_time_per_output_token": sum(
            r["time_per_output_token"] for r in results
        )
        / len(results),
        "average_total_generation_time": sum(
            r["total_generation_time"] for r in results
        )
        / len(results),
    }
    return averages


@app.get(
    "/results/average/{start_time}/{end_time}",
    response_model=AverageStatisticsSerializer,
)
def get_average_results_in_time_range(
    start_time: str, end_time: str, db: Session = Depends(get_db)
):
    start = datetime.fromisoformat(start_time)
    end = datetime.fromisoformat(end_time)

    results = (
        [
            r
            for r in test_data["benchmarking_results"]
            if start <= datetime.fromisoformat(r["timestamp"]) <= end
        ]
        if DEBUG
        else db.query(BenchmarkingResult)
        .filter(
            BenchmarkingResult.timestamp >= start, BenchmarkingResult.timestamp <= end
        )
        .all()
    )

    if not results:
        return {
            "average_token_count": 0,
            "average_time_to_first_token": 0,
            "average_time_per_output_token": 0,
            "average_total_generation_time": 0,
        }

    averages = {
        "average_token_count": sum(r["token_count"] for r in results) / len(results),
        "average_time_to_first_token": sum(r["time_to_first_token"] for r in results)
        / len(results),
        "average_time_per_output_token": sum(
            r["time_per_output_token"] for r in results
        )
        / len(results),
        "average_total_generation_time": sum(
            r["total_generation_time"] for r in results
        )
        / len(results),
    }
    return averages
