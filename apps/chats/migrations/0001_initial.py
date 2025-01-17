# Generated by Django 5.1.4 on 2025-01-12 01:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Integrantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.chat')),
            ],
        ),
    ]
