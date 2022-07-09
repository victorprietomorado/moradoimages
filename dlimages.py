import csv, sys
import requests
import urllib3
import os

filename = 'test.csv'
# errors='replace'
with open(filename, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            try:
                link = row[25]
                if link.startswith('http'):
                    link = link.split('?')[0]
                    data = requests.get(link)
                    print (link)
                    # Save file data to local copy
                    with open(os.path.basename(link), 'wb') as file:
                        file.write(data.content)
            except:
                print("Error " + link)
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
