# Generated by Django 4.2.7 on 2023-11-22 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=255)),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='trello.column')),
            ],
        ),
    ]
