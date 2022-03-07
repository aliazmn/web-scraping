# Generated by Django 4.0.3 on 2022-03-05 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='product name', max_length=255, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'color',
                'verbose_name_plural': 'colors',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='product name', max_length=255, unique=True, verbose_name='name')),
                ('price', models.PositiveIntegerField(help_text='product price', verbose_name='price')),
                ('exist', models.BooleanField(default=True, help_text='product existing check', verbose_name='exist')),
                ('color', models.ManyToManyField(help_text='product color', to='digikala.color', verbose_name='color')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]
