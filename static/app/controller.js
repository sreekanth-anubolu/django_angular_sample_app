(function(){

angular.module('dashboard.controllers')
  .controller('dashboardCtrl', dashboardCtrl)
  .controller('sendMailCtrl', sendMailCtrl);

function dashboardCtrl($scope, dashboard, _){

    var self = this;

    function init(){
      self.data = [];
      self.params = {};
      self.filters = {};
      initialzeFilters();
    }

    init();
    
    function initialzeFilters(){
      self.filters.problem = {};
      self.problemOptions = ["Not Recognized", "Unknown", "Combo Error", "Mapped", "Spelling Error", "Not in DB"]
      self.filters.date = {};
      self.dateOptions = ["Today", "Yesterday"]
      self.filters.state = {};
      self.stateOptions = ["Open", "Closed"]
    }

    $scope.$watchCollection(function(){
      return self.filters.problem;
    }, getData);

    $scope.$watchCollection(function(){
      return self.filters.date;
    }, getData);

    $scope.$watchCollection(function(){
      return self.filters.state;
    }, getData);

    function getData(){

      var probFilter = getProbTypes();
      if(probFilter.length > 0){
        self.params.problem = probFilter.join(",");
      }else{self.params.problem = null}

      var dayFilter = getDayTypes();
      if(dayFilter.length > 0){
        self.params.date = dayFilter.join(",");
      }else{self.params.date = null}

      var stateFilter = getStateTypes();
      if(stateFilter.length > 0){
        self.params.status = stateFilter.join(",");
      }else{self.params.status = null}

      dashboard.query(self.params).$promise.then(function(res){
        if(res.success){
          $scope.suggestions = res.data;
        }
      });
    }

    function getProbTypes(){
      var keys = [];
      _.each(self.filters.problem, function( val, key ) {
        if(val){ keys.push(key); }
      });
      return keys;
    }

    function getDayTypes(){
      var keys = [];
      _.each(self.filters.date, function( val, key ) {
        if(val){ keys.push(key); }
      });
      return keys;
    }

    function getStateTypes(){
      var keys = [];
      _.each(self.filters.state, function( val, key ) {
        if(val){ keys.push(key); }
      });
      return keys;
    }
}

function sendMailCtrl($scope, $filter, $window, $controller, Mail, $timeout){

    var self = this;

    self.locals = {
      type: "sendMail",
      controller: self,
      sendMailCtrl: self,
    };

    function initialize(){
      self.mail = {};
      self.showAlert = false;
    }

    initialize();

    function create(name, ctrl, extraLocals) {
      self[name] = self.locals[name] = $controller(ctrl,
        _.extend({ $scope: $scope.$new() }, _.defaults(extraLocals || {}, self.locals)));
    }

    function wrapUp(){
        self.alert = { type: 'success', msg: 'Mail successfully sent.' };
        self.showAlert = true;
        self.mail = {};
    }

    self.sendMail = function(smCtrl, id){
      self.mail.csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
      Mail.update({'id' : id, 'type' : 'mail'}, self.mail).$promise.then(function(res){
        if(res.success){
          wrapUp();
          $timeout(function(){
            smCtrl.scope.data['email_status'] = true;
            smCtrl.cancel();
          }, 3000);
        } else {
          console.log(res.errors);
        }
      });
    }
  };

})();
