# Generated by Django 4.1.3 on 2022-11-07 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='static/posts/'),
        ),
    ]
