# Generated by Django 4.2.6 on 2023-11-08 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(default='5778327143926261', max_length=100, verbose_name='token'),
        ),
    ]
