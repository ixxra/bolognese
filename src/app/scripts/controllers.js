var mainCtrl = function(Couch, Player){
	this.tracks = Couch.tracks.query();
	this.player = Player;
};

angular.module('library.controllers', ['library.services'])
	.controller('mainCtrl', ['Couch', 'Player', mainCtrl]);