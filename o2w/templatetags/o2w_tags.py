from django import template
from o2w.models import Node
register = template.Library()


@register.inclusion_tag('tags/menu.html')
def menu(selected, id='menu'):
    selectedSubNode = None

    if selected.is_parent():
        selectedNode = selected
    else:
        selectedNode = selected.get_parent()
        selectedSubNode = selected


    if selectedNode:
        submenu = selectedNode.get_children()


    return {
        'menu' : Node.objects.filter(parent_id__isnull=True).order_by('position'),
        'selected': selectedNode,
        'submenu' : submenu,
        'selectedSubMenu' : selectedSubNode,
        'id' : id
    }
