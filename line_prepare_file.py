def line_prepare(line):
    line = line.map(lambda x: str(x))
    line = line.map(lambda x: (x.replace('[','')))
    line = line.map(lambda x: (x.replace(']','')))
    line = line.map(lambda x: (x.replace(',','')))
    pspdata = line.map(lambda x: (x.replace('"','').split("'")[1], x.replace('"','').split("'")[3],x.replace('"','').split("'")[5], x.replace('"','').split("'")[6],x.replace('"','').split("'")[9], x.replace('"','').split("'")[len(x.replace('"','').split("'")) - 2]))
    return pspdata