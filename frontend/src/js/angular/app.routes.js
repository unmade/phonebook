(function() {
    'use strict';

    angular
        .module('pbApp.routes')
        .config(['$routeProvider', function($routeProvider) {
            $routeProvider.
                when('/employees', {
                    templateUrl: '/static/partials/employees/employees-list.html',
                    controller: 'EmployeesListCtrl',
                    controllerAs: 'ctrl'
                })
                .otherwise({
                    redirectTo: '/employees'
                })
            }
        ]);
})();
