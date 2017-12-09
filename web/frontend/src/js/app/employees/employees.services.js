(function() {
    'use strict';

    angular
        .module('pbApp.employees')
        .factory('employeeService', employeeService);

    employeeService.$inject = ['$resource'];

    function employeeService($resource) {
        return $resource('employees/api/employee/:id', {}, {
            query: {method: 'GET', isArray: false}
        });
    };

})();
