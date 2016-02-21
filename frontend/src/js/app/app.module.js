(function() {

    'use strict';
    angular
        .module('pbApp', [
            'ngRoute',
            'ngResource',
            'ngMaterial',
            'infinite-scroll',
            'pbApp.routes',
            'pbApp.layout',
            'pbApp.employees',
            'pbApp.companies',
            'pbApp.feedback',
            'pbApp.utils'
        ]);

    angular.module('pbApp.routes', []);
})();
