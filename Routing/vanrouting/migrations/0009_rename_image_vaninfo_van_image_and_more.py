# Generated by Django 4.1.7 on 2023-04-06 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vanrouting', '0008_institutes_details_remove_vaninfo_institute_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vaninfo',
            old_name='image',
            new_name='van_image',
        ),
        migrations.RenameField(
            model_name='vaninfo',
            old_name='slug',
            new_name='van_slug',
        ),
        migrations.AddField(
            model_name='institutes_details',
            name='institute_id',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institutes_details',
            name='institute_slug',
            field=models.SlugField(default=2, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vaninfo',
            name='available_seats',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vaninfo',
            name='total_seats',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vaninfo',
            name='van_id',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]