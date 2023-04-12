# Generated by Django 4.1.7 on 2023-03-24 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dreamstravel', '0009_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_name', models.CharField(max_length=80)),
                ('comment_email', models.EmailField(max_length=254)),
                ('comment_body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='dreamstravel.articles')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]