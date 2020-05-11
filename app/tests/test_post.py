import unittest
from app.models import Post,Comment


class PostTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''

        self.user_Sophy = User(username = 'Sophy', password = 'potato', email = 'kevo@ms.com')
        self.new_comment = Comment(comment = 'Awesome stuff', post_id = 12345, user_id=self.user_Sophy)
        self.new_post = Post(id=12345,post_title="First Post", post='Awesome post for stuff',category='Interview Post')

    def tearDown(self):
        Post.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.id,12345)
        self.assertEquals(self.new_post.post_title,'First ')
        self.assertEquals(self.new_post.post,' post for stuff')
        self.assertEquals(self.new_post.category,"Interview ")

    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all())>0)

    def test_get_post_by_id(self):

        self.new_post.save_post()
        got_posts = Post.get_post(12345)
        self.assertTrue(len(got_posts) == 1)