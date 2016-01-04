(function() {
    'use strict';

    angular
        .module('pbApp.employees.directives')
        .directive('employeeListItem', EmployeeListItem);

    function EmployeeListItem() {
        return {
            restrict: 'AE',
            templateUrl: 'employees/directives/templates/employee-list-item.html',
            scope: {
                'employee': '=employee'
            }
        }
    }
})();
