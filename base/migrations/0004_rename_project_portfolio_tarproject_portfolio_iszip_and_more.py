# Generated by Django 4.1.2 on 2022-11-20 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_portfolio_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='project',
            new_name='tarproject',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='isZip',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='zipproject',
            field=models.FileField(blank=True, null=True, upload_to='portfolio'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
