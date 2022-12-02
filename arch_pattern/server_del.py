import os
from jinja2 import Template

from props import TEMPLATES

def render(template_name, *arg):
  path = os.path.join(TEMPLATES, 'index.html')
  print(path)
  

      template = Template(file.read())


    # template = Template(template_name)

    return template.render(*arg)




