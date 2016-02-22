describe('Companies controllers', function() {

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

    describe('CompanyListCtrl Test', function() {
        var scope, $httpBackend, ctrl,
            companyRespond = {
                companies: {results: getCompanyList().results.slice(0, 40)},
                companySearch: {results: getCompanyList().results.slice(0, 5)},
            }

        beforeEach(inject(function(_$httpBackend_, $rootScope, $routeParams, $controller) {
            $httpBackend = _$httpBackend_;
            $httpBackend.whenGET('api/companies/company/?limit=40&offset=0')
                        .respond(companyRespond.companies);
            $httpBackend.whenGET('api/companies/company/?limit=4&offset=0&search=%D0%BD%D0%BF%D0%BE%D0%BB')
                        .respond(companyRespond.companySearch);
            scope = $rootScope.$new();
            ctrl = $controller('CompanyListCtrl', {$scope: scope});
        }));


        it('should fetch companies', function() {
            var limit = 40;
            expect(ctrl.companies).toEqualData({
                results: [],
                after: undefined,
                params: {limit: limit, offset: 0},
                busy: false
            });
            ctrl.companies.nextPage();
            expect(ctrl.companies.busy).toBe(true);
            $httpBackend.flush();
            expect(ctrl.companies.results).toEqualData(companyRespond.companies.results);
            expect(ctrl.companies.params.limit).toEqual(limit);
            expect(ctrl.companies.params.offset).toEqual(limit);
            expect(ctrl.companies.after).toBe(undefined);
            expect(ctrl.companies.busy).toBe(false);
        });


        it('should return results for autocomplete search query', function() {
            ctrl.searchText = "нпол";
            var res = ctrl.companySearch(ctrl.searchText);
            $httpBackend.flush();
            expect(res.$$state.value).toEqualData(companyRespond.companySearch.results);
        });


        it('should set ctrl.company to company', function() {
            expect(ctrl.company).toBeUndefined();
            var company = companyRespond.companies.results[0];
            ctrl.openCompanyDetail(company);
            expect(ctrl.company).toEqual(company);
        });
    });
});
