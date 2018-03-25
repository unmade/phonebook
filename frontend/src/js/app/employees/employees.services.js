(function() {
    'use strict';

    angular
        .module('pbApp.employees')
        .factory('employeeService', employeeService)
        .factory('employeeSuggest', employeeSuggest);

    employeeService.$inject = ['$resource'];

    function employeeService($resource) {
        return $resource('employees/api/employee/:id', {}, {
            query: {method: 'GET', isArray: false}
        });
    };

    employeeSuggest.$inject = ['$resource'];

    function employeeSuggest($resource) {
        return $resource('search/api/suggests/', {}, {
            query: {method: 'GET', isArray: true}
        })
    }

})();
