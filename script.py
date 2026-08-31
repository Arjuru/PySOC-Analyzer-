import requests

url = input("entrer votre URL : ")

code = requests.get(url)

if code.status_code == 200:
    print("cible accessible")
elif code.status_code == 404:
    print("alerte d'accès")

logs = [
    "2026-08-30;192.168.1.10;LOGIN_OK",
    "2026-08-30;10.0.0.5;LOGIN_FAIL",
    "2026-08-30;192.168.1.10;LOGIN_OK"
]

toutes_les_ips = []

for log in logs:
    extraire = log.split(";")
    toutes_les_ips.append(extraire[1])

ip_uniques = set(toutes_les_ips)

def detecter_suspect(ip):
    if ip.startswith("10.") or ip.startswith("172."):
        return True
    else:
        return False

# Exemple de test sur une IP de l'ensemble
for ip in ip_uniques:
    statut = detecter_suspect(ip)
    print("IP :", ip, "- Suspect :", statut)

bilan = {"cible": url, "statut_http": code.status_code, "total_ips": len(ip_uniques)}

print("Analyste :", bilan.get("analyste", "Admin-SOC"))
print("Bilan complet :", bilan)
