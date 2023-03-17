from PyQt5.uic import *
from PyQt5.QtWidgets import *


def ajouter():
    ch=windows.ch.text()
    if not (len(ch)>3 and len(ch)<7):
        QMessageBox.critical(windows,'Erreur',"unsecces")
    else:
        QMessageBox.information(windows,"valider","succes")
        perms = combination(ch)
        f=open("d.txt","w")
        for i in range(len(perms)):
            f.write(perms[i]+"\n")
            print(perms[i]+"\n")
        f.close()
        

def combination(x):
    if len(x) == 1:
        return x
    perms = []
    for i in range(len(x)):
        sub_perms = combination(x[:i] + x[i+1:])
        for j in range(len(sub_perms)): 
            perms += [x[i] + sub_perms[j]]
    return perms      


def afficher():
    windows.list.clear()
    f=open("d.txt","r")
    ch=f.read()
    windows.list.addItem(ch)
    f.close()


def fermer():
    windows.close()
    f=open('d.txt',"w")
    f.write("")
    f.close()

app=QApplication([])
windows=loadUi("combinaison.ui")
windows.show()
windows.b1.clicked.connect(ajouter)
windows.b2.clicked.connect(afficher)
windows.b3.clicked.connect(fermer)

app.exec_()


#youssef habbachi