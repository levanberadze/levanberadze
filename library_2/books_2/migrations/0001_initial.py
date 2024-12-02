# Generated by Django 5.1.3 on 2024-12-02 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('detective', 'Detective'), ('comedy', 'Comedy'), ('adventure', 'Adventure'), ('drama', 'Drama')], max_length=100)),
            ],
        ),
    ]
