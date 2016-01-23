(function() {
    'use strict';

    angular
        .module('pbApp.companies')
        .controller('CompanyListCtrl', CompanyListCtrl);

    CompanyListCtrl.$inject = ['$q', '$mdSidenav', 'companyService', 'companyScroll'];

    function CompanyListCtrl($q, $mdSidenav, companyService, companyScroll) {
        var self = this;

        self.companies = new companyScroll({limit: 40, offset: 0});

        self.showCompanyDetail = showCompanyDetail;
        self.companySearch = companySearch;

        function showCompanyDetail(company) {
            if (!company) return;
            self.company = company;
            $mdSidenav('company-detail-right').toggle();
        }

        function companySearch(query) {
            var limit = 4;
            if (!query) return self.companies.results.slice(0, limit);
            var deferred = $q.defer();
            companyService.query({
                search: query,
                limit: limit,
                offset: 0
            }, function(results, status) {
                deferred.resolve(results.results)
            });

            return deferred.promise
        }
    }
})();
