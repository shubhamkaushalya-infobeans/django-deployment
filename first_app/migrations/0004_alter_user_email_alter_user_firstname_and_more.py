# Generated by Django 4.1 on 2023-07-07 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('first_app', '0003_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='firstname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastname',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='UserProfileMoreInformationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_url', models.URLField(blank=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='first_app/profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
