# Generated by Django 3.2 on 2022-12-20 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0033_tour_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='is_featured',
            field=models.BooleanField(null=True),
        ),
    ]