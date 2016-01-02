'use strict';


describe('App filter', function() {

    beforeEach(module('pbApp'));

    describe('formatPhone', function() {

        it('should format phone number', inject(function(formatPhoneFilter) {
            expect(formatPhoneFilter('3808')).toEqual('38-08');
            expect(formatPhoneFilter('38-08')).toEqual('38-08');
            expect(formatPhoneFilter('38 08')).toEqual('38-08');
            expect(formatPhoneFilter('1580134')).toEqual('158-01-34');
            expect(formatPhoneFilter('158-01-34')).toEqual('158-01-34');
            expect(formatPhoneFilter('158 01 34')).toEqual('158-01-34');
            expect(formatPhoneFilter('9061583434')).toEqual('(906) 158-34-34');
            expect(formatPhoneFilter('906-158-34-34')).toEqual('(906) 158-34-34');
            expect(formatPhoneFilter('(906)-158-34-34')).toEqual('(906) 158-34-34');
            expect(formatPhoneFilter('(906) 158-34-34')).toEqual('(906) 158-34-34');
            expect(formatPhoneFilter('89061583434')).toEqual('8 (906) 158-34-34');
            expect(formatPhoneFilter('8-906-158-34-34')).toEqual('8 (906) 158-34-34');
            expect(formatPhoneFilter('8 906 158 34 34')).toEqual('8 (906) 158-34-34');
            expect(formatPhoneFilter('8 (906) 158-34-34')).toEqual('8 (906) 158-34-34');
            expect(formatPhoneFilter('+79061583434')).toEqual('+7 (906) 158-34-34');
        }));
    });
});
