# Generated by Django 3.2.20 on 2023-11-11 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_attachments_attachmentsevent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attachments',
        ),
        migrations.DeleteModel(
            name='AttachmentsEvent',
        ),
    ]
