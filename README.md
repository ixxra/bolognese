#About

This is a midnight project I'm working on. It aims to be a media server working as a backend for another project of mine: a couchdb based media library.

##Requirements

A lot of ;) ... since it is not intended for production:

* Gstreamer
* Vala
* libgee
* python3
* virtualenv
* pip
 
##What is in here

*requirements.txt*  contains the needed python packages. In the *src* folder there's mixed code:

* src/server.py: is a python server using *bottle*.
* src/app: contains an angularjs app to interact with the server.
* src/vala: contains a media player daemon.

The idea is to start the media daemon as a separated process, and interact with it by means of dbus. Therefore, the client/http-server job is to send commands to the media daemon.


##This is a mess

Yes! I know that!, but this is only for entertainment, not intended for production. If you have any questions, feel free to contact me.
