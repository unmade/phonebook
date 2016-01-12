(function() {
    'use strict';

    angular
        .module('pbApp.employees')
        .directive('employeeListItem', EmployeeListItem);

    function EmployeeListItem() {
        return {
            restrict: 'AE',
            templateUrl: 'directives/employee-list-item.directive.html',
            scope: {
                'employee': '=employee'
            }
        }
    }
})();
