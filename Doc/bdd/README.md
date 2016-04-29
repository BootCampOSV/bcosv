# Base de données

La base de données agrège la documentation sur OpenOSV en créant des liens entre les éléments et en dotant chaque éléments de propriétés.

+ Structure de la base de donnée

La base de donnée est constituée des quatre tables suivantes :

    + la table **element** :

| nom | type |
| --- | ---- |
| id  | Integer Primary Key |
| nom | Text |

    + la table **heritage** :

| nom | type |
| --- | ---- |
| id  | Integer Primary Key |
| id_element_parent | Integer |
| id_element_enfant | Integer |

    + la table **heritage** :

| nom | type |
| --- | ---- |
| id  | Integer Primary Key |
| nom | Text |
| valeur | Text |

    + la table **propriete_element** :

| nom | type |
| --- | ---- |
| id  | Integer Primary Key |
| id_element | Integer |
| id_propriete | Integer |


+ Méthodes d'accès à la base de donnée
