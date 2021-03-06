# Generated by Django 2.2.7 on 2020-01-25 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='degree',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Id_No',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together={('name', 'state')},
        ),
        migrations.AlterUniqueTogether(
            name='company',
            unique_together={('name', 'country')},
        ),
        migrations.AlterUniqueTogether(
            name='department',
            unique_together={('name', 'company')},
        ),
        migrations.AlterUniqueTogether(
            name='state',
            unique_together={('name', 'country')},
        ),
    ]
