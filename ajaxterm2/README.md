# AjaxTerm2</h1>

## Intro
AjaxTerm2 is a web based terminal application. This program is a fork of ''Ajaxterm''
written by Antony Lesuisse but ported to use 
[Python Paste](http://pythonpaste.org) instead of the orignal qweb framework. 
The original Ajaxterm was inspired by [Anyterm](http://anyterm.org).
(see below for comparison).

AjaxTerm2 written in python (and some AJAX javascript for client side) and
depends only on python2.3 or better, python paste and paste deploy.  It is *very simple to install* on 
Linux, MacOS X, FreeBSD, Solaris, cygwin and any other Unix that runs Python.  

The AjaxTerm2 port was created my Matthew R. Laue (email: matt AT akirisolutions.com), Dual License: GPL and commercial.

The original Ajaxterm was written by Antony Lesuisse (email: al AT udev.org), License Public
Domain.

---

## Changes
 * 2013-07-05: v1.0 fork from original ajaxterm and port to python paste.
 * 2013-07-02: v1.1 add argument passing via the query string for custom commands.

---

## Download and Install

To run the current development version of AjaxTerm2:

### zip:

    wget https://github.com/mattlaue/ajaxterm2/archive/master.zip
    unzip master.zip
    cd ajaxterm2-master
    ./ajaxterm2

### pip and virtualenv:

    mkdir ajaxterm2
    cd ajaxterm2
    virtualenv --no-site-packages .
    source bin/activate
    pip install https://github.com/mattlaue/ajaxterm2/tarball/master
    python -m ajaxterm2 development.ini

Then point your browser to this URL : http://localhost:8022

---

## Screenshot

<img src="https://www.akirisolutions.com/images/ajaxterm2.png" 
     alt="ajaxterm screenshot" width="256" height="192"/>

---

## Notes and Caveats
 * AjaxTerm2 depends on the key-handling support of the parent browser.
   Certain browser don't propogate all key events to Javascript - 
   e.g. older versions of Chrome use backspace to navigate to the previous
   page in the web history and no key event is generated.

 * If run as root AjaxTerm2 will run /bin/login, otherwise it will run ssh
   localhost. To specify a particular command, use the 'cmd' option in the 
   'DEFAULT' section of the INI file.

 * If you get the error 'OSError: out of pty devices', then the current user
   likely doesn't have permission to access /dev/ptmx (the error message is
   misleading).  Try adding yourself to the relevant group, e.g.:
    sudo usermod -a -G tty $USER

 * AjaxTerm2 only listens on 127.0.0.1:8022 when using the default 
   ajaxterm2.ini configuration file. For remote access, it is
   strongly recommended to use '''https SSL/TLS'''.  Secure transport is easy
   configure if you use the apache web server and mod_proxy.

   Using ssl will also speed up ajaxterm (probably because of keepalive).
   
   Here is an example configuration file:
   
   <pre>
    Listen 443
    NameVirtualHost *:443
    
    &lt;VirtualHost *:&gt;
       ServerName localhost
       SSLEngine On
       SSLCertificateKeyFile ssl/apache.pem
       SSLCertificateFile ssl/apache.pem

       ProxyRequests Off
       &lt;Proxy *&gt;
               Order deny,allow
               Allow from all
       &lt;/Proxy&gt;
       ProxyPass /ajaxterm/ http://localhost:8022/
       ProxyPassReverse /ajaxterm/ http://localhost:8022/
    &lt;/VirtualHost&gt;
   </pre>

 * Using GET HTTP request seems to speed up ajaxterm, just click on GET in the
   interface, but be warned that your keystrokes might be loggued (by apache or
   any proxy). I usually enable it after the login.

 * Parameters can be passed to the terminal command using the query string of the 
   application.  For example, assuming the custom command is ''cmd'' is specified 
   in the INI file, then ''?foo=baz&47&i=10'' becomes:

   <pre>
    cmd --foo baz 47 -i 10
   </pre>
   
   For security reasons, requests containing characters that the underlying shell would interpret are rejected.

 * Comparison to __anyterm__:
   * There are no partial updates, ajaxterm updates either all the screen or
     nothing. That make the code simpler and I also think it's faster. HTTP
     replies are always gzencoded. When used in 80x25 mode, almost all of
     them are below the 1500 bytes (size of an ethernet frame) and we just
     replace the screen with the reply (no javascript string handling).
   * Ajaxterm polls the server for updates with an exponentially growing
     timeout when the screen hasn't changed. The timeout is also resetted as
     soon as a key is pressed. Anyterm blocks on a pending request and use a
     parallel connection for keypresses. The anyterm approch is better
     when there aren't any keypress.

 * Comparison to the original __ajaxterm__:
   * Uses python paste as a webserver instead of qweb with the associated
     directory layout.
   * Configuration is via an INI file instead of using command line options.
   * Uses utf8 by default instead of latin1 for character encoding.
   * Improved key handling for modern web browsers (client-side).
   * Dual licensed: GPL and commercial.

 * AjaxTerm2 contains a copy of [Sarissa](http://sarissa.sourceforge.net/doc)
   which is covered under the LGPL license.  See the header of '/js/sarissa.js'
   for licensing details.

 * Commercial support for AjaxTerm2 is available from Akiri Solutions, Inc. 
   http://www.akirisolutions.com.

---
