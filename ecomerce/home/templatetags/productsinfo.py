from django import template

register = template.Library()

@register.simple_tag
def progress_percentage(value,total):
    percentage = (value/total)*100
    if total == 0:  # Avoid division by zero
        return 0
    return percentage
    
@register.simple_tag
def discount_price(price, discount):
    discount_amount = (discount/100) * price
    return int(price - discount_amount)