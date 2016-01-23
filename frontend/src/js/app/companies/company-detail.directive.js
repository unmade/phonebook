(function() {
    'use strict';

    angular
        .module('pbApp.companies')
        .directive('companyDetail', companyDetail);

    function companyDetail() {
        return {
            restrict: 'AE',
            templateUrl: 'company-detail.directive.html',
            scope: {
                company: '=company'
            }
        }
    }
})();
