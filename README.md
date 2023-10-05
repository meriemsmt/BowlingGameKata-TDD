# Bowling Game Kata en utilisant le TDD (Test Driven Development) sur Python

[![Fr](https://img.shields.io/badge/lang-fr-fr)](https://github.com/meriemsmt/BowlingGameKata-TDD/blob/main/README.md)
[![En](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/meriemsmt/BowlingGameKata-TDD/blob/main/README.en.md)

Le TDD (développement piloté par les tests) est une bonne pratique pour écrire du code de test avant le code de production. 
Cela comprend la répétition d'un cycle d'écriture d'un code de test qui échoue, le développement d'un code de production qui réussit le test et une refactorisation des deux côtés.

En utilisant Git&GitHub pour surveiller les modifications de code lors des commits, ce tutoriel présente une version Python de l'exemple de jeu de bowling étape par étape.

## Problème
Voici un exemple de tableau de scores d’un joueur de bowling :

| Case | 1st | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th | 9th | 10th |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Lancers | 1 &nbsp;&nbsp; 4 | 4 &nbsp;&nbsp; 5 | 6 &nbsp;&nbsp; / | 5 &nbsp;&nbsp; / | ✕ | 0 &nbsp;&nbsp; 1 | 7 &nbsp;&nbsp; / | 6 &nbsp;&nbsp; / | ✕ | 2 &nbsp;&nbsp; / &nbsp;&nbsp; 6 |
|Score| 5 | 14 | 29 | 49 | 60 | 61 | 77 | 97 | 117 | **133** |

Les règles du jeu sont :
>Le jeu se compose de 10 cases comme indiqué ci-dessus. Dans chaque case, le joueur a deux chances de faire tomber 10 quilles. Le score de la case est le nombre total de quilles renversées, plus les bonus des Strikes et des Spares.
>
>Un Spare , c'est lorsque le joueur fait tomber les 10 quilles en deux essais. Le bonus pour cette case est le nombre de quilles renversées au prochain lancer. Par exemple, pour la case 3 ci-dessus, le score est de 10 (le nombre total de quilles renversées) plus un bonus de 5 (le nombre de quilles renversées au prochain lancer.)
>
>Un strike, c'est lorsque le joueur fait tomber les 10 quilles lors de son premier essai. Le bonus pour cette case est la valeur des deux prochaines boules lancées.
>
>Pour la dixième case, un joueur qui lance un spare ou un strike est autorisé à lancer les balles supplémentaires pour terminer la case. Cependant, pas plus de trois balles peuvent être lancées dans la dixième case.

Le défi consiste à développer une classe permettant de calculer le score final obtenu dans un jeu de bowling grâce à TDD qui conduit à des tests approfondis et à un code propre. La classe *Game* résultante doit avoir deux méthodes :

- *Roll :* Utilisé pour renvoyer le nombre de quilles tombées à chaque lancé.
- *Score :* Utilisé à la fin de la partie pour obtenir le score final.

​## Solution
Voici le cycle d'un TDD:
![alt text](https://github.com/meriemsmt/BowlingGameKata-TDD/blob/main/TDDWorkflow.png)

1. [![Badge générique](https://img.shields.io/badge/⎍-Test-red.svg)](https://shields.io/)
    Écrire un test qui implique une des logiques du programme. Cela devrait commencer par la logique la plus simple et passer à des logiques légèrement plus compliquées lors des prochains tours. Puisqu'il n'y a pas de code de production pour la fonctionnalité à ce moment-là, elle devrait **échouer**.
2. [![Badge générique](https://img.shields.io/badge/⎍-Code-brightgreen.svg)](https://shields.io/)
    Pour écrire la quantité minimale de code de production juste pour **réussir** le test unitaire défaillant, mais pas plus loin.
3. [![Badge générique](https://img.shields.io/badge/⎍-Refactor-blue.svg)](https://shields.io/)
    Restructurer à la fois le code de test et le code de production en codes propres.

La solution se trouve sur les deux fichiers *test_bowling.py* et *bowling.py*, où le premier contient le code de test et le second le code de production. Pour voir le développement, veuillez accéder à la section **commits**, à partir du commit "1st Test - Scoring Zeros" jusqu'à "Final Refactoring".
