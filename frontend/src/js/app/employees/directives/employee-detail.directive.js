(function() {
    'use strict';

    angular
        .module('pbApp.employees')
        .directive('employeeDetail', EmployeeDetail);

    function EmployeeDetail() {
        return {
            restrict: 'AE',
            templateUrl: 'directives/employee-detail.directive.html',
            scope: {
                employee: "=employee"
            }
        }
    }

})();
