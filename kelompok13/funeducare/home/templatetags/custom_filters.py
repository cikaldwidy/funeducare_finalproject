from django import template

register = template.Library()

# Filter untuk memisahkan deskripsi berdasarkan baris baru
@register.filter
def split_paragraphs(value):
    if value:  
        return value.split("\n") 
    return []

@register.filter
def batch(iterable, size):
    iterable = list(iterable)
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

# Filter untuk memotong string hingga kata terakhir yang masih utuh
@register.filter
def slice_to_last_word(value, max_length):
    if not value:
        return ""
    truncated_text = value[:max_length]  
    last_space = truncated_text.rfind(' ')
    if last_space != -1:
        return truncated_text[:last_space]
    return truncated_text
