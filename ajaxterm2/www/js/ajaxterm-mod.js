var alerts = 0;

var callback;
var captchalayer, captchacontainer;
var oldkeypress, oldkeydown;
var ie = (window.ActiveXObject) ? true : false;

function getCaptchaLayer() {
    if (!captchalayer) captchalayer = document.getElementById("captchalayer");
    return captchalayer;
}

function getCaptchaContainer() {
    if (!captchacontainer) captchacontainer = document.getElementById("captchacontainer");
    return captchacontainer;
}

function keyinfo() {
	opener.location.href = "key.jsp";
	opener.focus();
}

function reactivate(fx) {
	callback = fx;
	showCaptcha();
}

function reactivateSubmitCaptcha() {
	var data = "";
	data = data + "reactivate=true";
	data = data + "&recaptcha_challenge_field=" + Recaptcha.get_challenge();
	data = data + "&recaptcha_response_field=" + Recaptcha.get_response();
	AJAX.post("u.x", data, reactivateDone, 0, true);
}

function reactivateSubmitKey() {
	var data = "";
	data = data + "reactivate=true";
	data = data + "&email=" + document.getElementById("email").value;
	data = data + "&userkey=" + document.getElementById("userkey").value;
	AJAX.post("u.x", data, reactivateDone, 0, true);
}

function reactivateDone(xml) {
	if (xml && xml.documentElement) {
		de=xml.documentElement;
		if(de && de.tagName=="pre") {
			Sarissa.updateContentFromNode(de, document.getElementById("div.dterm"));
		}
		timeout=window.setTimeout(callback, 100);
		// update key handlers
		document.onkeypress = oldkeypress;
		document.onkeydown = oldkeydown;
		// update display
		getCaptchaLayer().style.display = "none";
		getCaptchaContainer().style.display = "none";
	} 
	// keep captcha if something weng wrong
	else showCaptcha();
	// reset text field
	document.getElementById("userkey").value = "";
}

function showCaptcha() {
	// store key handler
	if (typeof document.onkeypress == "function") oldkeypress = document.onkeypress;
	if (typeof document.onkeydown == "function") oldkeydown = document.onkeydown;
	// update key handlers
	document.onkeypress = null;
	document.onkeydown = null;
	// update display
	getCaptchaLayer().style.display = "";
	getCaptchaContainer().style.display = "";
	// update captcha
	Recaptcha.create(ServerSettings.CONSOLE_CAPTCHA_PUBLIC,	"recaptcha", { theme: "red", callback: Recaptcha.focus_response_field });
}

function startTransfer() {
    openTransferWindow(ip, user, port);
}