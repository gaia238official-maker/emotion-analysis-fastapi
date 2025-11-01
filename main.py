from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from pydantic import BaseModel

# SQLite database URL
DATABASE_URL = "sqlite:///./emotions.db"

# Create the database engine
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

# SQLAlchemy model for Emotion records
class Emotion(Base):
    __tablename__ = "emotions"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    label = Column(String, nullable=True)

# Create tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI(title="Emotion Analysis API")

# Pydantic model for request body
class EmotionCreate(BaseModel):
    text: str
    label: str | None = None

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to create a new emotion record
@app.post("/emotions/")
def create_emotion(emotion: EmotionCreate, db: Session = Depends(get_db)):
    db_emotion = Emotion(text=emotion.text, label=emotion.label)
    db.add(db_emotion)
    db.commit()
    db.refresh(db_emotion)
    return db_emotion

# Endpoint to retrieve all emotion records
@app.get("/emotions/")
def read_emotions(db: Session = Depends(get_db)):
    emotions = db.query(Emotion).all()
    return emotions
