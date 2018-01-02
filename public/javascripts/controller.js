var app = angular.module('controller', ['ngRoute', 'ngResource']);

app.config(function($routeProvider){
	$routeProvider

		.when('/', {
			templateUrl: 'main.html',
		})

		.when('/education', {
			templateUrl: 'education.html',
		})

		.when('/software', {
			templateUrl: 'software.html',
        })
        
        .when('/employment', {
			templateUrl: 'employment.html',
		});
});
