from django.test import TestCase
# We need the models DB to run the tests
from .models import Item


# Create your tests here.
class TestViews(TestCase):

    def test_get_todo_list(self):
        # Signifies as if this page is directed to
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        # Signifies as if this page is directed to
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        item = Item.objects.create(name='Test todo_item')
        # Signifies as if this page is directed to
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_edit_item(self):
        item = Item.objects.create(name='Test todo_item')
        # Post as if we are actually on the form page
        response = self.client.post(f'/edit/{item.id}', {'name': 'updated name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'updated name')

    def test_can_add_item(self):
        response = self.client.post('/add', {'name': 'test add item'})
        self.assertRedirects(response, '/')
        existing_items = Item.objects.all()
        self.assertEqual(len(existing_items), 1)

    def test_can_delete_item(self):
        item = Item.objects.create(name='Test todo item')
        # Signifies as if this page is directed to
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item_done_field(self):
        item = Item.objects.create(name='Test todo item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

    def test_toggle_can_change_from_false_to_true(self):
        item = Item.objects.create(name='Test todo item')
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.done, True)
