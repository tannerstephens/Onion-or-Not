var chal = {};

function getChal()
{
	var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "/oon/endpoint/", false );
    xmlHttp.send( null );
    chal = JSON.parse(xmlHttp.responseText);
}

function setHeadline()
{
	getChal();
	var h = document.getElementById("hl");
	h.innerHTML = chal['headline'];
}

function check(button)
{
	var ans = document.getElementById("ans");
	if (button === chal.onion) {
		ans.style.color = "green";
		ans.innerHTML = "Correct!"
	} else {
		ans.style.color = "red";
		ans.innerHTML = "Incorrect."
	}
	setHeadline();
}