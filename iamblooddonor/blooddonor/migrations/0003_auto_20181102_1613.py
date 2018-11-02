# Generated by Django 2.1.2 on 2018-11-02 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blooddonor', '0002_auto_20181102_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectedorganization',
            name='organization_name',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='connectedorganization',
            name='join_as',
            field=models.CharField(choices=[('Sponsor', 'Sponsor'), ('Organization', 'Organization')], max_length=250),
        ),
    ]