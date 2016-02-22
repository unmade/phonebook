(function() {
    'use strict';

    angular
        .module('pbApp.employees')
        .controller('EmployeeListCtrl',  EmployeeListCtrl);

    EmployeeListCtrl.$inject = ['$q', '$filter', '$mdSidenav', 'employeeService', 'Scroll',
                                'companyService', 'centerService', 'divisionService'];

    function EmployeeListCtrl($q, $filter, $mdSidenav, employeeService, Scroll,
                              companyService, centerService, divisionService) {
        var self = this;

        self.employees = new Scroll(employeeService);
        self.companies = null;
        self.centers = null;
        self.divisions = null;
        self.selectedCompany = null;
        self.selectedCenter = null;
        self.selectedDivision = null;

        self.companyChanged = companyChanged;
        self.centerChanged = centerChanged;
        self.closeEmployeeDetail = closeEmployeeDetail;
        self.divisionChanged = divisionChanged;
        self.employeeSearch = employeeSearch;
        self.loadCompanies = loadCompanies;
        self.loadCenters = loadCenters;
        self.loadDivisions = loadDivisions;
        self.openEmployeeDetail = openEmployeeDetail;
        self.search = search;

        function companyChanged() {
            self.selectedCenter = null;
            self.selectedDivision = null;
            self.employees = new Scroll(employeeService, {
                company: self.selectedCompany,
                search: self.searchText || null
            });
            self.employees.nextPage();
        }

        function centerChanged() {
            self.selectedDivision = null;
            self.employees = new Scroll(employeeService, {
                company: self.selectedCompany,
                center: self.selectedCenter,
                search: self.searchText || null
            });
            self.employees.nextPage();
        }

        function closeEmployeeDetail() {
            $mdSidenav('employee-detail-right').close();
        }

        function divisionChanged() {
            self.employees = new Scroll(employeeService, {
                company: self.selectedCompany,
                center: self.selectedCenter,
                division: self.selectedDivision,
                search: self.searchText || null
            });
            self.employees.nextPage();
        }

        function employeeSearch(query) {
            var limit = 8;
            if (!query) return self.employees.results.slice(0, limit);
            var deferred = $q.defer(),
                translated = $filter('englishCharsToRussian')(query);
            employeeService.query({
                search: translated,
                limit: limit,
                offset: 0
            }, function(results, status) {
                deferred.resolve(results.results)
            });

            return deferred.promise
        }

        function loadCompanies() {
            return self.companies || companyService.query(function(data) {
                self.companies = data;
            });
        }

        function loadCenters() {
            if (self.centers && self.centers.results.length
                 && self.centers.results[0].company == self.selectedCompany) return;
            return centerService.query({company: self.selectedCompany}, function(data) {
                self.centers = data;
            });
        }

        function loadDivisions() {
            if (self.divisions && self.divisions.results.length
                 && self.divisions.results[0].center == self.selectedCenter) return;
            return divisionService.query({center: self.selectedCenter}, function(data) {
                self.divisions = data;
            });
        }

        function openEmployeeDetail(employee) {
            if (!employee) return;
            self.employee = employee;
            $mdSidenav('employee-detail-right').toggle();
        }

        function search(query) {
            self.selectedCompany = null;
            self.selectedCenter = null;
            self.selectedDivision = null;
            self.employees = new Scroll(employeeService, {search: query});
            self.employees.nextPage();
        }
    }
})();
