# Generated by Django 5.0.1 on 2024-01-11 20:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_diary_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
