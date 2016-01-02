(function () {
    'use strict';
    
    angular
        .module('pbApp.employees', [
            'pbApp.employees.controllers',
            'pbApp.employees.services',
            'pbApp.employees.directives'
        ]);

    angular.module('pbApp.employees.controllers', []);
    angular.module('pbApp.employees.directives', []);
    angular.module('pbApp.employees.services', ['ngResource']);

})();
