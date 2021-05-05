# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Stations(models.Model):
    generated_id = models.AutoField(primary_key=True, blank=True, null=False)
    station_id = models.TextField(db_column='Station_id', blank=True, null=True)  # Field name made lowercase.
    station_name = models.TextField(db_column='Station_Name', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    longnitude = models.FloatField(db_column='Longnitude', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'STATIONS'
