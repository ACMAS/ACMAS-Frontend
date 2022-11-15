from django.test import TestCase
from app.models import Post


class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title="Title", description="Blurb", wiki="Post")
        self.assertEqual(post.title, "Title")
        self.assertEqual(post.description, "Blurb")
        self.assertEqual(post.wiki, "Post")