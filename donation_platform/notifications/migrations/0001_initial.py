# Generated by Django 3.2.20 on 2023-11-01 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('noti_id', models.AutoField(primary_key=True, serialize=False)),
                ('noti_title', models.CharField(max_length=50)),
                ('noti_content', models.TextField()),
                ('noti_date', models.DateTimeField(blank=True, null=True)),
                ('was_read', models.BooleanField()),
            ],
            options={
                'db_table': 'notifications',
                'managed': False,
            },
        ),
    ]
