#!/usr/bin/env python
import sys
import argparse
import json
import time

x = []
o = ''
t = ''
b = ''
jsn = 0
tmp = 0
daftar = {}

def scp(c):
    try:
        global x, o, t, b, jsn, tmp, daftar
        a = str(c[1])
        a = a.replace("['", "")
        a = a.replace("']", "")

        ap = argparse.ArgumentParser()
        ap.add_argument('-t', help="file type (.json or .txt)")
        ap.add_argument('-o')
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

        elif tmp == 0:
            with open(a) as file:
                g = file.read()
                with open("nginx.txt", "w") as tulis:
                    tulis.write(g)

###########################################################################
        if tmp == 1:
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
    except:
        print("Invalid Argument \nUse 'python mytools.py -h' for Help")

def main():            
    c = sys.argv
    if c[1] == '-h':
        print("Argument: python mytools.py DIR/FILE -t TYPE -o DIR/FILE")
    else:
        scp(c)

if __name__ == '__main__':
    main()
