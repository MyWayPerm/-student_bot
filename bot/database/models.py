from datetime import datetime, date, timedelta
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from bot.config import DATABASE_URL

Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    title = Column(String)
    due_date = Column(Date)
    reminder_sent = Column(Boolean, default=False)

def init_db():
    Base.metadata.create_all(engine)

def add_new_task(user_id: int, title: str, due_date: datetime):
    session = Session()
    task = Task(user_id=user_id, title=title, due_date=due_date)
    session.add(task)
    session.commit()

def get_all_tasks(user_id: int):
    session = Session()
    return session.query(Task).filter(Task.user_id == user_id).all()

def get_tasks_for_reminder():
    session = Session()
    today = datetime.now().date()
    return session.query(Task).filter(
        Task.due_date == today + timedelta(days=1),
        Task.reminder_sent == False
    ).all()
