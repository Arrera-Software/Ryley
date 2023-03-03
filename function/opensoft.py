import os as systeme
import subprocess

def openSoft(file):
    systeme.system("start " + file)
    
def openSoftwareRacourcie(name):
    name = str(name)
    subprocess.Popen(["cmd", "/c", "start", name])