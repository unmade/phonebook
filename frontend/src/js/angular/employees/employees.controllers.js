(function() {
    'use strict';
    angular
        .module('pbApp.employees.controllers')
        .controller('EmployeesListCtrl', ['$scope', '$q', '$mdDialog', 'Employee', 'EmployeeScroll',
                                          'Company', 'Center', 'Division', EmployeesListCtrl]);

    function EmployeesListCtrl($scope, $q, $mdDialog, Employee, EmployeeScroll, Company, Center, Division) {
        var self = this;

        self.employees = new EmployeeScroll();
        self.companies = null;
        self.centers = null;
        self.divisions = null;
        self.selectedCompany = null;
        self.selectedCenter = null;
        self.selectedDivision = null;

        self.employeeSearch = employeeSearch;
        self.getEmployeeName = getEmployeeName;
        self.loadCompanies = loadCompanies;
        self.loadCenters = loadCenters;
        self.loadDivisions = loadDivisions;
        self.search = search;

        self.companyChanged = companyChanged;
        self.centerChanged = centerChanged;
        self.divisionChanged = divisionChanged;

        self.showEmployeeDetail = showEmployeeDetail;

        function showEmployeeDetail(ev, employee) {
            $mdDialog.show({
                controller: ['$scope' , 'employee', EmployeeDetailDialogCtrl],
                templateUrl: 'employee-detail.dialog.tmpl.html',
                parent: angular.element(document.body),
                locals: {employee: employee},
                targetEvent: ev,
                clickOutsideToClose:true
            });

            function EmployeeDetailDialogCtrl($scope, employee) {
                $scope.employee = employee;
                
                $scope.hide = function() {
                    $mdDialog.hide();
                }
                $scope.cancel = function() {
                    $mdDialog.cancel();
                }
                $scope.answer = function(answer) {
                    $mdDialog.hide(answer);
                }
            }
        }

        function employeeSearch(query) {
            var limit = 4;
            if (!query) return self.employees.results.slice(0, limit);
            var deferred = $q.defer();
            Employee.query({search: query, limit: limit, offset: 0}, function(results, status) {
                deferred.resolve(results.results)
            });

            return deferred.promise
        }

        function search(query) {
            self.selectedCompany = null;
            self.selectedCenter = null;
            self.selectedDivision = null;
            self.employees = new EmployeeScroll({search: query});
            self.employees.nextPage();
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

        function getEmployeeName(employee) {
            return employee.surname + ' ' + employee.firstname + ' ' + employee.patronymic;
        }
    }
})();
