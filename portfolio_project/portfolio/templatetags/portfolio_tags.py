from django import template
from portfolio.models import PortfolioItem

register = template.Library()

@register.simple_tag
def portfolio_count():
    return PortfolioItem.objects.count()
