# Generated by Django 5.0.6 on 2024-06-26 14:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionapp', '0011_menaccessories_womenaccessories_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartmodel',
            name='aid',
        ),
        migrations.RemoveField(
            model_name='cartmodel',
            name='cid',
        ),
        migrations.AddField(
            model_name='cartmodel',
            name='clothe_child_cid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fashionapp.clothechild'),
        ),
        migrations.AddField(
            model_name='cartmodel',
            name='clothe_cid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fashionapp.clothe'),
        ),
        migrations.AddField(
            model_name='cartmodel',
            name='clothe_women_cid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fashionapp.clothewomen'),
        ),
        migrations.AddField(
            model_name='cartmodel',
            name='men_aid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fashionapp.menaccessories'),
        ),
        migrations.AddField(
            model_name='cartmodel',
            name='women_aid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fashionapp.womenaccessories'),
        ),
    ]
