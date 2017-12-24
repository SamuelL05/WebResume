var app = angular.module('controller', ['ngRoute']);

app.config(function($routeProvider){
	$routeProvider

		.when('/', {
			templateUrl: 'main.html',
			//controller: 'main'
		})

		.when('/education', {
			templateUrl: 'education.html',
			//controller: 'education'
		})

		.when('/software', {
			templateUrl: 'software.html',
			//controller: 'software'
        })
        
        .when('/employment', {
			templateUrl: 'employment.html',
			//controller: 'employment'
		});
});

/*
app.controller('main', function($rootScope) {
	$rootScope.education = false;
	$rootScope.software = false;
	$rootScope.employment = false;
});

app.controller('education', function($rootScope) {
	$rootScope.education = true;
	$rootScope.software = false;
	$rootScope.employment = false;
});

app.controller('software', function($rootScope) {
	$rootScope.education = false;
	$rootScope.software = true;
	$rootScope.employment = false;
});

app.controller('employment', function($rootScope) {
	$rootScope.education = false;
	$rootScope.software = false;
	$rootScope.employment = true;
});
*/