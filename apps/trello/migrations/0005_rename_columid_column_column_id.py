# Generated by Django 4.2.7 on 2023-11-22 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trello', '0004_rename_id_column_columid_rename_id_task_task_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='column',
            old_name='columid',
            new_name='column_id',
        ),
    ]