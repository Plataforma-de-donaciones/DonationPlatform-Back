# Generated by Django 3.2.20 on 2023-11-01 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('mess_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('sent_date', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'message',
                'managed': False,
            },
        ),
    ]
