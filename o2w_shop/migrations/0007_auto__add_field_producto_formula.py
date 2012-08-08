# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Producto.formula'
        db.add_column('o2w_shop_producto', 'formula',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=80, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Producto.formula'
        db.delete_column('o2w_shop_producto', 'formula')


    models = {
        'o2w_shop.producto': {
            'Meta': {'object_name': 'Producto'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'conservacion': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'destacado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'formula': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
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