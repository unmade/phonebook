(function() {
    'use strict';
    angular
        .module('pbApp.employees.directives')
        .directive('employeesListItem', EmployeesListItem);

    function EmployeesListItem() {
        return {
            restrict: 'AE',
            templateUrl: 'employees/directives/templates/employees-list-item.html',
            scope: {
                'employee': '=employee'
            }
        }
    }
})();
