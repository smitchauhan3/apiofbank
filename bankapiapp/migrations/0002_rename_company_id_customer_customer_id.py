# Generated by Django 4.2.3 on 2023-10-21 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapiapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='company_id',
            new_name='customer_id',
        ),
    ]
