# Ecran expliquant comment utiliser Starpi.
# Une capture d'écran, avec des flèches,
# Un bouton suivant pour afficher la suite des instructions,
# Un bouton J'ai compris pour valider et commencer à utiliser Starpi.

Edit.nb: 1
Edit1.id: 0
0.x: 600
0.y: 750
0.w: 800
0.h: 100

Buttons.nb: 1
Button1: Next
Button1.id: 1
1.x: 1100
1.y: 750
1.link: app/scripts/nextOrEnd.gcs

Button.foreground: #ECAA34
Button.background: #0D0600
Button.width: 200
Button.size: 50

Onload: @[SetVar *current_pic 1]
OnDisplay: app/scripts/displayHowTo.gcs

[events]
Control-r: @[reset]
[/events]