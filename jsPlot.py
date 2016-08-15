from IPython.core.magic import (register_line_magic, register_cell_magic,
                                register_line_cell_magic)
from IPython.core.display import display, HTML, Javascript
from subprocess import call
import time
import os

pythonFile = """
math = Math

def setup():
    return '%s'

def inputs():
    return [%s]

%s
"""
pid = 0
base = open('base.html').read()
eachTime = open('plot.html').read()

@register_cell_magic
def jsPlot(line, cell):
    global pid
    pid += 1
    mode,parameter = line[:line.find(" ")], line[line.find(" "):]
    print(mode)
    print(parameter)
    pF = pythonFile%(mode,parameter,cell)
    pF = pF.replace("plot(","plot(%s,"%str(pid))
    pF = pF.replace("bar(","bar(%s,"%str(pid))
    pF = pF.replace("write(","write(%s,"%str(pid))

    fileName = 'tmp%d'%pid
    f = open(fileName+'.py','w')
    f.write(pF)
    f.close()
    call(["transcrypt", fileName+".py",'--nomin'])
    js = open("__javascript__/"+fileName+".js").read()
    js = js.replace('enumerable: true', 'enumerable: true, configurable:true')
    os.remove(fileName+'.py')
    os.remove("__javascript__/"+fileName+".js")
    print(pid)
    return HTML(eachTime.replace("JSSOURCE",js).replace("PID",str(pid)))


def start():
    return display(HTML(base))
