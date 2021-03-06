describe('Employees controllers', function() {

    beforeEach(function(){
        jasmine.addMatchers({
            toEqualData: function(util, customEqualityTesters) {
                return {
                    compare: function(actual, expected) {
                        return {
                            pass: angular.equals(actual, expected)
                        };
                    }
                };
            }
        });
    });

    beforeEach(module('pbApp'));
    beforeEach(module('pbApp.companies'));
    beforeEach(module('pbApp.employees'));

    describe('EmployeeListCtrl Test', function() {
        var scope, $httpBackend, ctrl,
            employeeRespond = {
                employees: {results: getEmployeeList().results.slice(0, 20)},
                employeesNext: {results: getEmployeeList().results.slice(20, 40)},
                filteredByCompany: {results: getEmployeeList().results.slice(0, 2)},
                filteredByCompanyAndCenter: {results: getEmployeeList().results.slice(0, 3)},
                filteredByCompanyAndCenterAndDivision: {results: getEmployeeList().results.slice(0, 8)},
                employeeSearch: {results: getEmployeeList().results.slice(0, 5)},
                search: {results: getEmployeeList().results.slice(0, 6)}
            },
            companiesRespond = {
                companyList: getCompanyList(),
                centerList: getCenterList(),
                divisionList: getDivisionList()
            };

        beforeEach(inject(function(_$httpBackend_, $rootScope, $routeParams, $controller) {
            $httpBackend = _$httpBackend_;
            $httpBackend.whenGET('employees/api/employee/?limit=20&offset=0')
                        .respond(employeeRespond.employees);
            $httpBackend.whenGET('employees/api/employee/?limit=20&offset=20')
                        .respond(employeeRespond.employeesNext);
            $httpBackend.whenGET('employees/api/employee/?company=1&limit=20&offset=0')
                        .respond(employeeRespond.filteredByCompany);
            $httpBackend.whenGET('employees/api/employee/?center=1&company=1&limit=20&offset=0')
                        .respond(employeeRespond.filteredByCompanyAndCenter);
            $httpBackend.whenGET('employees/api/employee/?center=1&company=1&division=1&limit=20&offset=0')
                        .respond(employeeRespond.filteredByCompanyAndCenterAndDivision);
            $httpBackend.whenGET('employees/api/employee/?limit=8&offset=0&search=%D0%BC%D0%BE%D1%80%D0%BE%D0%B7%D0%BE%D0%B2')
                        .respond(employeeRespond.employeeSearch);
            $httpBackend.whenGET('employees/api/employee/?limit=20&offset=0&search=%D0%9C%D0%BE%D1%80%D0%BE%D0%B7%D0%BE%D0%B2')
                        .respond(employeeRespond.search);
            $httpBackend.whenGET('companies/api/company/').respond(companiesRespond.companyList);
            $httpBackend.whenGET('companies/api/center/?company=1').respond(companiesRespond.centerList);
            $httpBackend.whenGET('companies/api/division/?center=1').respond(companiesRespond.divisionList);
            scope = $rootScope.$new();
            ctrl = $controller('EmployeeListCtrl', {$scope: scope});
        }));

        it('should fetch employees', function() {
            expect(ctrl.employees).toEqualData({
                results: [],
                after: undefined,
                params: {limit: 20, offset: 0},
                busy: false
            });
            ctrl.employees.nextPage();
            expect(ctrl.employees.busy).toBe(true);
            $httpBackend.flush();
            expect(ctrl.employees.results).toEqualData(employeeRespond.employees.results);
            expect(ctrl.employees.params.limit).toEqual(20);
            expect(ctrl.employees.params.offset).toEqual(20);
            expect(ctrl.employees.after).toBe(undefined);
            expect(ctrl.employees.busy).toBe(false);
        });

        it('should return results for autocomplete search query', function() {
            ctrl.searchText = "Морозов";
            var res = ctrl.employeeSearch(ctrl.searchText);
            $httpBackend.flush();
            expect(res.$$state.value).toEqualData(employeeRespond.employeeSearch.results);
        });

        it('should update employees list according to search query', function() {
            ctrl.searchText = "Морозов";
            ctrl.selectedCompany = 1;
            ctrl.selectedCenter = 1;
            ctrl.selectedDivision = 1;
            ctrl.search(ctrl.searchText);
            $httpBackend.flush();
            expect(ctrl.selectedCompany).toBeNull();
            expect(ctrl.selectedCenter).toBeNull();
            expect(ctrl.selectedDivision).toBeNull();
            expect(ctrl.employees.results).toEqualData(employeeRespond.search.results);
        });

        it('should load companies', function() {
            expect(ctrl.companies).toBeNull();
            ctrl.loadCompanies();
            $httpBackend.flush();
            expect(ctrl.companies).toEqualData(companiesRespond.companyList);
        });

        it('should load centers', function() {
            expect(ctrl.selectedCompany).toBeNull();
            expect(ctrl.centers).toBeNull();
            ctrl.selectedCompany = 1;
            ctrl.loadCenters();
            $httpBackend.flush();
            expect(ctrl.centers).toEqualData(companiesRespond.centerList);
        });

        it('should load divisions', function() {
            expect(ctrl.selectedCenter).toBeNull();
            expect(ctrl.divisions).toBeNull();
            ctrl.selectedCenter = 1;
            ctrl.loadDivisions();
            $httpBackend.flush();
            expect(ctrl.divisions).toEqualData(companiesRespond.divisionList);
        });

        it('should update employees list and clear selected center and division on company change', function() {
            ctrl.selectedCompany = 1;
            ctrl.selectedCenter = 1;
            ctrl.selectedDivision = 1;
            ctrl.companyChanged();
            expect(ctrl.selectedCenter).toBeNull();
            expect(ctrl.selectedDivision).toBeNull();
            $httpBackend.flush();
            expect(ctrl.employees.results).toEqualData(employeeRespond.filteredByCompany.results);
        });

        it('should update employees list and clear selected division on center change', function() {
            ctrl.selectedCompany = 1;
            ctrl.selectedCenter = 1;
            ctrl.selectedDivision = 1;
            ctrl.centerChanged();
            expect(ctrl.selectedDivision).toBeNull();
            $httpBackend.flush();
            expect(ctrl.employees.results).toEqualData(employeeRespond.filteredByCompanyAndCenter.results);
        });

        it('should update employees list on division change', function() {
            ctrl.selectedCompany = 1;
            ctrl.selectedCenter = 1;
            ctrl.selectedDivision = 1;
            ctrl.divisionChanged();
            $httpBackend.flush();
            expect(ctrl.employees.results).toEqualData(employeeRespond.filteredByCompanyAndCenterAndDivision.results);
        });
    });
});
