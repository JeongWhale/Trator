# Generated by Django 3.2.4 on 2021-07-27 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_remove_account_phone_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
    ]
