from django.test import TestCase
from django.urls import reverse
from .models import Post
class UpdatePostTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='Заголовок', description='описание')

    def test_update_post(self):
        self.post.title = 'Обновленный заголовок'
        self.post.description = 'Обновленная описание'
        self.post.save()
        updated_post = Post.objects.get(id=self.post.id)
        self.assertEqual(updated_post.title, 'Обновленный заголовок')
        self.assertEqual(updated_post.description, 'Обновленная описание')

class PostModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='Заголовок', description='описание')

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Заголовок')
        self.assertEqual(self.post.description, 'описание')


class DeletePostTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='Заголовок', description='описание')

    def test_delete_post(self):
        self.post.delete()
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())