import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mybackend.settings')
django.setup()

from mybackend.models import Item

# Sample data
items = [
    {"name": "Item 1", "description": "Description for Item 1"},
    {"name": "Item 2", "description": "Description for Item 2"},
    {"name": "Item 3", "description": "Description for Item 3"},
]

# Load data into the database
for item in items:
    Item.objects.create(name=item['name'], description=item['description'])

print("Data loaded successfully!")
