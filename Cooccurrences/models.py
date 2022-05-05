from django.db import models
from django.http import HttpResponseRedirect, request
from django.shortcuts import get_object_or_404, render


# Each class of this file refers to one table in our database.
# ! Differences with this database model and Geneview(2018) :
# * As id is a name that is reserved for primary keys when working with Django
# * all the id fields from the database were turned into "normalized".
# * An additional step is required in your database structure, for each table in a mysql shell :
# * ALTER TABLE `table_name` ADD id int NOT NULL AUTO_INCREMENT primary key;


class Abbreviations(models.Model):
    pmid = models.IntegerField(blank=True, null=True)
    normalized = models.CharField(max_length=100, blank=True, null=True)
    entity = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abbreviations'

    def __str__(self):
        return("pmid = " + str(self.pmid) + " normalized = " + str(self.normalized) + " entity = " + str(self.entity))


class Cells(models.Model):
    pmid = models.IntegerField(blank=True, null=True)
    normalized = models.CharField(max_length=30, blank=True, null=True)
    entity = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cells'

    def __str__(self):
        return("pmid = " + str(self.pmid) + " normalized = " + str(self.normalized) + " entity = " + str(self.entity))


class Chemicals(models.Model):
    pmid = models.IntegerField(blank=True, null=True)
    normalized = models.IntegerField(blank=True, null=True)
    entity = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chemicals'

    def __str__(self):
        return("pmid = " + str(self.pmid) + " normalized = " + str(self.normalized) + " entity = " + str(self.entity))


class Dates(models.Model):
    pmid = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    pubyear = models.SmallIntegerField(
        db_column='pubYear', blank=True, null=True)
    # Field name made lowercase.
    pubmonth = models.IntegerField(
        db_column='pubMonth', blank=True, null=True)
    # Field name made lowercase.
    pubday = models.IntegerField(db_column='pubDay', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dates'

    def __str__(self):
        return("pmid = " + str(self.pmid) + " pubyear = " + str(self.pubyear) + " pubmonth = " + str(self.pubmonth) + " pubday = " + str(self.pubday))


class Diseases(models.Model):
    pmid = models.IntegerField(blank=True, null=True)
    normalized = models.CharField(max_length=30, blank=True, null=True)
    entity = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diseases'

    def __str__(self):
        return("pmid = " + str(self.pmid) + " normalized = " + str(self.normalized) + " entity = " + str(self.entity))


class Enzymes(models.Model):
    pmid = models.IntegerField(blank=True, null=True)
    normalized = models.CharField(max_length=30, blank=True, null=True)
    entity = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enzymes'

    def __str__(self):
        return("pmid = " + str(self.pmid) + " normalized = " + str(self.normalized) + " entity = " + str(self.entity))


class Genes(models.Model):
    pmid = models.IntegerField(blank=True, null=True)
    normalized = models.IntegerField(blank=True, null=True)
    entity = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genes'

    def __str__(self):
        return("pmid = " + str(self.pmid) + " normalized = " + str(self.normalized) + " entity = " + str(self.entity))


class Histones(models.Model):
    pmid = models.IntegerField(blank=True, null=True)
    normalized = models.CharField(max_length=150, blank=True, null=True)
    entity = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histones'

    def __str__(self):
        return("pmid = " + str(self.pmid) + " normalized = " + str(self.normalized) + " entity = " + str(self.entity))


class Mutations(models.Model):
    pmid = models.IntegerField(blank=True, null=True)
    vartype = models.CharField(max_length=50, blank=True, null=True)
    entity = models.CharField(max_length=100, blank=True, null=True)
    normalized = models.CharField(max_length=100, blank=True, null=True)
    rs = models.CharField(max_length=100, blank=True, null=True)
    gene = models.CharField(max_length=100, blank=True, null=True)
    uniprot = models.CharField(max_length=50, blank=True, null=True)
    # Field name made lowercase.
    uniprotgene = models.CharField(
        db_column='uniprotGene', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mutations'

    def __str__(self):
        return("pmid = " + str(self.pmid) + " vartype = " + str(self.vartype) + " entity = " + str(self.entity)
               + " normalized = " + str(self.normalized) + " rs = " + str(self.rs) + " gene = " + str(self.gene) + " uniprot = " + str(self.uniprot))


class Species(models.Model):
    pmid = models.IntegerField(blank=True, null=True)
    entity = models.CharField(max_length=150, blank=True, null=True)
    normalized = models.IntegerField(blank=True, null=True)
    probability = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'species'

    def __str__(self):
        return("pmid = " + str(self.pmid) + " entity = " + str(self.entity) + " normalized = " + str(self.normalized) + " probability = " + str(self.probability))


class Tissues(models.Model):
    pmid = models.IntegerField(blank=True, null=True)
    normalized = models.CharField(max_length=150, blank=True, null=True)
    entity = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tissues'

    def __str__(self):
        return("pmid = " + str(self.pmid) + " normalized = " + str(self.normalized) + " entity = " + str(self.entity))
