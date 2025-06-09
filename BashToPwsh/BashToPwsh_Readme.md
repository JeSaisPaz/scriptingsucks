## Convertisseur de scripts Bash vers PowerShell

Ce script Python convertit un fichier Bash (`.sh`) en un script PowerShell (`.ps1`). Il prend en charge des commandes simples, supprime la ligne shebang `#!/bin/bash`, et remplace les variables Bash par l'équivalent PowerShell.

---

## Dépendances

Aucune dépendance externe.

Ce script fonctionne avec **Python 3** uniquement.

---

## Installation de Python 3 (si nécessaire)

```bash
sudo apt update
sudo apt install python3
```


## Commande pour la conversion

python3 bash_to_ps1.py exemple_script.sh exemple_script.ps1

## Limitations

Le convertisseur ne gère pas encore les éléments suivants :

    Fonctions Bash (function nom())

    Tubes (|), redirections (>, >>, 2>&1)

    Subshells ou commandes imbriquées ($(...))

    Commandes avancées (grep, awk, etc.)