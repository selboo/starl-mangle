// multiple function event handler
function EventHandler() { };

// adds a given function as a handler for an event
EventHandler.add = function (er, fx) {
	var eh = eval(er);
	if (typeof eh == "function") { // not first handler
		eval(er + " = function(event) { eh(event); fx(event);}");  
	} else { // first handler
		eval(er + " = fx;");
	}
}

// executes the passed function at and only at the next occurrence of the event
EventHandler.addOnce = function(er, fx) {
	var eh = eval(er);
	if (typeof eh == "function") {
		eval(er + " = function(event) { eh(event); eval('" + er + " = function(event) { eh(event); }'); fx(event)}");
	} else {
		eval(er + " = function(event) { eval('" + er + " = function(event) { }'); fx(event); }");
	}
}