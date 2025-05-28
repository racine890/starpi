[1]
Welcome to Starpi V2 !
This is a Moc, a tool for developpers that can help replace a distant server while programming using APIS. Front-end devs can use it to simulate backend data while backend developper can use it to simulate external resource when it's unaivalable
( eg : You have to use a payment api for your app but it's not available right now, then you can use Starpi to fake it ).
The advantages of using starpi instead of in-code moc is that it stays and is managed externally, to provide a better simulation.
Starpi uses its own server too, which allows to serve responses for multiple users on the same network. Starpi will just answer as long as the query matches the endpoint, which means that it will not check any security header.
That means that you don't have to change anything to your code but the base endpoint url, and it's all working!
NB: Please, Starpi responses are public, so don't use any private or sensitive data there!
[/1]

[2]
Creating APIS :
	Your apis are displayed in a Notebook. The red carret next to the API name marks its status. You can add an api by clicking on the (+) icon.
	Each api has multiple responses, displayed down at the right. You can select a specific response to see it in the edit.
Serving Responses :
	Before serving anything, you should start the server. First of all, click on the green start icon to start the server. You can stop it later by using the red carret icon to stop it when desired.
	Just notice you can't serve any response while the server is closed, and closing the server will unserve all apis.
	Once the server is started, you have to select the desired api, and click on the antena icon next to serve it. Once an api is served, its carret will turn green, and you can select the desired response.
	When the response is served, you can see the url you can use in postman to test it.
Updating apis and responses :
	You can use the save icon to update the current response. The trash icon can be used to delete the selected api, and you can updated with the pencil icon.
[/2]

[3]
In the API creation form, Fill the name, the endpoint (url), the method et select the response type as shown in the pic.
Then, write the first Answer in the edit, and press the "Add" button. The answer will be added to the responses list, so you can do the same thing for other responses.
You can also use the "Remove" button to drop an unwanted response.
Once all your responses are added, you can click on the save button to create the API and use it.
NB: 
	1) In the endpoint, mark your path variables between brackets and starting with a star like this : "/api/endpoint/{*path-variable}"
	2) Your endpoints have to start with either /api or /download
[/3]

[4]
While apis are running, you can use an external tool like your browser or postman to test it. With specific header or not, or whatever your path variables are replaced with,
 you will get the current answer for the specified api.
[/4]