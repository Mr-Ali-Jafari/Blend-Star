# Generated by Django 5.0.7 on 2024-07-14 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile/pictures/'),
        ),
    ]
