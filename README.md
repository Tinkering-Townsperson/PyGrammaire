# PyGrammaire

 Faisons de la grammaire! Les règles et les exceptions de la langue française, en forme de code!

*Read the [English Version](README.en.md)*

## L'Usage

```py
import pyfr.sujet as sujet
import pyfr.verbes.indicatif as indicatif

aller = indicatif.Présent("aller")

print("Je" + aller.conj(sujet.JE))
```
