# Generated by Django 2.2.5 on 2019-11-11 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191111_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='runtime',
            field=models.TextField(),
        ),
    ]
