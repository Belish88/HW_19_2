# Generated by Django 4.2.6 on 2023-11-20 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(default='3305966304712765', max_length=100, verbose_name='token'),
        ),
    ]
