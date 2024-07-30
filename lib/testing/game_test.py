import unittest
from lib.models import Game, Base, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

class TestGame(unittest.TestCase):
    def setUp(self):
        Base.metadata.create_all(engine)
        self.session = Session()

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(engine)

    def test_create_game(self):
        # Ensure no invalid arguments are used
        game = Game(title="Game Title")
        self.session.add(game)
        self.session.commit()

        games = self.session.query(Game).all()
        self.assertEqual(len(games), 1)
        self.assertEqual(games[0].title, "Game Title")

if __name__ == '__main__':
    unittest.main()
