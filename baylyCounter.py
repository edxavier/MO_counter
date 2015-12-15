__author__ = 'Eder Xavier Rojas'


from collections import Counter

events = []

events_file = raw_input("Nombre del archivo: ")
print "you entered", events_file
try:
    f = open(events_file,'r')
    line = f.readline()
    while line:
        try :
            #Set the whole string
            #remove enter
            line = line.rstrip('\n').rstrip('\r')
            line = ' '.join(line.split())
            try:
                if line:
                    #dividir las lineas por sus espacios en blanco
                    pieces = line.split()
                    #rearmar las lineas a partir de la segunda posicion
                    key = ' '.join(pieces[2:])
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
        print(key+":"+str(events_count[key]))
    print("TOTAL EVENTOS:"+str(total))
except Exception,e:
    print("Error: No fue posible leer el archivo [ " + events_file+" ]")
    print(e)