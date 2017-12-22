'use strict';

describe('Scroll Factory', function () {

    beforeEach(module('pbApp'));
    beforeEach(module('pbApp.utils'));


    it('should init and test new Scroll factory without params', inject(function(Scroll) {
        expect(Scroll).toBeDefined();
        var testService = {
            query: function(params, callback) {
                callback({results: [1, 2, 3, 4]});
            }
        }
        var scroll = new Scroll(testService);
        expect(scroll.results).toEqual([]);
        expect(scroll.busy).toBe(false);
        expect(scroll.service).toEqual(testService);
        expect(scroll.params.offset).toBe(0);
        expect(scroll.params.limit).toEqual(20);

        scroll.nextPage();

        expect(scroll.results).toEqual([1, 2, 3, 4]);
        expect(scroll.params.offset).toBe(20);
        expect(scroll.params.limit).toEqual(20);
    }));

    it('should init and test new Scroll factory with params', inject(function(Scroll) {
        expect(Scroll).toBeDefined();
        var testService = {
                query: function(params, callback) {
                    callback({results: [1, 2, 3, 4]});
                }
            },
            params = {
                limit: 40,
                offset: 10
            };
        var scroll = new Scroll(testService, params);
        expect(scroll.results).toEqual([]);
        expect(scroll.busy).toBe(false);
        expect(scroll.service).toEqual(testService);
        expect(scroll.params.offset).toBe(10);
        expect(scroll.params.limit).toEqual(40);

        scroll.nextPage();

        expect(scroll.results).toEqual([1, 2, 3, 4]);
        expect(scroll.params.offset).toBe(50);
        expect(scroll.params.limit).toEqual(40);
    }));
});
