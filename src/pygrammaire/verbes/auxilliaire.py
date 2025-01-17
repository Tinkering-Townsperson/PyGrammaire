ÊTRE_LIST = [
	"descendre",
	"retourner",

	"monter",
	"rester",
	"sortir",

	"venir",
	"aller",
	"naître",
	"devenir",
	"entrer",
	"rentrer",
	"tomber",
	"revenir",
	"arriver",
	"mourir",
	"partir"
]

# TODO: Implementer la prefixe "re" sur quelques verbes (renaître, remonter, etc.)


def get_aux(verbe):
	if verbe.startswith("se ") or verbe in ÊTRE_LIST:
		return "être"
	else:
		return "avoir"
