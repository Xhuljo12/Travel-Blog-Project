# Generated by Django 4.1.7 on 2023-03-21 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreamstravel', '0005_articles_articles_lines'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
