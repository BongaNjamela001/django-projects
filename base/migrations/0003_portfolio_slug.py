# Generated by Django 4.1.2 on 2022-11-19 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_portfolio_resume_alter_contact_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]