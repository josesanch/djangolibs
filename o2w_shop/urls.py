from django.conf.urls import patterns, url


urlpatterns = patterns(
    'o2w_shop.views',
    url(r'^/$', 'productHome', name='productHome'),
    url(r'^/pedido/$', 'pedidos', name='pedidos'),
    url(r'^/pedido/(?P<paso>\d+)?$', 'pedidos', name='pedidos'),
    url(r'^/pedido/add/(?P<id>\d+)/$', 'productAdd', name='productAdd'),
    url(r'^/pedido/clear/$', 'productClear', name='productClear'),
    
    url(r'^/(?P<slug>[^/]*)/$', 'productList', name='productList'),
    url(r'^/(?P<slug>[^/]*)/(?P<producto>.*)/$', 'productView', name='productView'),

    
)
 