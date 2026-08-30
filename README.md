# PySOC-Analyzer 

**PySOC-Analyzer** est un script d'audit et d'analyse de sécurité écrit en Python. Il permet d'évaluer la disponibilité d'une cible Web, de découper et traiter des logs réseau bruts, et de détecter des adresses IP suspectes.

Ce projet synthétise mes compétences d'automatisation Python appliquées à la cybersécurité.

---

## Fonctionnalités

- **Vérification d'état HTTP :** Teste la disponibilité d'un serveur Web via le module `requests`.
- **Parsing de logs bruts :** Extraie les adresses IP d'un journal d'événements texte avec découpage dynamique (`.split()`).
- **Dédoublonnage :** Nettoie automatiquement les doublons d'IP grâce aux ensembles (`set`).
- **Détection de menaces :** Analyse les plages d'adresses IP privées/internes (`10.x.x.x`, `172.x.x.x`) via des fonctions dédiées.
- **Rapport SOC :** Génère un dictionnaire de synthèse récapitulatif avec gestion de clés sécurisée (`.get()`).

---

## Prérequis & Installation

1. Assure-toi d'avoir Python 3 installe.
2. Installe la bibliothèque `requests` :

```bash
pip install requests
