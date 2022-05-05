# Generated by Django 3.2.2 on 2021-06-09 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abbreviations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmid', models.IntegerField(blank=True, null=True)),
                ('normalized', models.CharField(blank=True, max_length=100, null=True)),
                ('entity', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'abbreviations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cells',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmid', models.IntegerField(blank=True, null=True)),
                ('normalized', models.CharField(blank=True, max_length=30, null=True)),
                ('entity', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'cells',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Chemicals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmid', models.IntegerField(blank=True, null=True)),
                ('normalized', models.IntegerField(blank=True, null=True)),
                ('entity', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'chemicals',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmid', models.IntegerField(blank=True, null=True)),
                ('pubyear', models.SmallIntegerField(blank=True, db_column='pubYear', null=True)),
                ('pubmonth', models.IntegerField(blank=True, db_column='pubMonth', null=True)),
                ('pubday', models.IntegerField(blank=True, db_column='pubDay', null=True)),
            ],
            options={
                'db_table': 'dates',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmid', models.IntegerField(blank=True, null=True)),
                ('normalized', models.CharField(blank=True, max_length=30, null=True)),
                ('entity', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'diseases',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Enzymes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmid', models.IntegerField(blank=True, null=True)),
                ('normalized', models.CharField(blank=True, max_length=30, null=True)),
                ('entity', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'enzymes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Genes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmid', models.IntegerField(blank=True, null=True)),
                ('normalized', models.IntegerField(blank=True, null=True)),
                ('entity', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'genes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Histones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmid', models.IntegerField(blank=True, null=True)),
                ('normalized', models.CharField(blank=True, max_length=150, null=True)),
                ('entity', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'histones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mutations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmid', models.IntegerField(blank=True, null=True)),
                ('vartype', models.CharField(blank=True, max_length=50, null=True)),
                ('entity', models.CharField(blank=True, max_length=100, null=True)),
                ('normalized', models.CharField(blank=True, max_length=100, null=True)),
                ('rs', models.CharField(blank=True, max_length=100, null=True)),
                ('gene', models.CharField(blank=True, max_length=100, null=True)),
                ('uniprot', models.CharField(blank=True, max_length=50, null=True)),
                ('uniprotgene', models.CharField(blank=True, db_column='uniprotGene', max_length=50, null=True)),
            ],
            options={
                'db_table': 'mutations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmid', models.IntegerField(blank=True, null=True)),
                ('entity', models.CharField(blank=True, max_length=150, null=True)),
                ('normalized', models.IntegerField(blank=True, null=True)),
                ('probability', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'species',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tissues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pmid', models.IntegerField(blank=True, null=True)),
                ('normalized', models.CharField(blank=True, max_length=150, null=True)),
                ('entity', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'tissues',
                'managed': False,
            },
        ),
    ]
