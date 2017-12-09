'use strict';


describe('Utils filter', function() {

    beforeEach(module('pbApp.utils'));

    describe('Match english keyboard chars to russian', function() {

        it('should translate english keyboard chars to russian', inject(function(englishCharsToRussianFilter) {
            expect(englishCharsToRussianFilter('fcvec')).toEqual('асмус');
            expect(englishCharsToRussianFilter('Fcvec')).toEqual('асмус');
            expect(englishCharsToRussianFilter('|,ekby')).toEqual('ёбулин');
            expect(englishCharsToRussianFilter('`<ekby')).toEqual('ёбулин');
            expect(englishCharsToRussianFilter('[{}]')).toEqual('ххъъ');
            expect(englishCharsToRussianFilter(';:\'"')).toEqual('жжээ');
        }));
    });
});
