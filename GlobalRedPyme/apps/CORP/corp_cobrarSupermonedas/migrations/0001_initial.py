# Generated by Django 3.1.7 on 2021-11-28 00:55

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CobrarSupermonedas',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('identificacion', models.CharField(max_length=13)),
                ('codigoCobro', models.CharField(max_length=200)),
                ('monto', models.FloatField(null=True)),
                ('correo', models.EmailField(max_length=200)),
                ('estado', models.CharField(max_length=200)),
                ('user_id', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('state', models.SmallIntegerField(default=1)),
            ],
        ),
    ]
