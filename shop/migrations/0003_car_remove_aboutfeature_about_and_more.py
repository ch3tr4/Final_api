# Generated by Django 5.2.3 on 2025-07-11 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_blogcomment_blogpost_delete_testimonial_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(max_length=200, null=True)),
                ('vin', models.CharField(max_length=200, null=True)),
                ('originalPrice', models.CharField(max_length=200, null=True)),
                ('price', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('year', models.CharField(max_length=200, null=True)),
                ('mile', models.CharField(max_length=200, null=True)),
                ('tranmission', models.CharField(max_length=200, null=True)),
                ('housepw', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='aboutfeature',
            name='about',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='post',
        ),
        migrations.DeleteModel(
            name='TeamMember',
        ),
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='AboutFeature',
        ),
        migrations.DeleteModel(
            name='BlogComment',
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
