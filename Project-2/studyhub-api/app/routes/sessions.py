from fastapi import APIRouter, status
from app.schemas import SessionCreate, SessionResponse

router = APIRouter(
    prefix="/sessions",
    tags=["Sessions"]
)

sessions = []
next_session_id = 1


# GET all sessions
@router.get("/", response_model=list[SessionResponse], status_code=status.HTTP_200_OK)
def get_sessions():
    return sessions


# POST new session
@router.post("/", response_model=SessionResponse, status_code=status.HTTP_201_CREATED)
def create_session(session: SessionCreate):
    global next_session_id

    new_session = {
        "id": next_session_id,
        "subject": session.subject,
        "duration": session.duration
    }

    sessions.append(new_session)
    next_session_id += 1

    return new_session