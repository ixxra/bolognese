var Couch = function($resource){
	var Tracks = $resource('/api/v1/tracks', {}, {query: {method: 'GET', isArray: false}});
	return {
		tracks: Tracks 
	};
};

var Player = function(){
	var play = function(){
		console.log('play: click');
	};

	var pause = function(){
		console.log('pause: click');
	};

	var stop = function(){
		console.log('stop: click');
	};
	return {
		play: play,
		pause: pause,
		stop: stop
	};
};


angular.module('library.services', ['ngResource'])
	.service('Couch', ['$resource', Couch])
	.service('Player', Player);