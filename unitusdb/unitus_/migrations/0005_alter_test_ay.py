# Generated by Django 4.2.4 on 2023-08-05 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unitus_', '0004_macroaree_test_id_test_alter_availability_id_test_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='ay',
            field=models.IntegerField(),
        ),
    ]
