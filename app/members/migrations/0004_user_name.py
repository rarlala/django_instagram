# Generated by Django 2.2.9 on 2020-01-07 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_remove_user_img_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
