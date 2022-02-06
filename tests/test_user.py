import unittest
from app.models import User, Comments, Pitches


class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password='@liammyfirst1')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('@liammyfirst1'))


class CommentsModelTest(unittest.TestCase):

    def setUp(self):
        self.new_comment = Comments(id=1, user_id=2, comment='cross buns', pitches_id='5', date_posted='2022-02-06')

    def test_comment_variables(self):
        # self.assertEquals(self.new_comment.id, 2)
        self.assertEquals(self.new_comment.comment, 'cross buns')
        self.assertEquals(self.new_comment.date_posted, '2022-02-06')
        self.assertEquals(self.new_comment.user_id, 2)
        # self.assertEquals(self.new_comment.pitches_id, 4)

    def test_save_comment(self):
        self.assertTrue(len(Comments.query.all()) > 0)


class PitchesModelTest(unittest.TestCase):

    def test_save_pitch(self):
        self.assertTrue(len(Pitches.query.all()) > 0)