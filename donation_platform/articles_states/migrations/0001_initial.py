# Generated by Django 3.2.20 on 2023-11-01 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlesStates',
            fields=[
                ('state_id', models.AutoField(primary_key=True, serialize=False)),
                ('state_name', models.TextField()),
            ],
            options={
                'db_table': 'articles_states',
                'managed': False,
            },
        ),
    ]
