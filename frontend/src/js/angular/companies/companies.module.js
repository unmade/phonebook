(function () {
    'use strict';

    angular
        .module('pbApp.companies', [
            'pbApp.companies.services'
        ]);

    angular.module('pbApp.companies.services', ['ngResource']);
})();
