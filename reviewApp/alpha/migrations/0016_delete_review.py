# Generated by Django 4.1.7 on 2023-04-05 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alpha', '0015_alter_product_date_released_alter_product_timestamp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]