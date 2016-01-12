(function() {
    'use strict';

    angular
        .module('pbApp.employees')
        .controller('EmployeeListCtrl',  EmployeeListCtrl);

    EmployeeListCtrl.$inject = ['$q', '$mdDialog', 'employeeService', 'EmployeeScroll',
                                'companyService', 'centerService', 'divisionService'];

    function EmployeeListCtrl($q, $mdDialog, employeeService, EmployeeScroll,
                              companyService, centerService, divisionService) {
        var self = this;

        self.employees = new EmployeeScroll();
        self.companies = null;
        self.centers = null;
        self.divisions = null;
        self.selectedCompany = null;
        self.selectedCenter = null;
        self.selectedDivision = null;

        self.companyChanged = companyChanged;
        self.centerChanged = centerChanged;
        self.divisionChanged = divisionChanged;
        self.employeeSearch = employeeSearch;
        self.getEmployeeName = getEmployeeName;
        self.loadCompanies = loadCompanies;
        self.loadCenters = loadCenters;
        self.loadDivisions = loadDivisions;
        self.search = search;

        self.showEmployeeDetail = showEmployeeDetail;

        function showEmployeeDetail(ev, employee) {
            if (!employee) return;
            $mdDialog.show({
                controller: ['employee', EmployeeDetailDialogCtrl],
                controllerAs: 'dialog',
                templateUrl: 'employee-detail.dialog.tmpl.html',
                parent: angular.element(document.body),
                locals: {employee: employee},
                targetEvent: ev,
                clickOutsideToClose: true
            });
        }

        function EmployeeDetailDialogCtrl(employee) {
            var dialog = this;
            dialog.employee = employee;
            dialog.hide = hide;

            function hide() {
                $mdDialog.hide();
            }
        }

        function companyChanged() {
            self.selectedCenter = null;
            self.selectedDivision = null;
            self.employees = new EmployeeScroll({
                company: self.selectedCompany,
                search: self.searchText || null
            });
            self.employees.nextPage();
        }

        function centerChanged() {
            self.selectedDivision = null;
            self.employees = new EmployeeScroll({
                company: self.selectedCompany,
                center: self.selectedCenter,
                search: self.searchText || null
            });
            self.employees.nextPage();
        }

        function divisionChanged() {
            self.employees = new EmployeeScroll({
                company: self.selectedCompany,
                center: self.selectedCenter,
                division: self.selectedDivision,
                search: self.searchText || null
            });
            self.employees.nextPage();
        }

        function employeeSearch(query) {
            var limit = 4;
            if (!query) return self.employees.results.slice(0, limit);
            var deferred = $q.defer();
            employeeService.query({
                search: query,
                limit: limit,
                offset: 0
            }, function(results, status) {
                deferred.resolve(results.results)
            });

            return deferred.promise
        }

        function getEmployeeName(employee) {
            return employee.surname + ' ' + employee.firstname + ' ' + employee.patronymic;
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

        function search(query) {
            self.selectedCompany = null;
            self.selectedCenter = null;
            self.selectedDivision = null;
            self.employees = new EmployeeScroll({search: query});
            self.employees.nextPage();
        }

    }
})();
