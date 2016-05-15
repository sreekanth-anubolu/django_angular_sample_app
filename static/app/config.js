(function(){

angular.module('dashboard')
.config(['$routeProvider', function($routeProvider){
  $routeProvider
    .when('/', {
      templateUrl: "/static/partials/dashboard.html",
      controller: "dashboardCtrl",
      controllerAs: "ctrl"
    })
    .otherwise({redirectTo:'/'});
}]);

})();