(function(){

angular.module('dashboard', [
  'ngRoute',
  'ngResource',
  'dashboard.controllers',
  'dashboard.services',
  'dashboard.directives',
  'ui.bootstrap',
]);

angular.module('dashboard.controllers', []);
angular.module('dashboard.services', []);
angular.module('dashboard.directives', []);

})();