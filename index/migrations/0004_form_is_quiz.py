# Generated by Django 4.0 on 2022-01-14 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_remove_form_see_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='is_quiz',
            field=models.BooleanField(default=False),
        ),
    ]
