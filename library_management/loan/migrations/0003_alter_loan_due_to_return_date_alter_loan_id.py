# Generated by Django 5.0.6 on 2024-05-29 20:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_alter_loan_due_to_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='due_to_return_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 29, 2, 10, 56, 579860)),
        ),
        migrations.AlterField(
            model_name='loan',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
