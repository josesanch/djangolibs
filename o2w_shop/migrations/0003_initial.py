# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoProducto'
        db.create_table('o2w_shop_tipoproducto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('o2w_shop', ['TipoProducto'])

        # Adding model 'Producto'
        db.create_table('o2w_shop_producto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['o2w_shop.TipoProducto'])),
            ('destacado', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('body', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, blank=True)),
            ('precio', self.gf('django.db.models.fields.FloatField')()),
            ('meta_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('meta_keywords', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('meta_title', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
        ))
        db.send_create_signal('o2w_shop', ['Producto'])


    def backwards(self, orm):
        # Deleting model 'TipoProducto'
        db.delete_table('o2w_shop_tipoproducto')

        # Deleting model 'Producto'
        db.delete_table('o2w_shop_producto')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['o2w_shop']