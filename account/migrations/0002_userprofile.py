# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=50, blank=True)),
                ('last_name', models.CharField(max_length=50, blank=True)),
                ('user_type', models.CharField(default=b'Normal User', max_length=50, blank=True, choices=[(b'Administrator', b'ADMINISTRATOR'), (b'Dispatcher Master', b'DISPATCHER MASTER'), (b'Marketing Master', b'MARKETING MASTER'), (b'Master', b'MASTER'), (b'Normal User', b'NORMAL USER'), (b'UI Master', b'UI MASTER')])),
                ('mobile_no', models.CharField(max_length=10, blank=True)),
                ('gender', models.CharField(blank=True, max_length=20, choices=[(b'Female', b'FEMALE'), (b'Male', b'MALE')])),
                ('dob', models.DateField(null=True, blank=True)),
                ('profile_picture', models.ImageField(null=True, upload_to=b'profile_picture/', blank=True)),
                ('profile_picture_icon', django_resized.forms.ResizedImageField(null=True, upload_to=b'profile_picture/', blank=True)),
                ('profile_picture_thumbnail', django_resized.forms.ResizedImageField(null=True, upload_to=b'profile_picture/', blank=True)),
                ('addresses', models.ManyToManyField(to='account.UserAddress')),
            ],
        ),
    ]
