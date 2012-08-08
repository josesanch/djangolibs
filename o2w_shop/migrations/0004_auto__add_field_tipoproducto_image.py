# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TipoProducto.image'
        db.add_column('o2w_shop_tipoproducto', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default=1, max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TipoProducto.image'
        db.delete_column('o2w_shop_tipoproducto', 'image')


    models = {
        'o2w_shop.producto': {
            'Meta': {'object_name': 'Producto'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'destacado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'meta_title': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'precio': ('django.db.models.fields.FloatField', [], {}),
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