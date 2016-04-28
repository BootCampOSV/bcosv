HANDrive
========

système de conduite manuelle pour personnes à mobilité réduite 
(n'ayant pas l'usage des jambes/pieds)
accelérateur + frein


contexte : 
----------

Lors de l'open camp OSV, le propriétaire de l'OSVéhicle est une association / collectivité, la voiture est mise en autopartage.

problématique : 
---------------

Lorsqu'une PMR souhaite conduire de façon autonome un véhicule partagé, 
le système de conduite standard n'est pas adapté 
aux conditions nécessaires requises par la personnes (plusieurs cas possible : paraplégique, ou amputé d'un bras gauche, par exemple)

cahier des charges : 
--------------------

- l'utilisateur est propriétaire du système d'accélération / freinage 
(évite les problèmes de dégradations / entretients, et du non investissement d'une collectivité du système d'accéleration pour l'ensemble de la flotte / du parc)

- l'utilisateur apporte avec lui le systeme d'accélération lorsqu'il souhaite utiliser n'importe quel véhicule en autopartage.

- une OSV à un connecteur au niveau du volant (ou du tableau de bord, ou de la proximité de la colonne de direction), qui permet de brancher le système d'accélération

- une OSV à un interrupteur d'activation / désactivation du systeme d'accélération

- on ajoute à une OSV un controleur / calculateur (arduino) pour récupérer l'info d'un potentiomètre et l'envoyer à l'OSV



contraintes/limitations pour CampOSV : 
--------------------------------------

en 3 jours, on se limite à la fabrication du système d'accélération, 
le frein manuel étant puremment mécanique, 
et le matériel disponible pour la fabrication n'etant pas disponible sur l'événement, cette partie sera réporté à un autre moment.
Pour ce qui est de la partie mécanique du systeme d'accélÉration (le cercle en métal),  n'ayant pas sur place le matériel nécessaire à la fabrication, nous nous limitons à la partie électronique


Législation : 
-------------

Pour ce type d'aide technique à la conduite, la PMR doit avoir un permis de conduire adapté à cette aide technique (et donc passer une visite médicale dans une préfecture)
(10 changment de vitesse adapté) <--juridique / tehnique --> (boite automatique)
(20 mécanisme de freinage adapté) <--- juridique / tehnique --> (frein mécanique)
(25 mécanisme acélération adapté) <-- juridique / tehnique --> (accélérateur)

la législation en terme d'homologation du matériel : 
- le frein doit etre mécanique (pas de panne possible pour cet élément de sécurité)
- l'accélérateur doit être mécanique ou électronique, car en cas de panne, le véhicule ralenti tout seul. Il y a une homologation à passer (se renseigner concrètement)




évolution possible : 
--------------------

- faire une poignée de volant / commodo / télécommande , avec des interrupteurs qui commandent les cligniotants, le klaxon, ou d'autres fonctions du véhicule.
