# Generated by Django 5.0.2 on 2024-02-10 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list_app', '0002_remove_task_created_task_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
