# Generated by Django 4.2.4 on 2023-08-28 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_excel_db', '0006_inventory_delete_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='QTY',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
