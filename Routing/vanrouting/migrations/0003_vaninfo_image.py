# Generated by Django 4.1.7 on 2023-04-04 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vanrouting', '0002_vaninfo_institute_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaninfo',
            name='image',
            field=models.ImageField(default='u', upload_to='images'),
            preserve_default=False,
        ),
    ]
