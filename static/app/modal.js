(function(){

angular.module('dashboard.directives')
  .directive('myModal', smModal);

angular.module('dashboard.controllers')
  .controller('smModalCtrl', smModalCtrl);

    //directive
    function smModal($uibModal) {
        return {

            transclude: true,
            restrict: 'EA',
            template: '<a ng-click="open()" ng-transclude>Open</a>',
            scope: {
                //controller: "@",
                //controllerAs: "@",
                name: "@",
                size: "@",
                scope: "=scope",
                body: "@",
                bodyClass: "@",
                //ctrl: "=ctrl",
                data: "="
            },
            link: function(scope, element, attrs) {
                scope.open = function() {
                    var modalInstance = $uibModal.open({
                        animation: true,
                        templateUrl: attrs.template ? attrs.template : false,
                        controller: 'smModalCtrl',
                        controllerAs: 'smCtrl',
                        size: attrs.size ? attrs.size : 'sm', //lg - sm - md
                        windowClass: attrs.windowClass ? attrs.windowClass : 'angular-my-modal-window',
                        backdrop: attrs.backdrop ? attrs.backdrop : true,
                        keyboard: false,
                        resolve: {
                            modalScope: function() {
                                return scope;
                            }
                        }

                    });

                    modalInstance.result.then(function() {
                        //console.debug('success');
                    }, function() {
                        //console.debug('error');
                    });
                };
            }
        };
    }

    //directive controller
    function smModalCtrl($scope, $rootScope, $uibModalInstance, modalScope) {
        var that = this;

        that.scope = modalScope;
        that.accept = accept;
        that.cancel = cancel;

        // callback trigger //

        function accept(e) {
            $uibModalInstance.close();
            $rootScope.$emit('smModalAccepted', e);
            if (e) e.stopPropagation();
        };

        function cancel(e) {
            $uibModalInstance.dismiss('cancel');
            $rootScope.$emit('smModalCanceled', e);
            if (e) e.stopPropagation();
        };

        // event trigger //

        $rootScope.$on('smModalAccept', function() {
            accept();
        });
        $rootScope.$on('smModalCancel', function() {
            cancel();
        });
    }

})();