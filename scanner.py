import requests
import json
import argparse
import os
from dotenv import load_dotenv

# Charger les secrets du fichier .env
load_dotenv()

# 1. Configuration des arguments du terminal
parser = argparse.ArgumentParser(description="Scanner Threat Intel via AbuseIPDB")
parser.add_argument("ip", help="L'adresse IP suspecte à analyser")
args = parser.parse_args()

# 2. Configuration de l'API sécurisée
API_KEY = os.getenv('API_KEY')
IP_A_TESTER = args.ip

if not API_KEY:
    print("[-] ERREUR : Clé API introuvable. Vérifiez votre fichier .env")
    exit() 

# 3. Préparation de la requête
url = 'https://api.abuseipdb.com/api/v2/check'
headers = {
    'Accept': 'application/json',
    'Key': API_KEY
}
params = {
    'ipAddress': IP_A_TESTER,
    'maxAgeInDays': '90'
}

# 4. Lancement du scan
print(f"[*] Analyse de l'IP {IP_A_TESTER} en cours...")
reponse = requests.get(url, headers=headers, params=params)

# 5. Traitement et affichage du tableau de bord
if reponse.status_code == 200:
    donnees = reponse.json()
    info = donnees['data'] # On rentre dans la boîte principale

    # Extraction chirurgicale des variables
    ip = info['ipAddress']
    score = info['abuseConfidenceScore']
    pays = info['countryCode']
    fai = info['isp']
    domaine = info['domain']
    signalements = info['totalReports']

    # Affichage du rapport propre
    print("\n" + "="*50)
    print(" 🛡️  RAPPORT D'ANALYSE DE MENACE (THREAT INTEL) ")
    print("="*50)
    print(f" [>] Cible       : {ip}")
    print(f" [>] Pays        : {pays}")
    print(f" [>] Opérateur   : {fai} ({domaine})")
    print(f" [>] Dangerosité : {score}/100")
    print(f" [>] Historique  : {signalements} signalement(s) récent(s)")
    print("="*50 + "\n")
    
else:
    print(f"[-] Erreur de connexion. Code : {reponse.status_code}")