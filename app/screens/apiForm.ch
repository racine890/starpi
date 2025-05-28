Buttons.nb: 4
Button1: Save
Button1.id: 0
0.x: 300
0.y: 750
0.w: 200
0.h: 50
0.link: app/scripts/saveResponse.gcs

Button2: Back
Button2.id: 1
1.x: 700
1.y: 750
1.link: app/screens/main.ch

Button3: Remove
Button3.id: 9
9.x: 750
9.y: 400
9.link: app/scripts/removeResponse.gcs

Button4: Add
Button4.id: 13
13.x: 1110
13.y: 600
13.link: app/scripts/addResponse.gcs

Text.nb: 6
Text1: API Name
Text1.id: 2
2.x: 200
2.y: 100

Text2: URL Format
Text2.id: 3
3.x: 200
3.y: 150

Text3: Response Type
Text3.id: 4
4.x: 200
4.y: 250

Text4: Responses
Text4.id: 5
5.x: 200
5.y: 400

Text5: http://localhost:1901/
Text5.id: 10
10.x: 425
10.y: 150

Text6: Methode
Text6.id: 11
11.x: 200
11.y: 200

Input.nb: 3
Input1.id: 6
6.x: 575
6.y: 105

Input2.id: 7
7.x: 575
7.y: 155

Input3.id: 12
Input3: GET
12.x: 575
12.y: 200

Edit.nb: 1
Edit1.id: 8
8.x: 600
8.y: 600
8.w: 800
8.h: 200

Button.width: 200
Button.size: 50
Button.foreground: #ECAA34
Button.background: #0D0600
Entry.width: 300

OnDisplay: app/scripts/displayFields.gcs

[events]
Button-1: @[end]
[/events]