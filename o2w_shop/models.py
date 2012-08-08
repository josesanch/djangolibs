#encoding:utf-8
from django.db import models
from sorl.thumbnail import ImageField, default
ADMIN_THUMBS_SIZE = "90x90"

class TipoProducto(models.Model):
    name = models.CharField(max_length=255)
    position = models.PositiveSmallIntegerField("position")
    slug     = models.CharField(max_length=255)
    image    = models.ImageField(upload_to='uploaded_fotos', blank=True)
    body        = models.TextField(blank=True, verbose_name='Texto')

    def __unicode__(self):
        return self.name

        
    @models.permalink
    def get_absolute_url(self):
        return ('productList', [self.slug])
        
    class Meta:
        ordering = ['position']


class Producto(models.Model):
    name     = models.CharField(max_length=255)
    tipo     = models.ForeignKey(TipoProducto)

    destacado   = models.BooleanField()
    body        = models.TextField(blank=True, verbose_name='Texto')
    image       = ImageField(upload_to='uploaded_bloque', blank=True)
    slug        = models.SlugField(max_length=255, blank=True)

    precio  = models.FloatField()
    nombre_cientifico = models.CharField(max_length=255,blank=True, verbose_name='Nombre cientifico')
    nombre_comercial = models.CharField(max_length=255,blank=True, verbose_name='Nombre comercial')
    origen = models.TextField(blank=True)
    categoria = models.CharField(max_length=25, blank=True)
    frescura = models.CharField(max_length=25, blank=True)
    obtencion = models.CharField(max_length=80, blank=True)
    conservacion = models.CharField(max_length=80, blank=True)
    formula = models.CharField(max_length=80, blank=True)
    presentacion = models.TextField(blank=True)

    def image_img(self):
        if self.image:
            thumb = default.backend.get_thumbnail(self.image, ADMIN_THUMBS_SIZE)
            return u'<img src="%s" />' % thumb.url
        else:
            return ''

    image_img.short_description = 'Foto'
    image_img.allow_tags = True
    
    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('productView', [self.tipo.slug, self.slug])

    class Meta:
        ordering = ['-id', 'name']
            