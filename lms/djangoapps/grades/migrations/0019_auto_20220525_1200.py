# Generated by Django 3.2.13 on 2022-05-25 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0018_add_waffle_flag_defaults'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persistentgradesenabledflag',
            name='changed_by',
        ),
        migrations.DeleteModel(
            name='CoursePersistentGradesFlag',
        ),
        migrations.DeleteModel(
            name='PersistentGradesEnabledFlag',
        ),
    ]
