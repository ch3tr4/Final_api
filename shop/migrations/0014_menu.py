# Generated by Django 5.1.4 on 2025-07-26 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_delete_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MenuNameEN', models.CharField(max_length=200, null=True)),
                ('OrderBy', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
