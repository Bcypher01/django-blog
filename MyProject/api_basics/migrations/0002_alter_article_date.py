# Generated by Django 3.2.7 on 2022-08-22 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
