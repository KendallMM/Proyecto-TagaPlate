txt = ""
cont = 0

def update_id():
    global cont
    cont += 1
    return "%d" %cont

class Node():
    pass

class Null(Node):
    def __init__(self):
        self.type = 'void'

    def imprimir(self, ident):
        print(ident + "Node: Nulo")

    def traducir(self):
        global txt
        id = update_id()
        txt += id + "[label= "+"Nulo"+"]"+"\n\t"

        return id

class Program(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
    def imprimir(self, ident):

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        txt += id + "[label= "+self.name+"]"+"\n\t"
        return "TagaPlate {\n\t"+txt+"}"

class BodyProgram1(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)


    def traducir(self):
        global txt
        id = update_id()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class BodyProgram2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class BodyProgram3(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

"""class BodyProgramEmpty(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self, ident):
        print(ident + "Node: " + self.name)

    def translate(self):
        global txt
        id = update_id()
        return id"""

class Procedure1(Node):
    def __init__(self, son1, son2, son3, son4, son5, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

        # if str(type(self.son4)) == "<type 'tuple'>":
        if type(self.son4) == type(tuple()):
            # print "entro tupla"
            self.son4[0].imprimir(" " + ident)
        # elif str(type(self.son4)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son4.imprimir(" " + ident)
        # if str(type(self.son5)) == "<type 'tuple'>":
        if type(self.son5) == type(tuple()):
            # print "entro tupla"
            self.son5[0].imprimir(" " + ident)
        # elif str(type(self.son5)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son5.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son3) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        if type(self.son4) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        return id

class Procedure2(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

        # if str(type(self.son4)) == "<type 'tuple'>":
        if type(self.son4) == type(tuple()):
            # print "entro tupla"
            self.son4[0].imprimir(" " + ident)
        # elif str(type(self.son4)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son4.imprimir(" " + ident)
        # if str(type(self.son5)) == "<type 'tuple'>":
        if type(self.son5) == type(tuple()):
            # print "entro tupla"
            self.son5[0].imprimir(" " + ident)
        # elif str(type(self.son5)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son5.imprimir(" " + ident)
        if type(self.son6) == type(tuple()):
            # print "entro tupla"
            self.son6[0].imprimir(" " + ident)
        # elif str(type(self.son6)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son6.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son3) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        if type(self.son4) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()
        if type(self.son5) == type(tuple()):
            son6 = self.son6[0].traducir()
        else:
            son6 = self.son6.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        return id

class Instructions1(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, son8, son9, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8
        self.son9 = son9

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

        # if str(type(self.son4)) == "<type 'tuple'>":
        if type(self.son4) == type(tuple()):
            # print "entro tupla"
            self.son4[0].imprimir(" " + ident)
        # elif str(type(self.son4)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son4.imprimir(" " + ident)
        # if str(type(self.son5)) == "<type 'tuple'>":
        if type(self.son5) == type(tuple()):
            # print "entro tupla"
            self.son5[0].imprimir(" " + ident)
        # elif str(type(self.son5)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son5.imprimir(" " + ident)
        if type(self.son6) == type(tuple()):
            # print "entro tupla"
            self.son6[0].imprimir(" " + ident)
        # elif str(type(self.son6)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son6.imprimir(" " + ident)
        if type(self.son7) == type(tuple()):
            # print "entro tupla"
            self.son7[0].imprimir(" " + ident)
        # elif str(type(self.son7)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son7.imprimir(" " + ident)
        if type(self.son8) == type(tuple()):
            # print "entro tupla"
            self.son8[0].imprimir(" " + ident)
        # elif str(type(self.son8)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son8.imprimir(" " + ident)
        if type(self.son9) == type(tuple()):
            # print "entro tupla"
            self.son9[0].imprimir(" " + ident)
        # elif str(type(self.son9)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son9.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son3) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        if type(self.son4) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()
        if type(self.son5) == type(tuple()):
            son6 = self.son6[0].traducir()
        else:
            son6 = self.son6.traducir()
        if type(self.son6) == type(tuple()):
            son7 = self.son7[0].traducir()
        else:
            son7 = self.son7.traducir()
        if type(self.son7) == type(tuple()):
            son8 = self.son8[0].traducir()
        else:
            son8 = self.son8.traducir()
        if type(self.son8) == type(tuple()):
            son9 = self.son9[0].traducir()
        else:
            son9 = self.son9.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        txt += id + " -> " + son7 + "\n\t"
        txt += id + " -> " + son8 + "\n\t"
        txt += id + " -> " + son9 + "\n\t"

        return id

class Instructions2(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, son8, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

        # if str(type(self.son4)) == "<type 'tuple'>":
        if type(self.son4) == type(tuple()):
            # print "entro tupla"
            self.son4[0].imprimir(" " + ident)
        # elif str(type(self.son4)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son4.imprimir(" " + ident)
        # if str(type(self.son5)) == "<type 'tuple'>":
        if type(self.son5) == type(tuple()):
            # print "entro tupla"
            self.son5[0].imprimir(" " + ident)
        # elif str(type(self.son5)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son5.imprimir(" " + ident)
        if type(self.son6) == type(tuple()):
            # print "entro tupla"
            self.son6[0].imprimir(" " + ident)
        # elif str(type(self.son6)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son6.imprimir(" " + ident)
        if type(self.son7) == type(tuple()):
            # print "entro tupla"
            self.son7[0].imprimir(" " + ident)
        # elif str(type(self.son7)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son7.imprimir(" " + ident)
        if type(self.son8) == type(tuple()):
            # print "entro tupla"
            self.son8[0].imprimir(" " + ident)
        # elif str(type(self.son8)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son8.imprimir(" " + ident)


        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son3) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        if type(self.son4) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()
        if type(self.son5) == type(tuple()):
            son6 = self.son6[0].traducir()
        else:
            son6 = self.son6.traducir()
        if type(self.son6) == type(tuple()):
            son7 = self.son7[0].traducir()
        else:
            son7 = self.son7.traducir()
        if type(self.son7) == type(tuple()):
            son8 = self.son8[0].traducir()
        else:
            son8 = self.son8.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        txt += id + " -> " + son7 + "\n\t"
        txt += id + " -> " + son8 + "\n\t"

        return id

class Instructions3(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, son8, son9, son10, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8
        self.son9 = son9
        self.son10 = son10

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

        # if str(type(self.son4)) == "<type 'tuple'>":
        if type(self.son4) == type(tuple()):
            # print "entro tupla"
            self.son4[0].imprimir(" " + ident)
        # elif str(type(self.son4)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son4.imprimir(" " + ident)
        # if str(type(self.son5)) == "<type 'tuple'>":
        if type(self.son5) == type(tuple()):
            # print "entro tupla"
            self.son5[0].imprimir(" " + ident)
        # elif str(type(self.son5)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son5.imprimir(" " + ident)
        if type(self.son6) == type(tuple()):
            # print "entro tupla"
            self.son6[0].imprimir(" " + ident)
        # elif str(type(self.son6)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son6.imprimir(" " + ident)
        if type(self.son7) == type(tuple()):
            # print "entro tupla"
            self.son7[0].imprimir(" " + ident)
        # elif str(type(self.son7)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son7.imprimir(" " + ident)
        if type(self.son8) == type(tuple()):
            # print "entro tupla"
            self.son8[0].imprimir(" " + ident)
        # elif str(type(self.son8)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son8.imprimir(" " + ident)
        if type(self.son9) == type(tuple()):
            # print "entro tupla"
            self.son9[0].imprimir(" " + ident)
        # elif str(type(self.son9)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son9.imprimir(" " + ident)
        if type(self.son10) == type(tuple()):
            # print "entro tupla"
            self.son10[0].imprimir(" " + ident)
        # elif str(type(self.son10)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son10.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son3) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        if type(self.son4) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()
        if type(self.son5) == type(tuple()):
            son6 = self.son6[0].traducir()
        else:
            son6 = self.son6.traducir()
        if type(self.son6) == type(tuple()):
            son7 = self.son7[0].traducir()
        else:
            son7 = self.son7.traducir()
        if type(self.son7) == type(tuple()):
            son8 = self.son8[0].traducir()
        else:
            son8 = self.son8.traducir()
        if type(self.son8) == type(tuple()):
            son9 = self.son9[0].traducir()
        else:
            son9 = self.son9.traducir()
        if type(self.son9) == type(tuple()):
            son10 = self.son10[0].traducir()
        else:
            son10 = self.son10.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        txt += id + " -> " + son7 + "\n\t"
        txt += id + " -> " + son8 + "\n\t"
        txt += id + " -> " + son9 + "\n\t"
        txt += id + " -> " + son10 + "\n\t"

        return id

class Instructions4(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

        # if str(type(self.son4)) == "<type 'tuple'>":
        if type(self.son4) == type(tuple()):
            # print "entro tupla"
            self.son4[0].imprimir(" " + ident)
        # elif str(type(self.son4)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son4.imprimir(" " + ident)
        # if str(type(self.son5)) == "<type 'tuple'>":
        if type(self.son5) == type(tuple()):
            # print "entro tupla"
            self.son5[0].imprimir(" " + ident)
        # elif str(type(self.son5)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son5.imprimir(" " + ident)
        if type(self.son6) == type(tuple()):
            # print "entro tupla"
            self.son6[0].imprimir(" " + ident)
        # elif str(type(self.son6)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son6.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son3) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        if type(self.son4) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()
        if type(self.son5) == type(tuple()):
            son6 = self.son6[0].traducir()
        else:
            son6 = self.son6.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        return id

class Instructions5(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)


    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class Instructions6(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class Instructions7(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

        # if str(type(self.son4)) == "<type 'tuple'>":
        if type(self.son4) == type(tuple()):
            # print "entro tupla"
            self.son4[0].imprimir(" " + ident)
        # elif str(type(self.son4)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son4.imprimir(" " + ident)
        # if str(type(self.son5)) == "<type 'tuple'>":
        if type(self.son5) == type(tuple()):
            # print "entro tupla"
            self.son5[0].imprimir(" " + ident)
        # elif str(type(self.son5)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son5.imprimir(" " + ident)
        if type(self.son6) == type(tuple()):
            # print "entro tupla"
            self.son6[0].imprimir(" " + ident)
        # elif str(type(self.son6)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son6.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son3) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        if type(self.son4) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()
        if type(self.son5) == type(tuple()):
            son6 = self.son6[0].traducir()
        else:
            son6 = self.son6.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        return id

class Instructions8(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class Instructions9(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

        # if str(type(self.son4)) == "<type 'tuple'>":
        if type(self.son4) == type(tuple()):
            # print "entro tupla"
            self.son4[0].imprimir(" " + ident)
        # elif str(type(self.son4)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son4.imprimir(" " + ident)
        # if str(type(self.son5)) == "<type 'tuple'>":
        if type(self.son5) == type(tuple()):
            # print "entro tupla"
            self.son5[0].imprimir(" " + ident)
        # elif str(type(self.son5)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son5.imprimir(" " + ident)
        if type(self.son6) == type(tuple()):
            # print "entro tupla"
            self.son6[0].imprimir(" " + ident)
        # elif str(type(self.son6)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son6.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son3) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        if type(self.son4) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()
        if type(self.son5) == type(tuple()):
            son6 = self.son6[0].traducir()
        else:
            son6 = self.son6.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        return id

class Instructions10(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class Instructions11(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class Instructions12(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class Instructions13(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

        # if str(type(self.son4)) == "<type 'tuple'>":
        if type(self.son4) == type(tuple()):
            # print "entro tupla"
            self.son4[0].imprimir(" " + ident)
        # elif str(type(self.son4)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son4.imprimir(" " + ident)
        # if str(type(self.son5)) == "<type 'tuple'>":
        if type(self.son5) == type(tuple()):
            # print "entro tupla"
            self.son5[0].imprimir(" " + ident)
        # elif str(type(self.son5)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son5.imprimir(" " + ident)
        if type(self.son6) == type(tuple()):
            # print "entro tupla"
            self.son6[0].imprimir(" " + ident)
        # elif str(type(self.son6)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son6.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son3) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        if type(self.son4) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()
        if type(self.son5) == type(tuple()):
            son6 = self.son6[0].traducir()
        else:
            son6 = self.son6.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        return id

class Instructions14(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class Instructions15(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

        # if str(type(self.son4)) == "<type 'tuple'>":
        if type(self.son4) == type(tuple()):
            # print "entro tupla"
            self.son4[0].imprimir(" " + ident)
        # elif str(type(self.son4)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son4.imprimir(" " + ident)
        # if str(type(self.son5)) == "<type 'tuple'>":
        if type(self.son5) == type(tuple()):
            # print "entro tupla"
            self.son5[0].imprimir(" " + ident)
        # elif str(type(self.son5)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son5.imprimir(" " + ident)
        if type(self.son6) == type(tuple()):
            # print "entro tupla"
            self.son6[0].imprimir(" " + ident)
        # elif str(type(self.son6)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son6.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son3) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        if type(self.son4) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()
        if type(self.son5) == type(tuple()):
            son6 = self.son6[0].traducir()
        else:
            son6 = self.son6.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        return id

class Instructions16(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class InstructionsEmpty(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class AlterBody(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class DataType1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class DataType2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Value1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Value2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Value3(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Value4(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, son8, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

        # if str(type(self.son4)) == "<type 'tuple'>":
        if type(self.son4) == type(tuple()):
            # print "entro tupla"
            self.son4[0].imprimir(" " + ident)
        # elif str(type(self.son4)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son4.imprimir(" " + ident)
        # if str(type(self.son5)) == "<type 'tuple'>":
        if type(self.son5) == type(tuple()):
            # print "entro tupla"
            self.son5[0].imprimir(" " + ident)
        # elif str(type(self.son5)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son5.imprimir(" " + ident)
        if type(self.son6) == type(tuple()):
            # print "entro tupla"
            self.son6[0].imprimir(" " + ident)
        # elif str(type(self.son6)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son6.imprimir(" " + ident)
        if type(self.son7) == type(tuple()):
            # print "entro tupla"
            self.son7[0].imprimir(" " + ident)
        # elif str(type(self.son7)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son7.imprimir(" " + ident)
        if type(self.son8) == type(tuple()):
            # print "entro tupla"
            self.son8[0].imprimir(" " + ident)
        # elif str(type(self.son8)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son8.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son3) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        if type(self.son4) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()
        if type(self.son5) == type(tuple()):
            son6 = self.son6[0].traducir()
        else:
            son6 = self.son6.traducir()
        if type(self.son6) == type(tuple()):
            son7 = self.son7[0].traducir()
        else:
            son7 = self.son7.traducir()
        if type(self.son7) == type(tuple()):
            son8 = self.son8[0].traducir()
        else:
            son8 = self.son8.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        txt += id + " -> " + son7 + "\n\t"
        txt += id + " -> " + son8 + "\n\t"

        return id

class Operator1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Operator2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Operator3(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Operator4(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Comparator1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Comparator2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Comparator3(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Comparator4(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Comparator5(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Comparator6(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Position1(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Position2(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Position3(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Position4(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class RepeatInstructions(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class UntilBody(Node):
    def __init__(self, son1, son2, son3, son4, son5, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

        # if str(type(self.son4)) == "<type 'tuple'>":
        if type(self.son4) == type(tuple()):
            # print "entro tupla"
            self.son4[0].imprimir(" " + ident)
        # elif str(type(self.son4)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son4.imprimir(" " + ident)
        # if str(type(self.son5)) == "<type 'tuple'>":
        if type(self.son5) == type(tuple()):
            # print "entro tupla"
            self.son5[0].imprimir(" " + ident)
        # elif str(type(self.son5)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son5.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son3) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        if type(self.son4) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        return id

class WhileBody(Node):
    def __init__(self, son1, son2, son3, son4, son5, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

        # if str(type(self.son4)) == "<type 'tuple'>":
        if type(self.son4) == type(tuple()):
            # print "entro tupla"
            self.son4[0].imprimir(" " + ident)
        # elif str(type(self.son4)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son4.imprimir(" " + ident)
        # if str(type(self.son5)) == "<type 'tuple'>":
        if type(self.son5) == type(tuple()):
            # print "entro tupla"
            self.son5[0].imprimir(" " + ident)
        # elif str(type(self.son5)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son5.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son3) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        if type(self.son4) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        return id

class CaseBody1(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, son8, son9, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8
        self.son9 = son9

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

        # if str(type(self.son4)) == "<type 'tuple'>":
        if type(self.son4) == type(tuple()):
            # print "entro tupla"
            self.son4[0].imprimir(" " + ident)
        # elif str(type(self.son4)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son4.imprimir(" " + ident)
        # if str(type(self.son5)) == "<type 'tuple'>":
        if type(self.son5) == type(tuple()):
            # print "entro tupla"
            self.son5[0].imprimir(" " + ident)
        # elif str(type(self.son5)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son5.imprimir(" " + ident)
        if type(self.son6) == type(tuple()):
            # print "entro tupla"
            self.son6[0].imprimir(" " + ident)
        # elif str(type(self.son6)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son6.imprimir(" " + ident)
        if type(self.son7) == type(tuple()):
            # print "entro tupla"
            self.son7[0].imprimir(" " + ident)
        # elif str(type(self.son7)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son7.imprimir(" " + ident)
        if type(self.son8) == type(tuple()):
            # print "entro tupla"
            self.son8[0].imprimir(" " + ident)
        # elif str(type(self.son8)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son8.imprimir(" " + ident)
        if type(self.son9) == type(tuple()):
            # print "entro tupla"
            self.son9[0].imprimir(" " + ident)
        # elif str(type(self.son9)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son9.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son3) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        if type(self.son4) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()
        if type(self.son5) == type(tuple()):
            son6 = self.son6[0].traducir()
        else:
            son6 = self.son6.traducir()
        if type(self.son6) == type(tuple()):
            son7 = self.son7[0].traducir()
        else:
            son7 = self.son7.traducir()
        if type(self.son7) == type(tuple()):
            son8 = self.son8[0].traducir()
        else:
            son8 = self.son8.traducir()
        if type(self.son8) == type(tuple()):
            son9 = self.son9[0].traducir()
        else:
            son9 = self.son9.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        txt += id + " -> " + son7 + "\n\t"
        txt += id + " -> " + son8 + "\n\t"
        txt += id + " -> " + son9 + "\n\t"

        return id

class CaseBody2(Node):
    def __init__(self, son1, son2, son3, son4, son5, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

        # if str(type(self.son4)) == "<type 'tuple'>":
        if type(self.son4) == type(tuple()):
            # print "entro tupla"
            self.son4[0].imprimir(" " + ident)
        # elif str(type(self.son4)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son4.imprimir(" " + ident)
        # if str(type(self.son5)) == "<type 'tuple'>":
        if type(self.son5) == type(tuple()):
            # print "entro tupla"
            self.son5[0].imprimir(" " + ident)
        # elif str(type(self.son5)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son5.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son3) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        if type(self.son4) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        return id

class CaseBody3(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class InnerCaseBody1(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

        # if str(type(self.son4)) == "<type 'tuple'>":
        if type(self.son4) == type(tuple()):
            # print "entro tupla"
            self.son4[0].imprimir(" " + ident)
        # elif str(type(self.son4)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son4.imprimir(" " + ident)
        # if str(type(self.son5)) == "<type 'tuple'>":
        if type(self.son5) == type(tuple()):
            # print "entro tupla"
            self.son5[0].imprimir(" " + ident)
        # elif str(type(self.son5)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son5.imprimir(" " + ident)
        if type(self.son6) == type(tuple()):
            # print "entro tupla"
            self.son6[0].imprimir(" " + ident)
        # elif str(type(self.son6)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son6.imprimir(" " + ident)
        if type(self.son7) == type(tuple()):
            # print "entro tupla"
            self.son7[0].imprimir(" " + ident)
        # elif str(type(self.son7)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son7.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son3) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        if type(self.son4) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()
        if type(self.son5) == type(tuple()):
            son6 = self.son6[0].traducir()
        else:
            son6 = self.son6.traducir()
        if type(self.son6) == type(tuple()):
            son7 = self.son7[0].traducir()
        else:
            son7 = self.son7.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        txt += id + " -> " + son7 + "\n\t"

        return id

class InnerCaseBody2(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

        # if str(type(self.son4)) == "<type 'tuple'>":
        if type(self.son4) == type(tuple()):
            # print "entro tupla"
            self.son4[0].imprimir(" " + ident)
        # elif str(type(self.son4)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son4.imprimir(" " + ident)
        # if str(type(self.son5)) == "<type 'tuple'>":
        if type(self.son5) == type(tuple()):
            # print "entro tupla"
            self.son5[0].imprimir(" " + ident)
        # elif str(type(self.son5)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son5.imprimir(" " + ident)
        if type(self.son6) == type(tuple()):
            # print "entro tupla"
            self.son6[0].imprimir(" " + ident)
        # elif str(type(self.son6)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son6.imprimir(" " + ident)
        if type(self.son7) == type(tuple()):
            # print "entro tupla"
            self.son7[0].imprimir(" " + ident)
        # elif str(type(self.son7)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son7.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son3) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        if type(self.son4) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()
        if type(self.son5) == type(tuple()):
            son6 = self.son6[0].traducir()
        else:
            son6 = self.son6.traducir()
        if type(self.son6) == type(tuple()):
            son7 = self.son7[0].traducir()
        else:
            son7 = self.son7.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        txt += id + " -> " + son7 + "\n\t"

        return id

class InnerCaseBody3(Node):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

        # if str(type(self.son4)) == "<type 'tuple'>":
        if type(self.son4) == type(tuple()):
            # print "entro tupla"
            self.son4[0].imprimir(" " + ident)
        # elif str(type(self.son4)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son4.imprimir(" " + ident)
        # if str(type(self.son5)) == "<type 'tuple'>":
        if type(self.son5) == type(tuple()):
            # print "entro tupla"
            self.son5[0].imprimir(" " + ident)
        # elif str(type(self.son5)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son5.imprimir(" " + ident)
        if type(self.son6) == type(tuple()):
            # print "entro tupla"
            self.son6[0].imprimir(" " + ident)
        # elif str(type(self.son6)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son6.imprimir(" " + ident)
        if type(self.son7) == type(tuple()):
            # print "entro tupla"
            self.son7[0].imprimir(" " + ident)
        # elif str(type(self.son7)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son7.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son3) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()
        if type(self.son4) == type(tuple()):
            son5 = self.son5[0].traducir()
        else:
            son5 = self.son5.traducir()
        if type(self.son5) == type(tuple()):
            son6 = self.son6[0].traducir()
        else:
            son6 = self.son6.traducir()
        if type(self.son6) == type(tuple()):
            son7 = self.son7[0].traducir()
        else:
            son7 = self.son7.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"
        txt += id + " -> " + son5 + "\n\t"
        txt += id + " -> " + son6 + "\n\t"
        txt += id + " -> " + son7 + "\n\t"

        return id

class InnerCaseBodyEmpty(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

class Condition1(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class Condition2(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class Condition3(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class Condition4(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class Condition5(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Condition6(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class Condition7(Node):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()
        son1 = self.son1.traducir()
        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        return id

class IsTrue(Node):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

        # if str(type(self.son4)) == "<type 'tuple'>":
        if type(self.son4) == type(tuple()):
            # print "entro tupla"
            self.son4[0].imprimir(" " + ident)
        # elif str(type(self.son4)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son4.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        if type(self.son3) == type(tuple()):
            son4 = self.son4[0].traducir()
        else:
            son4 = self.son4.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

        return id

class PrintValues1(Node):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = update_id()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class PrintValues2(Node):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print "entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son1.imprimir(" " + ident)

        # if str(type(self.son2)) == "<type 'tuple'>":
        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)
        # elif str(type(self.son2)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son2.imprimir(" " + ident)

        # if str(type(self.son3)) == "<type 'tuple'>":
        if type(self.son3) == type(tuple()):
            # print "entro tupla"
            self.son3[0].imprimir(" " + ident)
        # elif str(type(self.son3)) == "<type 'instance'>":
        else:
            # print "entro instance"
            self.son3.imprimir(" " + ident)

    def traducir(self):
        global txt
        id = update_id()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        if type(self.son2) == type(tuple()):
            son2 = self.son2[0].traducir()
        else:
            son2 = self.son2.traducir()

        if type(self.son3) == type(tuple()):
            son3 = self.son3[0].traducir()
        else:
            son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class PrintValuesEmpty(Node):
    def __init__(self, name):
        self.name = name

    def print_op(self):
        pass

    def translate(self):
        global txt
        id = update_id()
        return id

##class Empty(Node):
