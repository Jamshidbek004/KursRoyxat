# Generated by Django 4.2.3 on 2024-08-22 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Royxat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=200)),
                ('familya', models.CharField(max_length=200)),
                ('yosh', models.CharField(max_length=2)),
                ('jinsi', models.BooleanField()),
                ('telraqam', models.CharField(max_length=14)),
                ('yashashjoyi', models.CharField(max_length=200)),
            ],
        ),
    ]
