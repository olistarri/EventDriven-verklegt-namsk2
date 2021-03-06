# Generated by Django 4.0.4 on 2022-05-27 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venue', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venue',
            old_name='accessible_seating',
            new_name='accessible_seats',
        ),
        migrations.RenameField(
            model_name='venue',
            old_name='seating',
            new_name='seats',
        ),
        migrations.AddField(
            model_name='venue',
            name='standing',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
