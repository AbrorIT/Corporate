# Generated by Django 3.2.7 on 2022-03-05 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_partners_link_partner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='team/')),
                ('position', models.CharField(max_length=50)),
                ('facebook', models.CharField(max_length=255)),
                ('twitter', models.CharField(max_length=255)),
                ('linkedin', models.CharField(max_length=255)),
                ('instagram', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команды',
            },
        ),
    ]