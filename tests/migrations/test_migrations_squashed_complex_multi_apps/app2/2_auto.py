# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("app2", "1_auto")]

    operations = [
        migrations.RunPython(lambda apps, schema_editor: None)
    ]
