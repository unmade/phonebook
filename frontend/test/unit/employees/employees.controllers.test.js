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
    beforeEach(module('pbApp.employees.controllers'));
    beforeEach(module('pbApp.employees.services'));
    beforeEach(module('pbApp.companies.services'));

    describe('EmployeesListCtrl Test', function() {
        var scope, $httpBackend, ctrl,
            employeeRespond = {
                getEmployeeList: getEmployeeList,
                getEmployeeDetail: getEmployeeDetail
            },
            companiesRespond = {
                getCompanyList: getCompanyList,
                getCenterList: getCenterList,
                getDivisionList: getDivisionList
            };

        beforeEach(inject(function(_$httpBackend_, $rootScope, $routeParams, $controller) {
            $httpBackend = _$httpBackend_;
            $httpBackend.whenGET('api/employees?limit=20&offset=0')
                        .respond(employeeRespond.getEmployeeList());
            $httpBackend.whenGET('api/employees?company=1&limit=20&offset=0')
                        .respond(employeeRespond.getEmployeeList());
            $httpBackend.whenGET('api/employees?center=1&limit=20&offset=0')
                        .respond(employeeRespond.getEmployeeList());
            $httpBackend.whenGET('api/employees?division=1&limit=20&offset=0')
                        .respond(employeeRespond.getEmployeeList());
            $httpBackend.whenGET('api/employees?limit=10&offset=0&search=%D0%9C%D0%BE%D1%80%D0%BE%D0%B7%D0%BE%D0%B2')
                        .respond(employeeRespond.getEmployeeList());
            $httpBackend.whenGET('api/companies').respond(companiesRespond.getCompanyList());
            $httpBackend.whenGET('api/centers?company=1').respond(companiesRespond.getCenterList());
            $httpBackend.whenGET('api/divisions?center=1').respond(companiesRespond.getDivisionList());
            scope = $rootScope.$new();
            ctrl = $controller('EmployeesListCtrl', {$scope: scope});
        }));

        it('should fetch employees', function() {
            expect(ctrl.employees).toEqualData({
                results: [],
                after: undefined,
                params: Object({ limit: 20, offset: 0 }),
                busy: false
            });
            ctrl.employees.nextPage();
            $httpBackend.flush();
            expect(ctrl.employees.results).toEqualData(employeeRespond.getEmployeeList().results);
        });

        it('should return results for autocomplete search query', function() {
            ctrl.searchText = "Морозов";
            var res = ctrl.querySearch(ctrl.searchText);
            $httpBackend.flush();
            expect(res.$$state.value).toEqualData(employeeRespond.getEmployeeList().results)
        })

        it('should load companies', function() {
            expect(ctrl.companies).toBeNull();
            ctrl.loadCompanies();
            $httpBackend.flush();
            expect(ctrl.companies).toEqualData(companiesRespond.getCompanyList());
        });

        it('should load centers', function() {
            expect(ctrl.selectedCompany).toBeNull();
            expect(ctrl.centers).toBeNull();
            ctrl.selectedCompany = 1;
            ctrl.loadCenters();
            $httpBackend.flush();
            expect(ctrl.centers).toEqualData(companiesRespond.getCenterList());
        });

        it('should load divisions', function() {
            expect(ctrl.selectedCenter).toBeNull();
            expect(ctrl.divisions).toBeNull();
            ctrl.selectedCenter = 1;
            ctrl.loadDivisions();
            $httpBackend.flush();
            expect(ctrl.divisions).toEqualData(companiesRespond.getDivisionList());
        });

        it('should update employees list and clear selected center and division on company change', function() {
            ctrl.selectedCompany = 1;
            ctrl.companyChanged();
            expect(ctrl.selectedCenter).toBeNull();
            expect(ctrl.selectedDivision).toBeNull();
            $httpBackend.flush();
            expect(ctrl.employees.results).toEqualData(employeeRespond.getEmployeeList().results);
        });

        it('should update employees list and clear selected division on center change', function() {
            ctrl.selectedCompany = 1;
            ctrl.selectedCenter = 1;
            ctrl.centerChanged();
            expect(ctrl.selectedDivision).toBeNull();
            $httpBackend.flush();
            expect(ctrl.employees.results).toEqualData(employeeRespond.getEmployeeList().results);
        });

        it('should update employees list on division change', function() {
            ctrl.selectedCompany = 1;
            ctrl.selectedCenter = 1;
            ctrl.selectedDivision = 1;
            ctrl.divisionChanged();
            $httpBackend.flush();
            expect(ctrl.employees.results).toEqualData(employeeRespond.getEmployeeList().results);
        });
    });
});
