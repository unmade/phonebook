(function() {
    'use strict';

    angular
        .module('pbApp.routes')
        .config(['$routeProvider', function($routeProvider) {
            $routeProvider.
                when('/employees', {
                    templateUrl: '/static/partials/employees/employee-list.html',
                    controller: 'EmployeeListCtrl',
                    controllerAs: 'ctrl'
                })
                .otherwise({
                    redirectTo: '/employees'
                })
            }
        ]);
})();
