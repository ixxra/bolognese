
var config = function($locationProvider, $routeProvider){
	$locationProvider.html5Mode(false);
	$routeProvider
		.when('/', {
			templateUrl: '/app/templates/main.tpl.html',
			controller: 'mainCtrl',
			controllerAs: 'main'
		});
};

angular.module('library', [
	'ngRoute', 
	'library.controllers', 
	'library.services',
	'library.directives'])
	.config(['$locationProvider', '$routeProvider', config]);