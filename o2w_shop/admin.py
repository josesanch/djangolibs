#encoding:utf-8
from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from django.contrib.contenttypes import generic
from o2w.models import Image as O2WImage
from o2w_shop import models

class ImageInline(AdminImageMixin, generic.GenericTabularInline):
    verbose_name = "Imágenes"
    model = O2WImage
    sortable_field_name = "position"
    extra=0



class ProductosAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display        = ('name', 'image_img', 'tipo', 'destacado', 'precio',)
    list_filter         = ('tipo','destacado')
    search_fields       = ('name',)
    sortable_field_name = "position"
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ ImageInline ]



class TipoProductosAdmin(AdminImageMixin, admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}




admin.site.register(models.Producto, ProductosAdmin)
admin.site.register(models.TipoProducto, TipoProductosAdmin)
