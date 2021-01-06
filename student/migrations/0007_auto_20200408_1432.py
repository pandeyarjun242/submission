# Generated by Django 3.0.3 on 2020-04-08 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0006_lor_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('subject', models.CharField(max_length=50)),
                ('transcripts', models.FileField(upload_to='sat2/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='sat',
            name='user',
        ),
        migrations.RemoveField(
            model_name='subjecttest',
            name='user',
        ),
        migrations.DeleteModel(
            name='ACT',
        ),
        migrations.DeleteModel(
            name='SAT',
        ),
        migrations.DeleteModel(
            name='SubjectTest',
        ),
    ]
