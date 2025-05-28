debug: yes

Background: app/res/bg.png
AppIcon: app/res/start.png

Title: Starpi : Lite Moc Server
Width: 1215
Size: 810

OnDisplay: @[config item 2 font=('Arial', 30, 'bold');end]

Text.nb: 1
Text1: Click anywhere to continue
Text1.id: 0
0.x: 800
0.y: 700

main_text_color: white

[events]
Button-1: app/scripts/firstTimeCheck.gcs
[/events]