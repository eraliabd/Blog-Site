# Generated by Django 4.0.6 on 2022-07-11 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='static/assets/images/'),
        ),
    ]
