(function() {
    angular
        .module('pbApp.employees.directives')
        .directive('employeeDetail', EmployeeDetail);

    function EmployeeDetail() {
        return {
            restrict: 'AE',
            templateUrl: 'employees/templates/employee-detail.html',
            scope: {
                employee: "=employee"
            }
        }
    }

})();
