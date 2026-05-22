from fastapi import FastAPI
from app.routes.tasks import router as task_router, tasks
from app.routes.sessions import router as session_router, sessions
from app.schemas import ProgressResponse

app = FastAPI(
    title="StudyHub API",
    description="Backend API for managing tasks, study sessions, and progress tracking.",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message":"StudyHub API is running"}

@app.get("/progress", response_model=ProgressResponse, tags=["Progress"])
def get_progress():
    total_tasks = len(tasks)

    completed_tasks = sum(
        1 for task in tasks
        if task["completed"]
    )

    pending_tasks = (
        total_tasks - completed_tasks
    )

    total_sessions = len(sessions)

    total_study_minutes = sum(
        session["duration"]
        for session in sessions
    )

    total_study_hours = round(
        total_study_minutes / 60, 
        2
    )

    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "total_sessions": total_sessions,
        "total_study_minutes": total_study_minutes,
        "total_study_hours": total_study_hours
    }

@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "healthy",
        "message": "StudyHub API is running"
    }

app.include_router(task_router)
app.include_router(session_router)

