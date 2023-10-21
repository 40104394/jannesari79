# Generated by Django 4.2.4 on 2023-08-30 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0003_alter_vendors_vendor_phone_number'),
        ('import_excel_db', '0013_alter_inventory_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='vendors.vendors'),
            preserve_default=False,
        ),
    ]
