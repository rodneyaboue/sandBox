import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# Données
left_vehicles = [
    "J10XA053339", "J11MA096782", "J11MA096875", "J11MA096879", "J10XA053161", "J10XC002374",
    "J11MA096895", "J11MA096914", "J10XA053122", "J11MA096932", "J10XA053486", "J11MA096991",
    "J11MA096961", "J11MA096986", "J10XA053493", "J11MC011802", "J10XA053491", "J11MA096964",
    "J11MA096983", "J11MA097005", "J11MA097060", "J10XA053529", "J10XA053538", "J11MA097045",
    "J10XA053545", "J11MA097023", "J10XA053591", "J10XA053560", "J10XA053573", "J11MA097077",
    "J10XA053614", "J11MA097122", "J11MC011840", "J11MA097086", "J11MA097138", "J11MA097145",
    "J11MA097080", "J10XA053616", "J11MA097162", "J11MA097160", "J11MA097158", "J10XA053638",
    "J11MJ005133", "J11MA097150", "J11MC011862", "J10XA053716", "J11MA097195", "J10XA053735",
    "J10XA053724", "J11MA097218", "J11MA097214", "J10XA053727", "J11MA097220", "J10XA053768",
    "J11MM008700", "J10XA053684", "J11MA097217", "J11MA097253", "J10XA053789", "J10XA053824",
    "J10XA053760", "J10XA053841", "J11MA097259", "J10XA053842", "J11MC011900", "J10XA053877",
    "J10XA053881", "J11MA097317", "J10XA053953", "J10XA053904", "J11MA097328", "J10XA053973",
    "J11MA097321", "J10XA054009", "J11MA097312", "J10XA054010", "J10XA054016", "J11MA097368",
    "J30CA008865", "J10XC002414", "J10XA054063", "J10XA054083", "J10XA054112", "J10XA054116",
    "J11MC011931", "J11MA097384", "J10XA054081", "J10XA054140", "J11MC011933", "J11MA097391",
    "J10XA054137", "J10XA054197", "J10XA054181", "J11MA097416", "J10XA054210", "J10XA054221",
    "J11MA097426", "J11MA097432", "J10XC002421", "J11MA097438", "J10XA054255", "J11MC011946",
    "J10XA054296", "J10XA054300", "J10XA054332", "J10XA054382", "J10XA054358", "J10XA054390",
    "J10XM002678", "J10XA054362", "J10XA054413", "J11MC011991", "J11MC011989", "J10XA054430",
    "J10XA054433", "J10XA054455", "J10XA054442", "J10XA054440", "J10XA054439", "J30CA008880",
    "J10XA054464", "J10XA054072", "J10XA054477", "J10XA054497", "J10XA054493", "J10XD000905",
    "J10XA054516", "J10XA054495", "J10XA054541", "J10XA054524", "J11MC012002", "J11MA097611",
    "J10XA054513", "J10XA054161", "J10XA054531", "J11MC012012", "J10XA054558", "J10XA054217",
    "J11MA097657", "J10XA054216", "J10XA054580", "J10XJ000746", "J11MA097716", "J10XC002452",
    "J10XA054697", "J11MA097807", "J11MA097784", "J10XA054690", "J11MA097825", "J10XA054711",
    "J10XA054716"
]


right_vehicles = [
    "J10XA053364", "J11MA096851", "J10XA053487", "J30CS011875", "J11MM008693", "J30CM006906",
    "J11MA097185", "J10XM002659", "J10XA053846", "J11MJ005136", "J30CA008858", "J30CR000979",
    "J30CM006921", "J31KP002497", "J31KP002502", "J11MA097366", "J30CS011965", "J10XA054099",
    "J10XA054143", "J11MA097417", "J11MJ005150", "J11MA097415", "J10XA054239", "J11MM008729",
    "J10XA054279", "J10XD000903", "J10XM002669", "J11MJ005154", "J10XM002676", "J11MA097352",
    "J11MA097505", "J10XM002680", "J10XM002682", "J10XM002683", "J31KP002530", "J10XA054504",
    "J10XA054505", "J11MA097615", "J11MA097616", "J31KP002558", "J10XA054367", "J10XA054350",
    "J31KP002562", "J10XA054595", "J31KP002566", "J31KP002568", "J10XA054603", "J31KP002573",
    "J31KP002569", "J31KP002571", "J10XM002687", "J31KP002578", "J11MA097794", "J11MA097802",
    "J10XA054613", "J10XA054721", "J10XA054681"
]


# Fonction pour extraire le jeu de véhicules (les 5 premiers caractères)
def extract_gamme_codes(vehicles):
    return [vehicle[:5] for vehicle in vehicles]

# Extraction des jeux de véhicules
gammes_left = extract_gamme_codes(left_vehicles)
gammes_right = extract_gamme_codes(right_vehicles)

# Comptage des véhicules par jeu
count_left = Counter(gammes_left)
count_right = Counter(gammes_right)

# Combinaison des jeux de véhicules pour l'axe X
all_gammes = sorted(set(count_left.keys()).union(set(count_right.keys())))

# Compte des véhicules pour chaque jeu de véhicules
count_left_combined = [count_left.get(gamme, 0) for gamme in all_gammes]
count_right_combined = [count_right.get(gamme, 0) for gamme in all_gammes]

# Création du graphique
fig, ax = plt.subplots(figsize=(12, 8))

# Position des barres
bar_width = 0.35
index = np.arange(len(all_gammes))

# Barres pour la liste gauche
bars_left = ax.bar(index - bar_width/2, count_left_combined, bar_width, label='gauche', color='blue')

# Barres pour la liste droite
bars_right = ax.bar(index + bar_width/2, count_right_combined, bar_width, label='droite', color='green')

# Ajout des labels et titres
ax.set_xlabel('Gamme de Véhicules')
ax.set_ylabel('Nombre de Véhicules')
ax.set_title('Nombre de Véhicules par gamme et Durée de Gavage')
ax.set_xticks(index)
ax.set_xticklabels(all_gammes, rotation=45, ha='right')
ax.legend()

# Affichage
plt.tight_layout()
plt.show()
