# Generated by Django 4.0.5 on 2022-06-16 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageApp', '0003_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='image/'),
        ),
    ]
