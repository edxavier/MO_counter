__author__ = 'Eder Xavier Rojas'


from collections import Counter

events = []
fechas = []

events_file = raw_input("Nombre del archivo: ")
print "you entered", events_file
try:
    f = open(events_file,'r')
    line = f.readline()
    while line:
        try :
            #Set the whole string
            #remove enter
            if(not line.startswith('#')):
                line = line.rstrip('\n').rstrip('\r')
                line = ','.join(line.split(',')[3:])
                try:
                    if line:
                        #print(line)
                        #dividir las lineas por sus espacios en blanco
                        pieces = line.split(',')
                        #rearmar las lineas a partir de la segunda posicion
                        key = pieces[0].strip('"')+","+pieces[1].strip('"')
                        fechas.append(pieces[2].split()[1])
                        key = key.strip('"')
                        events.append(key)
                except:
                    pass
            line = f.readline()
        except:
            pass

    events_count = Counter(events)
    total = 0
    for key in events_count:
        total += events_count[key]
        print(key+","+str(events_count[key]))
    print("TOTAL EVENTOS:"+str(total))
    print("------------------------------------")
    fachas_count = Counter(fechas)
    for key in fachas_count:
        print(key+","+str(fachas_count[key]))

except Exception,e:
    print("Error: No fue posible leer el archivo [ " + events_file+" ]")
    print(e)