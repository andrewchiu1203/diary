# Generated by Django 4.1.3 on 2024-01-08 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_diary_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='body',
            field=models.CharField(max_length=100024),
        ),
    ]
