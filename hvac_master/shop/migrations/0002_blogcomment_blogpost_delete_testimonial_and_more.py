# Generated by Django 5.2.3 on 2025-07-01 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='shop.blogcomment')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('author_image', models.ImageField(blank=True, null=True, upload_to='blog/authors/')),
                ('date', models.DateField()),
                ('content', models.TextField()),
                ('hero_image', models.ImageField(blank=True, null=True, upload_to='blog/hero/')),
                ('hero_label', models.CharField(blank=True, max_length=100, null=True)),
                ('hero_avatar', models.ImageField(blank=True, null=True, upload_to='blog/hero/avatar/')),
                ('quote', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Testimonial',
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='shop.blogpost'),
        ),
    ]
