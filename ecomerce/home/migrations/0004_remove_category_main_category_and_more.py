# Generated by Django 5.1.4 on 2024-12-31 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_banner_area_slider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='Main_category',
        ),
        migrations.RemoveField(
            model_name='sub_category',
            name='category',
        ),
        migrations.AlterField(
            model_name='slider',
            name='deal',
            field=models.CharField(choices=[('New Deal', 'New Deal'), ('Hot Deal', 'Hot Deal'), ('New arrival', 'New arrival'), ('Best seller', 'Best seller')], default='', max_length=200),
        ),
        migrations.DeleteModel(
            name='Main_Category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Sub_Category',
        ),
    ]
