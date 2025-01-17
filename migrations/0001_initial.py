# Generated by Django 5.1 on 2024-10-27 15:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_at', models.DateTimeField(auto_now_add=True)),
                ('id_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.book')),
            ],
            options={
                'ordering': ['-read_at'],
            },
        ),
    ]
