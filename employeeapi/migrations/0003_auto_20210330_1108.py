# Generated by Django 3.1.7 on 2021-03-30 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapi', '0002_auto_20210330_1052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='name',
            new_name='username',
        ),
    ]
