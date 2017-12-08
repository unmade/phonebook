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
        return $resource('companies/api/company/:id', {} , {
            query: {method: 'GET', isArray: false}
        });
    }

    function centerService($resource) {
        return $resource('companies/api/center/:id', {} , {
            query: {method: 'GET', isArray: false}
        });
    }

    function divisionService($resource) {
        return $resource('companies/api/division/:id', {} , {
            query: {method: 'GET', isArray: false}
        });
    }

})();
