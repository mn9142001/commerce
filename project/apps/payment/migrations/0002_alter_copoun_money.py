# Generated by Django 4.0.4 on 2022-04-27 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copoun',
            name='money',
            field=models.FloatField(),
        ),
    ]
