# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0003_auto_20160516_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='quotation_no',
            field=models.IntegerField(),
        ),
    ]
