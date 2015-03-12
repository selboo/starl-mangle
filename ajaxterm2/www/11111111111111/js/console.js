var serverregex = new RegExp("^([a-zA-Z0-9_\\-]+\\.)*[a-zA-Z0-9_\\-]+$");

function execute() {
	// read values
	var server = document.getElementById("console.server").value;
	var user = document.getElementById("console.user").value;
	var port = document.getElementById("console.port").value;
	var pk = document.getElementById("console.pk") ? document.getElementById("console.pk").value : null;
	// do checks
	if (!server || !serverregex.test(server))
		alert("Please enter a valid server address.");
	else if (!Validation.isInteger(port))
		alert("Port has to be an integer value.");
	else if (!user)
		alert("Please enter a valid SSH user name.");
	else if (!termsAccepted())
		alert("ATTENTION: The consoleFISH is a backup tool for system administrators who are aware of the risks associated with the use of web based SSH clients. If you do not accept our terms and conditions as well as the provided notes on security you can not (and should not) proceed. Thanks for your understanding.");
		//alert("In order to continue you have to accept our terms & conditions.");
	else openConsoleWindow(server, user, port, pk);
}

function openConsoleWindow(server, user, port, pk) {
	var url = "ajaxterm.html?ip=" + server + "&user=" + user + "&port=" + port;
	if (pk) url = url + "&pk=" + escape(pk).replace(new RegExp("\\+","g"), "%2B");
	if (ServerSettings.HTTPS_ROOT) url = ServerSettings.HTTPS_ROOT + "/console/" + url;
	window.open(url, "console", "width=648,height=436,status=0");
}

function openTransferWindow(server, user, port) {
    var url = "transfer.jsp?ip=" + server + "&user=" + user + "&port=" + port;
    window.open(url, "console.transfer", "width=340,height=240,status=0");
}

function purchaseKey() {
	var email = document.getElementById("console.email").value.trim();
	var pass = document.getElementById("console.pass").value;
	var pass2 = document.getElementById("console.pass2").value;
	var select = document.getElementById("console.product");
	var product = select.options[select.selectedIndex].value;
	if (!Validation.isEmail(email)) 
		alert("Please provide a valid E-Mail address.");
	else if (pass.length < 4)
		alert("Password must be at least four characters long.");
	else if (pass != pass2)
		alert("Passwords do not match.");
	else if (!termsAccepted())
		alert("In order to continue you have to accept our terms & conditions.");
	else {
		var msg = AJAX.get("../root/servlet/method/com.serverside.fish.console.Interface.registerKey?product=" + product + "&email=" + escape(email) + "&pass=" + escape(pass));
		var ex = msg.split(" ");
		if (ex.length == 2 && ex[0] == "OK" && ex[1] && ex[1] != "null") {
			document.location.href = ex[1];
		} else alert(msg);
	}
}

function termsAccepted() {
	var cb = document.getElementById("console.terms");
	return cb.checked;
}

function init() {
	if (document.getElementById("console.server"))
		document.getElementById("console.server").focus();
}

EventHandler.add("window.onload", init);
