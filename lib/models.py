from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    reviews = relationship("Review", back_populates="game")

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    game_id = Column(Integer, ForeignKey('games.id'))
    game = relationship("Game", back_populates="reviews")

# Create a new SQLite database (or connect to an existing one)
engine = create_engine('sqlite:///games.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
