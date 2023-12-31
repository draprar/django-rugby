# Generated by Django 4.2.2 on 2023-12-29 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0008_tale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Tale',
        ),
    ]
