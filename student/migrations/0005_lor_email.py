# Generated by Django 3.0.3 on 2020-04-08 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20200408_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='lor',
            name='email',
            field=models.CharField(default='samyakjainbvs@gmail.com', max_length=200),
        ),
    ]
