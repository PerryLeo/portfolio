# Generated by Django 2.0.2 on 2019-03-22 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20190321_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default='default.png', upload_to='media/image/'),
        ),
    ]
