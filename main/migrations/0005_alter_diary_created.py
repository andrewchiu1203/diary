# Generated by Django 4.1.3 on 2024-01-07 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_diary_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
