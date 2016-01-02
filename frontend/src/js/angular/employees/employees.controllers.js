(function() {
    'use strict';
    angular
        .module('pbApp.employees.controllers')
        .controller('EmployeesListCtrl', ['$scope', '$q', 'Employee', 'EmployeeScroll', 'Company', 'Center', 'Division', EmployeesListCtrl]);

    function EmployeesListCtrl($scope, $q, Employee, EmployeeScroll, Company, Center, Division) {
        var self = this;

        self.employees = new EmployeeScroll();
        self.companies = null;
        self.centers = null;
        self.divisions = null;
        self.selectedCompany = null;
        self.selectedCenter = null;
        self.selectedDivision = null;

        self.querySearch = querySearch;
        self.getEmployeeName = getEmployeeName;
        self.loadCompanies = loadCompanies;
        self.loadCenters = loadCenters;
        self.loadDivisions = loadDivisions;

        self.companyChanged = companyChanged;
        self.centerChanged = centerChanged;
        self.divisionChanged = divisionChanged;

        function querySearch(query) {
            var deferred = $q.defer();
            Employee.query({search: query, limit: 10, offset: 0}, function(results, status) {
                deferred.resolve(results.results)
            });

            return deferred.promise
        }

        function loadCompanies() {
            return self.companies || Company.query(function(data) {
                self.companies = data;
            });
        }

        function loadCenters() {
            if (self.centers && self.centers.results.length
                 && self.centers.results[0].company == self.selectedCompany) return;
            return Center.query({company: self.selectedCompany}, function(data) {
                self.centers = data;
            });
        }

        function loadDivisions() {
            if (self.divisions && self.divisions.results.length
                 && self.divisions.results[0].center == self.selectedCenter) return;
            return Division.query({center: self.selectedCenter}, function(data) {
                self.divisions = data;
            });
        }

        function companyChanged() {
            self.selectedCenter = null;
            self.selectedDivision = null;
            self.employees = new EmployeeScroll({company: self.selectedCompany});
            self.employees.nextPage();
        }

        function centerChanged() {
            self.selectedDivision = null;
            self.employees = new EmployeeScroll({center: self.selectedCenter});
            self.employees.nextPage();
        }

        function divisionChanged() {
            self.employees = new EmployeeScroll({division: self.selectedDivision});
            self.employees.nextPage();
        }

        function getEmployeeName(employee) {
            return employee.surname + ' ' + employee.firstname + ' ' + employee.patronymic;
        }

    }
})();
