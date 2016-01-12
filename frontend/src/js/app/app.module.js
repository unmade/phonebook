(function() {

    'use strict';
    angular
        .module('pbApp', [
            'ngRoute',
            'ngResource',
            'ngMaterial',
            'infinite-scroll',
            'pbApp.routes',
            'pbApp.employees',
            'pbApp.companies',
            'pbApp.feedback'
        ]);

    angular.module('pbApp.routes', []);
})();
