var chal = {};

function getChal()
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            update(xmlHttp.responseText);
    }
    xmlHttp.open("GET", "/oon/endpoint/", true); // true for asynchronous 
    xmlHttp.send(null);
}

function update(json)
{
	chal = JSON.parse(json);
	var h = document.getElementById("hl");
	h.style.color = "black";
	h.innerHTML = chal['headline'];
}

function check(button)
{
	var ans = document.getElementById("hl");
	if (button === chal.onion) {
		ans.style.color = "green";
		ans.innerHTML = "Correct!"
	} else {
		ans.style.color = "red";
		ans.innerHTML = "Incorrect."
	}
	getChal();
}