# Generated by Django 5.2.4 on 2025-07-20 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_contactinfo_logo_phonenumber_sociallink_widget'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactInfo',
        ),
        migrations.DeleteModel(
            name='Logo',
        ),
        migrations.DeleteModel(
            name='PhoneNumber',
        ),
        migrations.DeleteModel(
            name='SocialLink',
        ),
        migrations.DeleteModel(
            name='Widget',
        ),
    ]
