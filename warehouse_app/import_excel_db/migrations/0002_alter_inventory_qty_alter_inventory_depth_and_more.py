# Generated by Django 4.2.4 on 2023-08-27 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_excel_db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='QTY',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='depth',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='length',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
