# Generated by Django 4.2.2 on 2023-06-22 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='nick_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]