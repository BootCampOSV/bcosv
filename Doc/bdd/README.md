# Base de données

L'idée est de décrire l'assemblage des pièces du véhicule sous la forme d'un graphe où chaque noeud du graphe représente une pièce ou un assemblage de pièces. Une base de donnée permet de construire ce graph.

## Structure de la base de donnée

La base de donnée est constituée des quatre tables suivantes :

### la table **element** :

| nom | type |
| --- | ---- |
| id  | Integer Primary Key |
| nom | Text |

Chaque objet de cette table décrit un élément (matériel ou non) de la voiture (par exemple une vis, un cable, le chassis ou la voiture elle même).

### la table **heritage** :

Cette table permet d'associer deux éléments en établissant une relation d'héritage entre eux. Par exemple, l'élément *train avant* appartient à l'élément *chassis*. Ainsi un élément permet de désigner un assemblage complexe ou une simple vis et d'orienter le graph.

| nom | type |
| --- | ---- |
| id  | Integer Primary Key |
| id_element_parent | Integer |
| id_element_enfant | Integer |

### la table **propriete** :

Pour décrire un élément du véhicule, il est nécessaire de lui attribuer des propriétes (une couleur, un matériau, un plan de montage, un modèle CAO, un prix, un fournisseur, etc.). Cette table contient ces propriétés.

| nom | type |
| --- | ---- |
| id  | Integer Primary Key |
| nom | Text |
| valeur | Text |

### la table **propriete_element** :

Cette table permet d'associer à un élément une propriété.

| nom | type |
| --- | ---- |
| id  | Integer Primary Key |
| id_element | Integer |
| id_propriete | Integer |


## Méthodes d'accès à la base de donnée

De nombreuses méthodes de traitement de la base doivent être concidérées, par exemple :
+ la création, la modification d'un élément ;
+ l'affichage de l'arbre de construction d'un véhicule ;
+ le chiffrage d'un véhicule ;
+ ...
