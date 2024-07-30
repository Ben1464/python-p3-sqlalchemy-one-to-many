import unittest
from lib.models import Game, Review, Base, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

class TestReview(unittest.TestCase):
    def setUp(self):
        Base.metadata.create_all(engine)
        self.session = Session()

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(engine)

    def test_create_review(self):
        game = Game(title="Game Title")
        self.session.add(game)
        self.session.commit()

        review = Review(content="Great game!", game_id=game.id)
        self.session.add(review)
        self.session.commit()

        reviews = self.session.query(Review).all()
        self.assertEqual(len(reviews), 1)
        self.assertEqual(reviews[0].content, "Great game!")
        self.assertEqual(reviews[0].game.title, "Game Title")

if __name__ == '__main__':
    unittest.main()
