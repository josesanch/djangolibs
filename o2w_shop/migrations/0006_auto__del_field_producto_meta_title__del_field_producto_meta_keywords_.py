# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Producto.meta_title'
        db.delete_column('o2w_shop_producto', 'meta_title')

        # Deleting field 'Producto.meta_keywords'
        db.delete_column('o2w_shop_producto', 'meta_keywords')

        # Deleting field 'Producto.meta_description'
        db.delete_column('o2w_shop_producto', 'meta_description')

        # Adding field 'Producto.nombre_comercial'
        db.add_column('o2w_shop_producto', 'nombre_comercial',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)


        # Changing field 'Producto.nombre_cientifico'
        db.alter_column('o2w_shop_producto', 'nombre_cientifico', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):
        # Adding field 'Producto.meta_title'
        db.add_column('o2w_shop_producto', 'meta_title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=125, blank=True),
                      keep_default=False)

        # Adding field 'Producto.meta_keywords'
        db.add_column('o2w_shop_producto', 'meta_keywords',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Producto.meta_description'
        db.add_column('o2w_shop_producto', 'meta_description',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Deleting field 'Producto.nombre_comercial'
        db.delete_column('o2w_shop_producto', 'nombre_comercial')


        # Changing field 'Producto.nombre_cientifico'
        db.alter_column('o2w_shop_producto', 'nombre_cientifico', self.gf('django.db.models.fields.TextField')())

    models = {
        'o2w_shop.producto': {
            'Meta': {'object_name': 'Producto'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'conservacion': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'destacado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'frescura': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre_cientifico': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nombre_comercial': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'obtencion': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'origen': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'precio': ('django.db.models.fields.FloatField', [], {}),
            'presentacion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['o2w_shop.TipoProducto']"})
        },
        'o2w_shop.tipoproducto': {
            'Meta': {'object_name': 'TipoProducto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['o2w_shop']