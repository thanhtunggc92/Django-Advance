# Generated by Django 4.1.2 on 2022-10-28 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_books_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
    ]
