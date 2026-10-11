class Prestito:
    def __init__(self, codice_prestito, data, id_strumento, cognome_allievo):
        self.codice_prestito = codice_prestito
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo

    def __repr__(self):
        return f"{self.codice_prestito} {self.data} {self.id_strumento} {self.cognome_allievo}"