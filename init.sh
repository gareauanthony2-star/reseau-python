#!/bin/bash
# dit au système d'exécuter ce fichier aec Bash

mkdir -p models
# mettre en place le dossier models / -p évite l'erreur si ce dossier existe

touch README.md .gitignore main.py
touch models/__init__.py models/machine.py models/switch.py
touch models/router.py modesl/worstation.py models/server.py models/wireless.py
# touch = mettre en place des fichiers vides (sans toucher les existants)

[ -f README.md ] && [ ! -s README.MD ] && echo "#Topologie réseau en Python" > README
#n'écrit le titre que si README.md est vide (pour ne pas écraser mon texte)

cat > .gitignore << 'EOF'
__pycache__/
*.pyc
.venv/
.vscode/
EOF
# écrit la liste des éléments que GIT ignore

if [ ! -d ".git" ]; then
git init # met en place le dépôt s'in n'existe pas
git config user.name "Anthony"
git config user.email "gareauanthony2@gmail.com"
git remote add origin git@gitlab.com:gareauanthony2-star/mon-site-web.git
fi
# [ ! -d ".git" ] = "si le dossier .git n'existe pas"

git add . # prépare tous les fichiers
git commit -m "Initialisation du projet" # enregistre une version
git branch -M main # nomme la branche "main"
git push -u origin main # envoie sur gitlab  