# Generated by Django 4.1.7 on 2023-03-21 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dreamstravel', '0006_subscribe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscribe',
            old_name='contact_email',
            new_name='subscribe_email',
        ),
        migrations.RenameField(
            model_name='subscribe',
            old_name='contact_id',
            new_name='subscribe_id',
        ),
    ]