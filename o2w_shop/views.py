#encoding:utf-8
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from o2w_shop import models
from cart import Cart

import o2w
from app import forms

def getNodeProductos():
    return o2w.models.Node.objects.get(slug='productos')

    
def productHome(request):
    tipoProducto = models.TipoProducto.objects.all()[0]
    return redirect(tipoProducto, True)



def productList(request, slug = ''):
    tipo = get_object_or_404(models.TipoProducto, slug=slug)
    tipoProductos = models.TipoProducto.objects.all()
    todosProductos = models.Producto.objects.select_related().filter(tipo=tipo)

    paginator = Paginator(todosProductos, 9)
    page = request.GET.get('page')
    
    try:
        productos = paginator.page(page)
    except PageNotAnInteger:
        productos = paginator.page(1)
    except EmptyPage:
        productos = paginator.page(paginator.num_pages)

    return render(
        request,
        "shop/list.dhtml",{
            'tipoProducto' : tipo,
            'productos' : productos,
            'tipoProductos' : tipoProductos,
            'totalProductos' : len(todosProductos),
            'cart' : Cart(request),
            'node' : getNodeProductos()
        })



def productView(request, slug, producto):
    producto = get_object_or_404(models.Producto, tipo__slug=slug, slug=producto)

    if not producto:
        raise Http404

    tipoProductos = models.TipoProducto.objects.all()

    return render(
        request,
        'shop/view.dhtml', {
            'producto' : producto,
            'tipoProductos' : tipoProductos,
            'cart' : Cart(request),
            'node' : getNodeProductos()
        }
    )


def productAdd(request, id, cantidad = 1):
    cart = Cart(request)    
    producto = get_object_or_404(models.Producto, pk=id)
    cantidad = request.POST.get("cantidad", 1)
    cart.add(producto, producto.precio, cantidad)
    return redirect(pedidos)

def productClear(request):
    cart = Cart(request)
    cart.clear()
    return redirect(pedidos)

def pedidos(request, paso = 1):
    cart = Cart(request)
    template = 'shop/pedido%s.dhtml' % paso

    form = None
    if int(paso) == 2:
        form = forms.Facturacion(request.POST)
    
    return render(
        request,
        template, {
            'cart' : cart,
            'actual' : int(paso),
            'siguiente' : int(paso) + 1,
            'pasos' : [ 'Resumen de su pedido', 'Datos de facturacion', 'Datos de entrega', 'Confirmar pedido' ],
            'form' : form
        }
    )

