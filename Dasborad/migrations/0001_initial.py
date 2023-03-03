# Generated by Django 4.1.7 on 2023-03-02 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(choices=[('food', 'food'), ('cars', 'cars'), ('fans', 'fans')], max_length=20, null=True)),
                ('quantity', models.PositiveBigIntegerField(null=True)),
            ],
        ),
    ]
