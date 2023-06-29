import shutil
import subprocess
import os
from tkinter.filedialog import askopenfilename

class ObjetSoftware :
    
    def __init__(self,name):
        self.racourcieSoft =os.path.abspath("racoucie/"+str(name)+".lnk")
        
    def saveSoftware(self):
        emplacement = askopenfilename(defaultextension=".lnk", filetypes=[("Racourcie", ".lnk")])
        shutil.copyfile(emplacement,self.racourcieSoft)
        
    def openSoftware(self):
        subprocess.Popen(["cmd", "/c", "start", self.racourcieSoft])