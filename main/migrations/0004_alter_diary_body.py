# Generated by Django 4.1.3 on 2024-01-07 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_diary_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='body',
            field=models.TextField(),
        ),
    ]
