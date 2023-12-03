# Zaprezentować generowanie własnej strony internetowej wyświetlającej tabele z danymi. Strona ma być wygenerowana z wykorzystaniem biblioteki Jinja 2. Dane maja być pobierane z plików CSV.
import csv
import os
from jinja2 import Template

path = os.path.dirname(os.path.abspath(__file__))

with open(f'{path}/data.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)
    
jinja_template = open(f'{path}/template.html', 'r').read()
html_template = Template(jinja_template).render(data=data)

with open(f'{path}/index.html', 'w') as file:
    file.write(html_template)
