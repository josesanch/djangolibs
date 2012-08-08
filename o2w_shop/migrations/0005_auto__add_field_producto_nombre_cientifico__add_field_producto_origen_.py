# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Producto.nombre_cientifico'
        db.add_column('o2w_shop_producto', 'nombre_cientifico',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Producto.origen'
        db.add_column('o2w_shop_producto', 'origen',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Producto.categoria'
        db.add_column('o2w_shop_producto', 'categoria',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=25, blank=True),
                      keep_default=False)

        # Adding field 'Producto.frescura'
        db.add_column('o2w_shop_producto', 'frescura',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=25, blank=True),
                      keep_default=False)

        # Adding field 'Producto.obtencion'
        db.add_column('o2w_shop_producto', 'obtencion',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=80, blank=True),
                      keep_default=False)

        # Adding field 'Producto.conservacion'
        db.add_column('o2w_shop_producto', 'conservacion',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=80, blank=True),
                      keep_default=False)

        # Adding field 'Producto.presentacion'
        db.add_column('o2w_shop_producto', 'presentacion',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Producto.nombre_cientifico'
        db.delete_column('o2w_shop_producto', 'nombre_cientifico')

        # Deleting field 'Producto.origen'
        db.delete_column('o2w_shop_producto', 'origen')

        # Deleting field 'Producto.categoria'
        db.delete_column('o2w_shop_producto', 'categoria')

        # Deleting field 'Producto.frescura'
        db.delete_column('o2w_shop_producto', 'frescura')

        # Deleting field 'Producto.obtencion'
        db.delete_column('o2w_shop_producto', 'obtencion')

        # Deleting field 'Producto.conservacion'
        db.delete_column('o2w_shop_producto', 'conservacion')

        # Deleting field 'Producto.presentacion'
        db.delete_column('o2w_shop_producto', 'presentacion')


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
            'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'meta_title': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre_cientifico': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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