var AJAX = new Object();

AJAX.get = 	function get(url, method, ms, xml) {
   	var xmlHttpReq = false;
    var self = this;
    // Mozilla/Safari
   	if (window.XMLHttpRequest)
       	self.xmlHttpReq = new XMLHttpRequest();
    // IE
   	else if (window.ActiveXObject)
       	self.xmlHttpReq = new ActiveXObject("Microsoft.XMLHTTP");
    // timeout
    if (ms > 0) {
	    var onTimeout = function() {
    		self.xmlHttpReq.abort();
	    }
    	var timeout = setTimeoutHelper(onTimeout, ms);
    }
    // AJAX
    if (method != null && typeof(method) == "function") {
	   	self.xmlHttpReq.open('GET', url, true);
    	self.xmlHttpReq.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	   	self.xmlHttpReq.onreadystatechange = function() {
    	   	if (method && self.xmlHttpReq.readyState == 4) {
    	   		if (ms > 0) clearTimeoutHelper(timeout);
        	   	if (xml) method(self.xmlHttpReq.responseXML);
        	   	else method(self.xmlHttpReq.responseText);
        	}
	    }
       	self.xmlHttpReq.send(null); // query string is argument
	} 
	// SJAX
	else {
	   	self.xmlHttpReq.open('GET', url, false);
	   	try {
	       	self.xmlHttpReq.send(null); // query string is argument
   			if (ms > 0) clearTimeoutHelper(timeout);
			return self.xmlHttpReq.responseText;
		} catch(ex) {
			return null;
		}
	}
}

AJAX.post = function get(url, data, method, ms, xml) {
   	var xmlHttpReq = false;
    var self = this;
    // Mozilla/Safari
   	if (window.XMLHttpRequest)
       	self.xmlHttpReq = new XMLHttpRequest();
    // IE
   	else if (window.ActiveXObject)
       	self.xmlHttpReq = new ActiveXObject("Microsoft.XMLHTTP");
    // timeout
    if (ms > 0) {
	    var onTimeout = function() {
    		self.xmlHttpReq.abort();
	    }
    	var timeout = setTimeoutHelper(onTimeout, ms);
    }
    // AJAX
    if (method != null && typeof(method) == "function") {
	   	self.xmlHttpReq.open('POST', url, true);
    	self.xmlHttpReq.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	   	self.xmlHttpReq.onreadystatechange = function() {
    	   	if (method && self.xmlHttpReq.readyState == 4) {
    	   		if (ms > 0) clearTimeoutHelper(timeout);
        	   	if (xml) method(self.xmlHttpReq.responseXML);
        	   	else method(self.xmlHttpReq.responseText);
        	}
	    }
       	self.xmlHttpReq.send(data); // query string is argument
	} 
	// SJAX
	else {
	   	self.xmlHttpReq.open('POST', url, false);
	   	try {
	       	self.xmlHttpReq.send(data); // query string is argument
   			if (ms > 0) clearTimeoutHelper(timeout);
			return self.xmlHttpReq.responseText;
		} catch(ex) {
			return null;
		}
	}
}
