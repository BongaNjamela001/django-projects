# Generated by Django 4.1.2 on 2022-11-19 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('project', models.FileField(blank=True, null=True, upload_to='portfolio')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Bonga_Njamela_Resume')),
                ('resume', models.FileField(blank=True, null=True, upload_to='resume')),
            ],
            options={
                'verbose_name': 'Resume',
                'verbose_name_plural': 'Resumes',
            },
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contact Me'},
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='updated',
            new_name='timestamp',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='created',
        ),
        migrations.AddField(
            model_name='contact',
            name='isValid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='brief',
            field=models.TextField(blank=True, null=True, verbose_name='Brief Message'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=254, verbose_name='Email'),
        ),
    ]
