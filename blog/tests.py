from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser",
            password="testpassword123",
        )
        cls.post = Post.objects.create(
            title="Hello, World!",
            author=cls.user,
            body="This is a test post.",
        )

    def test_post_createview(self):
        response = self.client.post(
            reverse("post_new"),
            {
                "title": "New title",
                "body": "New text",
                "author": self.user.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New title")
        self.assertEqual(Post.objects.last().body, "New text")

    def test_post_updateview(self):
        response = self.client.post(
            reverse("post_edit", args=[self.post.pk]),
            {
                "title": "Updated title",
                "body": "Updated text",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, "Updated title")
        self.assertEqual(self.post.body, "Updated text")

    def test_post_deleteview(self):
        response = self.client.post(
            reverse("post_delete", args=[self.post.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())
