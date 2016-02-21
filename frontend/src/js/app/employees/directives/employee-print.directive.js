(function() {
    'use strict';

    angular
        .module('pbApp.employees')
        .directive('printEmployees', printEmployees);

    function printEmployees() {
        return {
            restrict: 'AE',
            controller: printEmployeesCtrl,
            controllerAs: 'printCtrl',
            templateUrl: 'directives/employee-print.directive.html'
        };
    }

    printEmployeesCtrl.$inject = ['$mdDialog'];

    function printEmployeesCtrl($mdDialog) {
        var self = this;
        self.showPrintDialog = showPrintDialog;

        function showPrintDialog(ev) {
            $mdDialog.show({
                controller: printDialogCtrl,
                controllerAs: 'printDialogCtrl',
                templateUrl: 'print-employee-dialog.tmpl.html',
                parent: angular.element(document.body),
                targetEvent: ev,
                clickOutsideToClose: true
            });
        }
    }

    printDialogCtrl.$inject = ['$q', '$filter', '$mdDialog',
                               'companyService', 'employeeService', 'printerService'];

    function printDialogCtrl($q, $filter, $mdDialog, companyService, employeeService, printerService) {
        var self = this;

        self.busy = false;
        self.companies = companyService.query();
        self.type = 'all';
        self.selectedEmployees = [];
        self.selectedCompany = null;
        self.selectedItem = null;
        self.searchText = null;

        self.employeeSearch = employeeSearch;
        self.hide = hide;
        self.print = print;


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

        function hide() {
            $mdDialog.hide();
        }

        function print() {
            self.busy = true;
            var employees,
                callback = function(data) {
                    employees = data.results;
                    printerService.print(
                        '/static/partials/utils/print-template.html',
                        {
                            employees: employees
                        }
                    );
                    self.busy = false;
                };

            if (self.type === 'all') {
                employeeService.query({limit: 99999999}, callback);
            }
            if (self.type === 'by_company') {
                employeeService.query({limit: 99999999, company: self.selectedCompany}, callback);
            }
            if (self.type === 'custom') {
                callback({results: self.selectedEmployees});
            }
        }
    }

})();
