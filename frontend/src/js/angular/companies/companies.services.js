(function() {
    'use strict'
    angular
        .module('pbApp.companies.services')
        .factory('Company', ['$resource', Company])
        .factory('Center', ['$resource', Center])
        .factory('Division', ['$resource', Division]);

    function Company($resource) {
        return $resource('api/companies/:id', {} , {
            query: {method: 'GET', isArray: false}
        });
    }

    function Center($resource) {
        return $resource('api/centers/:id', {} , {
            query: {method: 'GET', isArray: false}
        });
    }

    function Division($resource) {
        return $resource('api/divisions/:id', {} , {
            query: {method: 'GET', isArray: false}
        });
    }

})();
