from django.contrib.auth import get_user_model
from django import template
from django.utils.html import format_html

register = template.Library()
user_model = get_user_model()

@register.filter
def author_details(author, current_user):
  if not isinstance(author, user_model):
  #check if author is in user_model collection
  #return empty string as default
    return ""
  if author == current_user:
    return format_html("<strong>me</strong>")

#check if first name and last name fields are populated
  if author.first_name and author.last_name:
    name = f"{author.first_name} {author.last_name}"
  else:
      name = f"{author.username}"

  if author.email:
    prefix = format_html('<a href="mailto:{}">', author.email)
    suffix = format_html('</a>')
  else:
    prefix = ""
    suffix = ""

  return format_html('{}{}{}', prefix, name, suffix)
