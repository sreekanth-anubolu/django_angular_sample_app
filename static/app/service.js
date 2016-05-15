(function(){

angular.module('dashboard.services')
.factory("dashboard", dashboard)
.factory("_", Underscore)
.factory("Mail", Mail)

function dashboard($resource) {
  return $resource('/api/suggestions', {},{
    query: { 
      isArray: false
    }
  });
}

function Mail($resource) {
  return $resource('/api/suggestion/:id/update', {
    suggestionId: '@_id'
  },{
    update: {
      method: 'PUT'
    },
    query: {
      isArray: false
    }
  });
}

function Underscore() {
  return window._;
}

})();