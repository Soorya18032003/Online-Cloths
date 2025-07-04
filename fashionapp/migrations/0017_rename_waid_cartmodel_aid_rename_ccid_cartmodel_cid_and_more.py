# Generated by Django 5.0.4 on 2024-07-16 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fashionapp', '0016_remove_cartmodel_clothe_id_cartmodel_clothe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartmodel',
            old_name='waid',
            new_name='aid',
        ),
        migrations.RenameField(
            model_name='cartmodel',
            old_name='ccid',
            new_name='cid',
        ),
        migrations.RenameField(
            model_name='clothechild',
            old_name='ccid',
            new_name='cid',
        ),
        migrations.RenameField(
            model_name='clothewomen',
            old_name='cwid',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='menaccessories',
            old_name='maid',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='womenaccessories',
            old_name='waid',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='cartmodel',
            name='clothe',
        ),
        migrations.RemoveField(
            model_name='cartmodel',
            name='cwid',
        ),
        migrations.RemoveField(
            model_name='cartmodel',
            name='maid',
        ),
    ]
