#!/usr/bin/env python
import sys
import argparse
import json
import time

x = []
o = ''
t = ''
jsn = 0
tmp = 0

def scp(c):
    try:
        global x, o, t, jsn, tmp
        a = str(c[1])
        a = a.replace("['", "")
        a = a.replace("']", "")

        ap = argparse.ArgumentParser()
        ap.add_argument('-t', required=False, type=str)
        ap.add_argument('-o', required=False, type=str)
        ap.add_argument(a)
        args = ap.parse_args()

###########################################################################
        if args.o:
            o = args.o
            tmp = 1
        else:
            pass

        if args.t:
            t = args.t
            if t == "json":
                jsn = 1
            elif t == "text":
                pass
            else:
                print("-t invalid flag")
        else:
            pass

###########################################################################
        if jsn == 1 and tmp == 0:
            q = a.split('/')
            q = q[-1]
            
            with open(a) as file:
                for z in file:
                    z = z.splitlines()
                    b = z[0]
                    x.append({"log":b})
                x = {q: x}
            file.close()

            with open("nginx.json", "w") as g:
                json.dump(x, g, indent=2)
            g.close()
            
###########################################################################
        elif tmp == 0:
            with open(a) as file:
                g = file.read()
                with open("nginx.txt", "w") as tulis:
                    tulis.write(g)

###########################################################################
        elif tmp == 1:
            p = o.split('/')
            u = p[-1]
            u = u.split('.')

            q = a.split('/')
            q = q[-1]

            if u[-1] == "json":
                with open(a) as file:
                    for z in file:
                        z = z.splitlines()
                        b = z[0]
                        x.append({"log":b})
                    x = {q: x}
                file.close()

                with open(o, "w") as g:
                    json.dump(x, g, indent=2)
                g.close()
            
            elif u[-1] == "txt":     
                with open(a) as file:
                    g = file.read()
                    with open(o, "w") as tulis:
                        tulis.write(g)
            else:
                print("invalid extention")
    except:
        print("Invalid Argument \nUse 'python FIQIH_AL_AZIZ.py -h' for Help")

def main():
    try:
        c = sys.argv
        if c[1] == '-h':
            print("command: sudo python FIQIH_AL_AZIZ.py DIR/FILE -t TYPE -o DIR/FILE")
        else:
            scp(c)
    except:
        print("Invalid Argument \nUse 'python FIQIH_AL_AZIZ.py -h' for Help")
        

if __name__ == '__main__':
    main()
