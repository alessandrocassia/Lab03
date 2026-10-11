from csv import reader
from strumento import Strumento
from operator import attrgetter
from prestito import Prestito

class DepositoStrumenti:
    def __init__(self, nome_deposito, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome_deposito = nome_deposito
        self.__responsabile = responsabile
        self.dizionario_strumenti = dict()
        self.dizionario_prestiti = dict()

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
                file = reader(csvfile)
                for line in file:
                    codice_strumento = line[0]
                    tipo = line[1]
                    marca = line[2]
                    anno_acquisto = int(line[3])
                    valore = float(line[4])

                    s = Strumento(codice_strumento, tipo, marca, anno_acquisto, valore) #creo l'oggetto strumento con i dati del file

                    self.dizionario_strumenti[codice_strumento] = s #aggiungo l'oggetto strumento al dizionario del deposito
                    #print(s)

        except FileNotFoundError: #nel caso in cui il nome del file fosse sbagliato sollevo un'eccezione
            raise FileNotFoundError("non è stato possibile aprire il file")

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        numero_ultimo_codice = len(self.dizionario_strumenti)
        nuovo_codice = f"S{numero_ultimo_codice + 1}"

        strumento_nuovo = Strumento(nuovo_codice, tipo, marca, anno_acquisto, valore)
        self.dizionario_strumenti[nuovo_codice] = strumento_nuovo
        return strumento_nuovo

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        lista_strumenti = self.dizionario_strumenti.values()
        lista_ordinata = sorted(lista_strumenti, key = attrgetter("marca"))

        return lista_ordinata

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        if id_strumento not in self.dizionario_strumenti:
            raise Exception("lo strumento non è ancora presente nel nostro deposito")

        strumento_corrente = self.dizionario_strumenti[id_strumento]

        if strumento_corrente.prestato: #verifico se lo strumento è già stato dato in prestito
            raise Exception("lo strumento è già stato prestato e al momento non è disponibile")

        numero_ultimo_prestito = len(self.dizionario_prestiti)
        nuovo_codice_prestito = f"P{numero_ultimo_prestito +1}"
        prestito = Prestito(nuovo_codice_prestito, data, id_strumento, cognome_allievo)
        self.dizionario_strumenti[id_strumento].prestato = True

        return prestito


    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
