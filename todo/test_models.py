from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test to do item')
        self.assertFalse(item.done)

    def test_item_string_returns_name(self):
        item = Item.objects.create(name='Test to do item')
        self.assertAlmostEqual(str(item), 'Test to do item')
