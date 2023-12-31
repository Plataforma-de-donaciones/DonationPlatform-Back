# Generated by Django 3.2.20 on 2023-11-01 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moderator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('moderator_state', models.IntegerField()),
                ('erased_at', models.DateTimeField(blank=True, null=True)),
                ('erased_reason', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'moderator',
                'managed': False,
            },
        ),
    ]
