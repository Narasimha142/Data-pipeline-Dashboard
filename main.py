from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel
import random
import datetime

app = FastAPI()

# Allow CORS from localhost:3000 (React dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class PipelineJob(BaseModel):
    id: int
    name: str
    status: str
    last_run: str
    duration_sec: int

def generate_jobs() -> List[PipelineJob]:
    statuses = ["Success", "Running", "Failed", "Queued"]
    jobs = []
    for i in range(1, 6):
        status = random.choice(statuses)
        last_run = (datetime.datetime.now() - datetime.timedelta(minutes=random.randint(1, 120))).strftime("%Y-%m-%d %H:%M:%S")
        duration = random.randint(30, 600)
        jobs.append(PipelineJob(id=i, name=f"Job-{i}", status=status, last_run=last_run, duration_sec=duration))
    return jobs

@app.get("/api/jobs", response_model=List[PipelineJob])
async def get_jobs():
    return generate_jobs()
