#encoding:utf-8
from django.db import models
from django.db.models import permalink
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from transmeta import TransMeta
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField
from django_google_maps import fields as map_fields

class BaseNode(models.Model):
    __metaclass__ = TransMeta

    name             = models.CharField(max_length=255,verbose_name="Nombre")
    title            = models.CharField(max_length=255,verbose_name="Titulo")
    subtitle         = models.CharField(max_length=255,verbose_name="Sub Titulo", blank=True, null=True)
    parent           = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    position         = models.PositiveSmallIntegerField("position")
    body             = RichTextField(blank=True,verbose_name="Contenido")
    slug             = models.CharField(max_length=125, db_index=True)
    controller       = models.CharField(max_length=125, blank=True)
    published        = models.BooleanField()
    empty            = models.BooleanField(verbose_name='Redirige a subseccion')
    image             = ImageField(upload_to='uploaded_images', blank=True)

    meta_description = models.TextField(blank=True)
    meta_keywords    = models.TextField(blank=True)
    meta_title       = models.CharField(max_length=125, blank=True)

    def __unicode__(self):
        return self.name

    def get_headers(self):
        return ImageHeader.objects.filter(object_id=self.id)

    def get_files(self):
        return Files.objects.filter(object_id=self.id)

    def get_images(self):
        return Image.objects.filter(object_id=self.id)

    def get_children(self):
        return Node.objects.filter(parent_id=self.id).order_by('position')

    def get_parent(self):
        if self.parent_id:
            return Node.objects.get(id=self.parent_id)
        return None

    def is_parent(self):
        return not self.parent_id

    def get_image(self):
        if self.image:
            return self.image

    def get_headers_including_parents(self):

        if self.get_headers() or not self.get_parent():
            return self.get_headers()
        else:
            return self.get_parent().get_headers()

    @permalink
    def get_absolute_url(self):
        return ('node', None, { 'slug': self.slug })

    class Meta:
        translate = ('title', 'subtitle', 'body', 'name', )
        abstract = True
        ordering = ['position']
        verbose_name = "Página"
        verbose_name_plural = "Contenidos"

class Node(BaseNode):
    pass

class BaseMedia(models.Model):
    name           = models.CharField(max_length=255, blank=True)
    object_id      = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")
    position       = models.PositiveSmallIntegerField("position", blank=True)


    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['position']



class File(BaseMedia):
    file = models.FileField(upload_to='uploaded_files')
    content_type   = models.ForeignKey(ContentType, related_name="media_contenttype")

class Image(BaseMedia):
    image = ImageField(upload_to='uploaded_images')
    content_type   = models.ForeignKey(ContentType, related_name="images_contenttype")

class ImageHeader(BaseMedia):
    image = ImageField(upload_to='uploaded_headers')
    content_type   = models.ForeignKey(ContentType, related_name="headers_contenttype")





class Company(models.Model):
    name = models.CharField(max_length = 255, verbose_name='Nombre')
    street  = models.CharField(max_length = 250, verbose_name='Dirección')
    postalcode = models.CharField(max_length = 50, verbose_name='Código postal')
    city = models.CharField(max_length = 50, verbose_name='Ciudad')
    province = models.CharField(max_length = 50, verbose_name='Provincia')
    phone = models.CharField(max_length = 25, verbose_name='Teléfono')
    fax = models.CharField(max_length = 25, blank=True, verbose_name='Fax')
    email = models.CharField(max_length = 50, verbose_name='Email')
    text  = models.TextField(blank=True, verbose_name='Texto')
    image = models.ImageField(upload_to='uploaded_company', blank=True, verbose_name='Foto')
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100, blank=True, verbose_name='Geolocalización')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Datos de empresa'
        verbose_name_plural = "Datos de empresa"    

    