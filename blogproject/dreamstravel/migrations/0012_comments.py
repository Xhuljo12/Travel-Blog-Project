# Generated by Django 4.1.7 on 2023-03-24 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreamstravel', '0011_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_lines', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
