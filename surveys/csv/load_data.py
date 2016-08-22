import csv
import os
import django
import sys

sys.path.append(os.path.abspath(os.path.dirname(__name__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chadmin.settings")
django.setup()

from surveys.models import *

markets_file = os.path.join('surveys','csv','markets.csv')
with open(markets_file, 'r+') as csvfile:
    reader = csv.reader(csvfile)
    try:
        for row in reader:
            market = Market()
            market.name = row[0]
            market.code = row[1]
            market.currency_code = row[2]
            market.save()
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))


locales_file = os.path.join('surveys','csv','locales.csv')
with open(locales_file, 'r+') as csvfile:
    reader = csv.reader(csvfile)
    try:
        for row in reader:
            locale = Locale()
            locale.name = row[0]
            locale.code = row[1]
            locale.mit_code = row[2]
            locale.save()
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
