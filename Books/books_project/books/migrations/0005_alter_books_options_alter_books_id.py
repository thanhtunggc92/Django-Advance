# Generated by Django 4.1.2 on 2022-11-03 23:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_books_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={},
        ),
        migrations.AlterField(
            model_name='books',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
