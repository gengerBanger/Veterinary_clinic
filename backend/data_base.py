from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

URL = "postgresql://aleks:password@localhost/clinic"

engine = create_engine(URL)

SessionLocal = sessionmaker(bind=engine,
                       autoflush=False,
                       autocommit=False)

Base = declarative_base()
