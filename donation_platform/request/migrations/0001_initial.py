# Generated by Django 3.2.20 on 2023-09-23 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_name', models.CharField(max_length=50)),
                ('req_description', models.TextField()),
                ('accept_terms', models.BooleanField()),
                ('req_sent_date', models.DateTimeField()),
                ('has_confirmation', models.BooleanField()),
                ('confirmed_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'requests',
                'managed': False,
            },
        ),
    ]