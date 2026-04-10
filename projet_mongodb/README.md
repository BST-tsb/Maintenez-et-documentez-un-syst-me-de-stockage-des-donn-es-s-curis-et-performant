\# 🏥 Migration de données médicales vers MongoDB



\## 📌 Contexte



Dans le cadre d’un projet Data Engineering, l’objectif est de migrer un dataset médical au format CSV vers une base de données NoSQL MongoDB afin d’améliorer la scalabilité et la gestion des données.



\---



\## ⚙️ Technologies utilisées



\- Python

\- MongoDB

\- Pandas

\- PyMongo

\- Docker



\---



\## 📂 Structure du projet

projet\_mongodb/

├── healthcare\_dataset.csv

├── explore.py

├── migration.py

├── test\_data.py

├── crud\_test.py

├── requirements.txt

├── docker-compose.yml

├── README.md





\---



\## 🔍 Analyse des données



\- Dataset de \*\*55 500 lignes\*\*

\- \*\*Aucune valeur manquante\*\*

\- Types de données cohérents

\- Présence de doublons



\---



\## 🧹 Nettoyage des données



\- Suppression des doublons

\- Conversion des dates (`Date of Admission`, `Discharge Date`) en datetime



Après nettoyage :

➡️ \*\*54 966 enregistrements\*\*



\---



\## 🗄️ Modélisation MongoDB



\- \*\*Base de données\*\* : `healthcare\_db`

\- \*\*Collection\*\* : `patients`



Chaque ligne du dataset est convertie en \*\*document JSON\*\*



\---



\## 🔄 Processus de migration



1\. Chargement du fichier CSV avec Pandas

2\. Nettoyage des données

3\. Transformation en dictionnaire

4\. Insertion dans MongoDB via PyMongo



\---



\## ▶️ Exécution



Lancer la migration :



```bash

python migration.py

