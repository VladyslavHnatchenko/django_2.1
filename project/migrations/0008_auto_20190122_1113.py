# Generated by Django 2.1.5 on 2019-01-22 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20190122_1044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelTable(
            name='student',
            table='student_info',
        ),
    ]
