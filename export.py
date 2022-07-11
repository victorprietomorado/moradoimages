import csv, sys

exportFile = "morado2-export.csv"

filename = "morado2.csv"

with open(exportFile, 'w') as f_write:
    with open(filename, 'r') as f_read:
        reader = csv.reader(f_read)
        try:
            for row in reader:
                nombre_foto = row[25].split("/")[-1]
                nombre_foto_png = nombre_foto.replace(".jpg" , ".png")
                try:
                    nombre_foto_final = nombre_foto_png.split('?v=')[0]
                except:
                    nombre_foto_final = nombre_foto_png

                row[25] = nombre_foto_final
                url_ref = "https://cdn.shopify.com/s/files/1/0626/0847/4335/products/"
                url = url_ref + row[25]
                handle = row[0]
                title = row[1]

                f_write.write(handle + "," + title + "," + url +  "\n")

                
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
