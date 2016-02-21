'use strict';


describe('Employees filter', function() {
    beforeEach(module('pbApp'));
    beforeEach(module('pbApp.employees'));

    describe('toFullname', function() {

        it('should get employee full name (as a string)', inject(function(toFullnameFilter) {
            var employee1 = {
                surname: 'Smith',
                firstname: 'GE',
                patronymic: '.'
            },
            employee2 = {
                surname: 'Smith',
                firstname: 'GE',
                patronymic: null
            };

            expect(toFullnameFilter(employee1)).toEqual('Smith GE .');
            expect(toFullnameFilter(employee2)).toEqual('Smith GE');
        }));
    });
});
