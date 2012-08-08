#encoding:utf-8
from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse_lazy
from transmeta import canonical_fieldname

from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

from o2w.models import Node
from o2w import models

class ImageInline(generic.GenericTabularInline):
    verbose_name = "Imágenes"
    model = models.Image
    sortable_field_name = "position"
    extra=0

class FileInline(generic.GenericTabularInline):
    verbose_name = "Documentos"
    model = models.File
    sortable_field_name = "position"
    extra=0

class CabecerasInline(AdminImageMixin, generic.GenericTabularInline):
    verbose_name = "Cabeceras"
    model = models.ImageHeader

    extra=0


class NodeAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display        = ('name','title', 'parent', 'slug','position', 'published', 'empty', 'controller')
    list_filter         = ('published', 'parent')
    list_editable       = ('published', 'position')
    search_fields       = ('name','title')
    ordering            = ['position', 'parent']
    sortable_field_name = "position"
    prepopulated_fields = {"slug": ("name_es",)}
#    inlines = [ ImageInline, FileInline, CabecerasInline ]
    inlines = [ CabecerasInline ]

    fieldsets = (
        (None, {
            'fields': (
                ('name_es',),
                ('title_es', ),
                ('subtitle_es', ),
                ('parent', 'position'),
                'slug', 'controller', 'image', 'published', 'empty', 'body_es'
            )
        }),

        # ('Contenido (idiomas)' , {
        #     'classes' : ('collapse',),
        #     'fields' : ('body_en', 'body_de')
        # }),

        ('SEO', {
            'classes' : ('collapse',),
            'fields': ('meta_title', 'meta_description', 'meta_keywords',)
        })
     )



admin.site.register(Node, NodeAdmin)

class CompanyAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget },
    }



admin.site.register(models.Company, CompanyAdmin)
#admin.site.register(models.Image)
