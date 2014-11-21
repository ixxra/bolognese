
var ixxPlayerControls = function() {
	return {
		restrict: 'E',
		scope: {
			player: '=player'
		},
		templateUrl: '/app/templates/directives/ixxPlayerControls.tpl.html'
	};
};


angular.module('library.directives', [])
	.directive('ixxPlayerControls', ixxPlayerControls);