var URL = new Object();

URL.getParameter = function(name) {
    var path=document.location.toString(); 
    var variable = name;
    if (path.indexOf("&" + variable + "=") > -1 || path.indexOf("?" + variable + "=") > -1) {
        if (path.indexOf("&" + variable + "=") > -1)
            variable = "&" + variable;
        else if (path.indexOf("?" + variable + "=") > -1)
            variable = "?" + variable;
        var start = path.indexOf(variable + "=") + variable.length + 1;
        var done = path.indexOf("&", path.indexOf(variable + "=") + 1);
        var end = (done > -1) ? done : path.length;
        return path.substring(start, end);
    }
}