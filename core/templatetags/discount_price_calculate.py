from django import template


register = template.Library()


@register.filter
def discount_price_calcualte(mrp_price, discount_percentage):
    return mrp_price-mrp_price*discount_percentage/100