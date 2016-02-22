(function() {
    'use strict';

    angular
        .module('pbApp.companies')
        .controller('CompanyListCtrl', CompanyListCtrl);

    CompanyListCtrl.$inject = ['$q', '$filter', '$mdSidenav', 'Scroll', 'companyService'];

    function CompanyListCtrl($q, $filter, $mdSidenav, Scroll, companyService) {
        var self = this;

        self.companies = new Scroll(companyService, {limit: 40, offset: 0});

        self.companySearch = companySearch;
        self.closeCompanyDetail = closeCompanyDetail;
        self.openCompanyDetail = openCompanyDetail;

        function companySearch(query) {
            var limit = 4;
            if (!query) return self.companies.results.slice(0, limit);
            var deferred = $q.defer(),
                translated = $filter('englishCharsToRussian')(query);
            companyService.query({
                search: translated,
                limit: limit,
                offset: 0
            }, function(results, status) {
                deferred.resolve(results.results)
            });

            return deferred.promise
        }

        function closeCompanyDetail() {
            $mdSidenav('company-detail-right').close();
        }

        function openCompanyDetail(company) {
            if (!company) return;
            self.company = company;
            $mdSidenav('company-detail-right').toggle();
        }
    }
})();
