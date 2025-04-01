# Generated by Django 5.1.7 on 2025-04-01 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=13, unique=True)),
                ('descricao', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=30)),
                ('quantidade_minima', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('custo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('observacao', models.TextField(blank=True, max_length=255)),
            ],
        ),
    ]
