from sqlalchemy import create_engine
import os
from sqlalchemy.orm import declarative_base,sessionmaker
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(url=os.environ['DATABASE_URL'],echo=True)
Base = declarative_base()
Session = sessionmaker()
