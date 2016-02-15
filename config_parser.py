import os

#read config from file
def loadConfig(fileName = None):
    config = {}
    lineNo = 0
    if fileName == None:
        fileName = os.path.dirname(os.path.realpath(__file__)) + "/car.config"
    
    with open(fileName) as f:
        for line in f:
            lineNo += 1
            line = line.strip()
            if len(line) == 0 or line.startswith("#"):
                continue
            line = line.split(":")
            if len(line) != 2:
                raise Exception("Error reading config on line " + str(lineNo))
            key = line[0].strip().lower()
            value = line[1].strip()
            if not key or not value:
                raise Exception("Error reading config on line " + str(lineNo))
            config[key] = value
    return config

#print any dict in form:
#header
#  key1: value1
#  key2: value2 ...
def printDict(header, d):
    print "\n", header
    for k in d:
        print "  " + str(k) + ": " + str(d[k])
    print
