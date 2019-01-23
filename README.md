# Simple-HTTP-Proxy
A very basic implementation of the HTTP-Proxy server

This is a very simple terminal based HTTP-Proxy test server which is developed mostly for the terminal based clients who use netcat or any other similar tools to access proxies.

***Python Version Required:*** 3.6.7

***Required Modules:***
  1. socket
  2. re
  3. requests
  
***Usage:***
  * Run the port-80-listner.py on the machine which you would like to use as a web server
  * Run the http-proxy.py on the machine which is dedicated for the proxy.
  * Use netcat,ncat or any similar tools to access the proxy and tunnel through it to connect to the web server
  
**** Warning: Never run this program on production environment as this program is in the test phase ****
