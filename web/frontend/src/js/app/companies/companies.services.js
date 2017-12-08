(function() {
    'use strict';

    angular
        .module('pbApp.companies')
        .factory('companyService', ['$resource', companyService])
        .factory('centerService', ['$resource', centerService])
        .factory('divisionService', ['$resource', divisionService]);

    companyService.$inject = ['$resourse'];
    centerService.$inject = ['$resourse'];
    divisionService.$inject = ['$resourse'];

    function companyService($resource) {
        return $resource('api/companies/company/:id', {} , {
            query: {method: 'GET', isArray: false}
        });
    }

    function centerService($resource) {
        return $resource('api/companies/center/:id', {} , {
            query: {method: 'GET', isArray: false}
        });
    }

    function divisionService($resource) {
        return $resource('api/companies/division/:id', {} , {
            query: {method: 'GET', isArray: false}
        });
    }

})();
