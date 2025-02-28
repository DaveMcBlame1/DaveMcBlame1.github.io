from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class BannedUser(Base):
    __tablename__ = 'banned_user'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)

# Replace 'sqlite:///your_database.db' with your actual database URL
engine = create_engine('sqlite:///bannedusers.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Example of adding a new banned user
new_user = BannedUser(username='test')
session.add(new_user)
session.commit()