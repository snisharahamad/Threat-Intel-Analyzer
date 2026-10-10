# Threat Intel IP Scanner

Petit utilitaire CLI en Python pour vérifier rapidement la réputation d'une adresse IP. 

À l'origine, j'ai codé ce script pour automatiser l'analyse des IP qui frappaient mon honeypot local (que je ne pouvais pas exposer proprement à cause du CGNAT de mon routeur). Le script tape sur l'API d'AbuseIPDB et parse la réponse JSON pour extraire uniquement la data tactique, directement dans le terminal.

## Stack 
- **Python 3** (librairie `requests`)
- **uv** pour la gestion de l'environnement virtuel et des dépendances
- **python-dotenv** pour la gestion sécurisée de la clé API

## Setup

**1. Récupérer le projet**
```bash
git clone [https://github.com/snisharahamad/Threat-Intel-Analyzer.git](https://github.com/snisharahamad/Threat-Intel-Analyzer.git)
cd Threat-Intel-Analyzer
uv sync
```

**2. Configuration**
Créer un fichier `.env` à la racine du projet pour y glisser la clé API AbuseIPDB. Le fichier est ignoré par Git via le `.gitignore` pour éviter toute fuite.
```text
API_KEY="ta_cle_api_ici"
```

## Utilisation

Il suffit de passer l'IP suspecte en argument :
```bash
uv run scanner.py 118.25.6.39
```