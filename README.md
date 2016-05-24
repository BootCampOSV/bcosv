# Description 

This repository has been created during the Boot camp OSV from April 27 to 29  2016. 



## Objectifs

+ Capitaliser un maximum d'idées, de contenus, d'outils, de projets, ...., autour de la plateforme Open Source Vehicle
et de son usage possible dans le contexte local Rennais.

+ Disposer d'une base de départ pour aller plus loin (AAP) dans une phase ultérieure.

+ "Have fun together" 

## Règles du jeu 

+ Règle 1 : Le travail réalisé pendant la durée du boot camp est ouvert. 

+ Règle 2 : Les langues de travail sont indifféremment le français ou l'anglais (selon le contexte).

+ Règle 3 : Les projets sont définis après la présentation des règles du jeu.

+ Règle 4 : Chaque projet  dispose d'un répertoire sous de dépôt github (idéalement chaque équipe dispose d'un participant familier de l'utilisation de git, et se charge d'uploader le contenu digital produit (photos de tableaux, croquis, url , code ,....).

+ Règle 5 : Chaque équipe projet organise son répertoire propre selon, ses propres règles, définies collaborativement par les membres de l'équipe. 


## Liens Utiles

[Le Pad du Projet OSV (Trait d'union entre toutes les initiatives en cours ) ](https://annuel.framapad.org/p/osv-rennes)

[Description du Véhicule](http://bootcamposv.github.io/bcosv/)


L'un des résultats du boot camp OSV est l'amorçage du sous-projet OPEP, décrit ci-dessous.
 
# (OPEP project) OSV Parts Editing Project  

### Localisation des fichiers STEP

Les fichiers STEP sont déposés  à cette adresse  :

[Fichiers STEP](https://github.com/BootCampOSV/bcosv/tree/master/Doc/mechanics/stp)

Les fichiers STEP (extension .stp)  sont des fichiers de type texte ( visualisable en ligne sauf quand ils sont trop gros )

Celui ci par exemple :

[rear_frame.stp](https://github.com/BootCampOSV/bcosv/blob/master/Doc/mechanics/stp/rear_frame/rear_frame.stp)

Il est éditable avec [freecad](http://www.freecadweb.org/). 
(La pièce a été renommé , à ce stade c'est sans doute une mauvaise idée pour. Il peut servir d'exemple pour créer tous les autres sur le même principe. 

![rear_frame in freecad](images/freecad1.png)_

## Comment participer à l'OPEP ?

1. Sous Windows installer git pour windows
    Sous linux : sudo apt-get install git
2. Se créer un compte github
3. Forker le répertoire bcosv sur son compte github 
4. Cloner le répertoire 
    git clone https://github.com/BootCampOSV/bcosv.git
5. Editer `ma_nouvelle_piece.stp`
6. Quand  le fichier est éditable sous [freecad](http://www.freecadweb.org/)
    - git add ma_nouvelle piece.stp 
    - git commit -a - m "Ajout de ma_nouvelle_piece.stp bla bla"
    - git push origin master 
7. Sur son compte github faire un pull request pour demander l'intégration de sa pièce dans le projet

## Travail à faire    
     
 + **Milestone 1** (Achieved 4%) : 
  Tout le fichier STEP du chassis OSV est découpé en blocs élémentaires. Chaque bloc est renommé avec une nomenclature approprié (à débattre)
  et organisé hiérarchiquement et fonctionnellement vis à vis des autres blocs système. La structure de graphe du châssis est dégagée (liens d'appartenance à un bloc et liens fonctionnels entre blocs).        
 + **Milestone 2**(Achieved 0%): Les pièces du châssis réel non présentes dans le fichier STEP original sont détaillées et ajoutées . Les méta informations sur chaque pièces sont ajoutées. (Fournisseurs, prix, masse, distance aux contraintes d'homologation... )    
 + **Milestone 3**(Achieved 0%): Le châssis complet du véhicule est documenté, dans toute ses parties et consultable en ligne,  y compris le système d'informations, le châssis et la carrosserie.
 + **Milestone 4** (Achieved 0%): Créer des évolutions sous formes de branches git de nouvelles évolutions du véhicule. (Autres motorisations, autres châssis, ajouts de capteurs, systèmes d'aide à la perception et à l'autonomisation....)     
        
# Let's start ...

### Structure d'un fichier

- Le fichier [rear_frame.stp](https://github.com/BootCampOSV/bcosv/blob/master/Doc/mechanics/stp/rear_frame/rear_frame.stp) peut servir d'exemple pour créer tous les autres sur le même principe.


#### Entete

L’entête est de la forme :


	ISO-10303-21;
	HEADER;
	FILE_DESCRIPTION((''),'2;1');
	FILE_NAME('SAVANNAH_STEP_ASM','2015-03-16T',('Roberto'),(''),
	'PRO/ENGINEER BY PARAMETRIC TECHNOLOGY CORPORATION, 2008310',
	'PRO/ENGINEER BY PARAMETRIC TECHNOLOGY CORPORATION, 2008310','');
	FILE_SCHEMA(('CONFIG_CONTROL_DESIGN'));
	ENDSEC;
	DATA;

+ (Note 1 : à terme on pourrait y glisser aussi des infos sur sa license):

+ (Note 2 : Après édition et réenregistrement sous [freecad](http://www.freecadweb.org/) l'entete est un peu modifié. On peut ajjouter le nom de l'éditeur du fichier et la license du fichier. 


#### Clôture du fichier

La clôture du fichier : 
	
    ENDSEC;
    END-ISO-10303-21;


#### Corps ( Ici  est décrit l'essentiel  du travail à faire)

Le corps du fichier se tient entre son entête et sa cloture.
 
Algo pour enrichir la base avec un nouveau fichier stp

+ Créer avec son éditeur de texte préféré le fichier : ma_nouvelle_piece.stp

+ Tant que le nouveau fichier ma_nouvelle_piece.stp fichier n'est pas éditable sous freecad :

  + ajouter de nouveaux blocs de directives prélevées (avec réflexion type SUDOKU) dans

       - https://github.com/BootCampOSV/bcosv/blob/master/Doc/mechanics/stp/tabby2.stp
       Attention : ce n'est plus le fichier original du site OSV

       - Le niveau hiérarchique d'un bloc des pièces est indiquée par son indentation dans le fichier :

        [ListProduct.txt](https://github.com/BootCampOSV/bcosv/blob/master/Doc/mechanics/ListProduct.txt)

  + Si le fichier est éditable sous [freecad](http://www.freecadweb.org/):

    - Bravo, une nouvelle pièce ou bloc qui pourra recevoir des nombreuse informations complémentaires est créée ! 
    - Placer le fichier à sa place dans l'arborescence du véhicule et proposer un pull request  (une nouvelle contribution)
        + Dans peu de temps, la nouvelle pièce sera convertie en html et visualisable sur le web ici
                [mechanics](http://bootcamposv.github.io/bcosv/Doc/mechanics/)
    - Sortir

  + Sinon:
      
      - Regarder ce qui cloche 
      - corriger le problème (Dans 99% des cas, c'est un lien manquant. Chercher ce qui a été oublié dans le gros fichier STEP)


Dans un premier temps, il est préférable de nommer les fichiers avec le nom original du bloc qu'il contient.


A quelques-uns, cela pourrait avancer assez vite. :) 

Vous pouvez bien sûr modifier, compléter et améliorer, traduire, cette documentation pour aider d'autres participants à nous aider. 
