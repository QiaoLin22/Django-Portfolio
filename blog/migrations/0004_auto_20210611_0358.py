# Generated by Django 3.2.3 on 2021-06-11 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_name',
            field=models.CharField(max_length=120),
        ),
    ]
