import json

def lectureJSON(file,flag):
    with open(file, 'r') as openfile:
        dict = json.load(openfile)[flag]
    return str(dict)

def lectureSimpleJSON(file):
    with open(file, 'r') as openfile:
        dict = json.load(openfile)
    return dict
def EcritureJSON(file,flag,valeur):
    openfile = open(file, 'r')
    dict = json.load(openfile)
    openfile.close()
    writeFile = open(file, 'w')
    dict[flag] = valeur
    json.dump(dict,writeFile,indent=2)

def EcritureSansEcrasement(file,vardict,newDictName):
    with open(file, 'r') as openfile:
        dict1 = json.load(openfile)
    with open(file,"w") as file :
        newdict = {newDictName : vardict} 
        alldict = dict(dict1,**newdict)
        json.dump(alldict,file,indent=2)

def compteurJSON(file):
    with open(file, 'r') as openfile:
        dict1 = json.load(openfile)
        return len(dict1)