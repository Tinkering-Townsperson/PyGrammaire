from pyfr.verbes import Verbe
from pyfr.verbes.infinitif import Infinitif
from pyfr.sujet import Sujet
from typing import Union


class Présent(Verbe):
	TERMINAISONS = {
		"cer": {
			(1, False): "ce",
			(2, False): "ces",
			(3, False): "ce",
			(1, True): "çons",
			(2, True): "cez",
			(3, True): "cent",
		},
		"ger": {
			(1, False): "ge",
			(2, False): "ges",
			(3, False): "ge",
			(1, True): "geons",
			(2, True): "gez",
			(3, True): "gent",
		},
		"er": {
			(1, False): "e",
			(2, False): "es",
			(3, False): "e",
			(1, True): "ons",
			(2, True): "ez",
			(3, True): "ent",
		},
		"ir": {
			(1, False): "is",
			(2, False): "is",
			(3, False): "it",
			(1, True): "issons",
			(2, True): "issez",
			(3, True): "issent",
		},
		"re": {
			(1, False): "s",
			(2, False): "s",
			(3, False): "t",
			(1, True): "ons",
			(2, True): "ez",
			(3, True): "ent",
		},
		"cevoir": {
			(1, False): "çois",
			(2, False): "çois",
			(3, False): "çoit",
			(1, True): "cevons",
			(2, True): "cevez",
			(3, True): "çoient",
		},
		"enir": {
			(1, False): "iens",
			(2, False): "iens",
			(3, False): "ient",
			(1, True): "enons",
			(2, True): "enez",
			(3, True): "iennent",
		},
		"aître": {
			(1, False): "ais",
			(2, False): "ais",
			(3, False): "aît",
			(1, True): "aissons",
			(2, True): "aissez",
			(3, True): "aissent",
		}
		# TODO: Ajoute tous les exceptions des terminaisons
	}
	EXCEPTIONS = {
		"aller": {
			(1, False): "vais",
			(2, False): "vas",
			(3, False): "va",
			(1, True): "allons",
			(2, True): "allez",
			(3, True): "vont",
		},
		"avoir": {
			(1, False): "ai",
			(2, False): "as",
			(3, False): "a",
			(1, True): "avons",
			(2, True): "avez",
			(3, True): "ont",
		},
		"être": {
			(1, False): "suis",
			(2, False): "es",
			(3, False): "est",
			(1, True): "sommes",
			(2, True): "êtes",
			(3, True): "sont",
		},
		"faire": {
			(1, False): "fais",
			(2, False): "fais",
			(3, False): "fait",
			(1, True): "faisons",
			(2, True): "faites",
			(3, True): "font",
		},
		"devoir": {
			(1, False): "dois",
			(2, False): "dois",
			(3, False): "doit",
			(1, True): "devons",
			(2, True): "devez",
			(3, True): "doivent",
		},
		"pouvoir": {
			(1, False): "peux",
			(2, False): "peux",
			(3, False): "peut",
			(1, True): "pouvons",
			(2, True): "pouvez",
			(3, True): "peuvent",
		},
		"vouloir": {
			(1, False): "veux",
			(2, False): "veux",
			(3, False): "veut",
			(1, True): "voulons",
			(2, True): "voulez",
			(3, True): "veulent",
		},
		"savoir": {
			(1, False): "sais",
			(2, False): "sais",
			(3, False): "sait",
			(1, True): "savons",
			(2, True): "savez",
			(3, True): "savent",
		}
		# TODO: Ajoute tous les exceptions des verbes entières
	}

	def __init__(self, verbe: Union[Infinitif, str]):
		"""Initialise l'instance de la classe Présent.

		Parameters:
		verbe (Union[Infinitif, str]): L'infinitif du verbe ou le verbe sous forme de string
		"""
		super(Présent, self).__init__()
		if verbe is None:
			raise ValueError("Le verbe ne peut pas être \"None\".")
		if not isinstance(verbe, Infinitif):
			verbe = Infinitif(verbe)
		self.infinitif = verbe.infinitif
		self.racine = verbe.racine
		self.terminaison = verbe.terminaison
		self.aux = verbe.aux
		self.groupe = verbe.groupe

	def conj(self, sujet: Sujet) -> str:
		"""Conjugue le verbe au présent de l'indicatif.

		Parameters:
		sujet (Sujet): Le sujet de la conjugaison.

		Returns:
		str: La conjugaison du verbe.
		"""
		if self.infinitif in self.EXCEPTIONS:
			return self.EXCEPTIONS[self.infinitif][(sujet.personne, sujet.pluriel_ou_poli)]

		terminaison = self.TERMINAISONS[self.terminaison][
			(sujet.personne, sujet.pluriel_ou_poli)
		]
		return f"{self.racine}{terminaison}"
