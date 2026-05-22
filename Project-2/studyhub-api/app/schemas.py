from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: str = Field(
        ...,
        min_length=3,
        max_length=100
    )
    completed: bool = False


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: int

class SessionBase(BaseModel):
    subject: str = Field(
        ...,
        min_length=2,
        max_length=50
    )
    duration: int = Field(
        ...,
        gt=0
    )

class SessionCreate(SessionBase):
    pass


class SessionResponse(SessionBase):
    id: int


class ProgressResponse(BaseModel):
    total_tasks: int
    completed_tasks: int
    pending_tasks: int
    total_sessions: int
    total_study_minutes: int
    total_study_hours: float