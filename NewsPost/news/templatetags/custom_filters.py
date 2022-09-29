from django import template
from re import findall as re_findall, sub as re_sub, escape as re_escape


register = template.Library()

filth_list = ["редиска", "дурак", "черт", "козел", "олух"]


@register.filter(name='censor')
def censor(value: str):
    if not isinstance(value, str):
        value = str(value)

    for word in re_findall(r'\b\S+\b', value):
        if word.lower() not in filth_list:
            continue
        regex = rf'(?=^|\S+){re_escape(word)}(?=\S+|$)'
        value = re_sub(regex, '*' * len(word), value)

    return value
