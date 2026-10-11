#in questo file definisco la classe dello STRUMENTO MUSICALE

class Strumento:
    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        self.codice_strumento = codice
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore
        self.prestato = False

    def __repr__(self):
        return f"{self.codice_strumento} {self.tipo} {self.marca} {self.anno_acquisto} {self.valore} - Prestito: {self.prestato}"


