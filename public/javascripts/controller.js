var app = angular.module('controller', ['ngRoute']);

app.config(function($routeProvider){
	$routeProvider

		.when('/', {
			templateUrl: 'index.html',
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
