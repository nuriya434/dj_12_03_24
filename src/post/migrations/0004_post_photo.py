# Generated by Django 4.0 on 2024-02-24 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_rename_lostik_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(null=True, upload_to='', verbose_name='..\\photo.jpg'),
        ),
    ]