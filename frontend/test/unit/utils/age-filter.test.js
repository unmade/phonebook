'use strict';

describe('Age Filter', function() {
    beforeEach(module('pbApp'));
    beforeEach(module('pbApp.utils'));

    it('should return age based on birthday datestring', inject(function(ageFilter) {
        expect(ageFilter('1970-01-01')).toBe(new Date().getFullYear() - 1970);
    }));

    it('should return pluralized age string', inject(function(agePluralFilter) {
        expect(agePluralFilter(0)).toEqual('0 лет');
        expect(agePluralFilter(1)).toEqual('1 год');
        expect(agePluralFilter(2)).toEqual('2 года');
        expect(agePluralFilter(3)).toEqual('3 года');
        expect(agePluralFilter(4)).toEqual('4 года');
        expect(agePluralFilter(5)).toEqual('5 лет');
        expect(agePluralFilter(6)).toEqual('6 лет');
        expect(agePluralFilter(7)).toEqual('7 лет');
        expect(agePluralFilter(8)).toEqual('8 лет');
        expect(agePluralFilter(9)).toEqual('9 лет');
        expect(agePluralFilter(10)).toEqual('10 лет');
        expect(agePluralFilter(11)).toEqual('11 лет');
        expect(agePluralFilter(12)).toEqual('12 лет');
        expect(agePluralFilter(13)).toEqual('13 лет');
        expect(agePluralFilter(14)).toEqual('14 лет');
        expect(agePluralFilter(15)).toEqual('15 лет');
    }));
});
