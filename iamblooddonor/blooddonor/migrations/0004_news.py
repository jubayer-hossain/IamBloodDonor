# Generated by Django 2.1.2 on 2018-11-02 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blooddonor', '0003_auto_20181102_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('news_text', models.TextField()),
                ('created_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]