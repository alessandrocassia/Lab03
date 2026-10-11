class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.__responsabile = responsabile
        self.strumenti_deposito = dict()

    @property
    def responsabile(self):
        return self.__responsabile
    @responsabile.setter
    def responsabile(self, responsabile):
        self.__responsabile = responsabile


    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            with open(file_path) as csvfile:
                pass

        except FileNotFoundError:
            raise FileNotFoundError("non è stato possibile aprire il file")




    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
