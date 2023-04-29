from django import template

from menu.models import Item


register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu) -> dict:
    """ Формирование меню. """
    try:
        items = Item.objects.filter(menu__title=menu)
        items_values = items.values()
        primary_item = [item for item in items_values.filter(parent=None)]
        selected_item_id = int(context['request'].GET[menu])
        selected_item = items.get(id=selected_item_id)
        selected_item_id_list = get_selected_item_id_list(
            selected_item, primary_item, selected_item_id
        )
        for item in primary_item:
            if item['id'] in selected_item_id_list:
                item['child_items'] = get_child_items(
                    items_values, item['id'], selected_item_id_list
                )
        result_dict = {'items': primary_item}

    except Exception:
        result_dict = {
            'items': [
                item for item in Item.objects.filter(menu__title=menu,
                                                     parent=None).values()
                ]
        }

    result_dict['menu'] = menu
    result_dict['other_querystring'] = get_querystring(context, menu)

    return result_dict


@register.simple_tag(takes_context=True)
def get_querystring(context, menu) -> str:
    """ Определение индексов для "пути" к меню. """
    querystring_args: list = []
    for key in context['request'].GET:
        if key != menu:
            querystring_args.append(key + '=' + context['request'].GET[key])
    querystring = ('&').join(querystring_args)
    return querystring


def get_child_items(items_values, current_item_id,
                    selected_item_id_list) -> list:
    """ Формирование подменю. """
    item_list = [
        item for item in items_values.filter(parent_id=current_item_id)
    ]
    for item in item_list:
        if item['id'] in selected_item_id_list:
            item['child_items'] = get_child_items(
                items_values, item['id'], selected_item_id_list
            )
    return item_list


def get_selected_item_id_list(parent, primary_item, selected_item_id) -> list:
    """ Определение id активных секций меню. """
    selected_item_id_list: list = []
    while parent:
        selected_item_id_list.append(parent.id)
        parent = parent.parent
    if not selected_item_id_list:
        for item in primary_item:
            if item['id'] == selected_item_id:
                selected_item_id_list.append(selected_item_id)
    return selected_item_id_list
