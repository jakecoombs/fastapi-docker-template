from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Setting up the database connection and session
engine = create_engine("postgresql+psycopg2://postgres:password@db:5432/sample_db")
SessionLocal = scoped_session(sessionmaker(bind=engine))
