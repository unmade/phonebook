describe('new-feedback.directive.js', function() {
    var $compile, $httpBackend, ctrl, $rootScope;

    beforeEach(module('pbApp'));
    beforeEach(module('pbApp.feedback'));

    beforeEach(inject(function(_$compile_, _$httpBackend_, _$rootScope_, $controller) {
        $compile = _$compile_;
        $rootScope = _$rootScope_;
        $httpBackend = _$httpBackend_;
        $httpBackend.expectPOST('api/feedback/feedback/').respond(201, '');
    }));

    it('should add new feedback', function() {
        var element = $compile('<new-feedback></new-feedback>')($rootScope);
        $rootScope.$digest();
        var scope = element.isolateScope(),
            newFeedback = scope.newFeedback;
        newFeedback.sender = 'Yoa Noel';
        newFeedback.text = 'Great job!';
        newFeedback.add();
        $httpBackend.flush();
        expect(newFeedback.status).toBe('');
    });

});
