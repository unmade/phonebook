(function() {
    'use strict';

    angular
        .module('pbApp.routes')
        .config(config);

    config.$inject = ['$routeProvider'];

    function config($routeProvider) {
        $routeProvider.
            when('/employees', {
                templateUrl: '/static/partials/employees/employee-list.html',
                controller: 'EmployeeListCtrl',
                controllerAs: 'ctrl'
            }).
            when('/feedback', {
                templateUrl: '/static/partials/feedbacks.html',
                controller: 'FeedbackListCtrl',
                controllerAs: 'ctrl'
            }).
            otherwise({
                redirectTo: '/employees'
            })
    };
})();
