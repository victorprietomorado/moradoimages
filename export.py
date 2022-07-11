import csv, sys
import os

exportFile = "morado2-export.csv"

filename = "morado2.csv"

with open(exportFile, 'w') as f_write:
    with open(filename, 'r') as f_read:
        reader = csv.reader(f_read)
        try:
            for row in reader:
                url_foto = row[25]
                url_foto_png = url_foto.replace(".jpg" , ".png")
                try:
                    url_foto_final = url_foto_png.split('?v=')[0]
                except:
                    url_foto_final = url_foto_png

                row[25] = url_foto_final
                url = row[25]
                handle = row[0]
                title = row[1]

                f_write.write(handle + "," + title + "," + url +  "\n")

                
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))