# Generated by Django 2.2.27 on 2022-03-11 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('name', '0039_depopulate_constraintname_editor_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='constraintname',
            name='editor_label',
        ),
    ]
