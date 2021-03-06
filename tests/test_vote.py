import unittest
from app.models import User, Comment,Category,Vote,Pitch,Role

class VoteModelTest(unittest.TestCase):
  def setUp(self):
    self.new_user=User(name="Agnes",password='password',role=Role.query.filter_by(name='User').first())
    self.new_pitch=Pitch(category=Category.query.filter_by(name='life').first(),user=self.new_user)
    self.new_vote=Vote(user=self.new_user,pitch=self.new_pitch,upvote=True)

  def tearDown(self):
    Vote.query.delete()
    Pitch.query.delete()
    User.query.delete()

  def test_instance_variables(self):
    self.assertEquals(self.new_vote.user,self.new_user)
    self.assertEquals(self.new_vote.pitch,self.new_pitch)
    self.assertEquals(self.new_vote.upvote,True)

  def test_save_vote(self):
    self.new_vote.save_vote()
    self.assertTrue(len(Vote.query.all())==1)