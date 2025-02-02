# Generated by Django 3.0.1 on 2020-01-26 04:57

import chatterbot.conversation
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('search_text', models.CharField(blank=True, max_length=255)),
                ('conversation', models.CharField(max_length=32)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time that the statement was created at.')),
                ('in_response_to', models.CharField(max_length=255, null=True)),
                ('search_in_response_to', models.CharField(blank=True, max_length=255)),
                ('persona', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'statement',
            },
            bases=(models.Model, chatterbot.conversation.StatementMixin),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(unique=True)),
            ],
            options={
                'db_table': 'tag',
            },
        ),
    
    ]
