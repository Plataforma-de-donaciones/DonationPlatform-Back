# Generated by Django 3.2.20 on 2023-10-26 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('cat_name', models.TextField()),
            ],
            options={
                'db_table': 'categories',
                'managed': False,
            },
        ),
    ]