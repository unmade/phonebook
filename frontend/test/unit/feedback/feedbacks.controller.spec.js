describe('feedbacks.controllers', function() {

    var scope, $httpBackend, ctrl,
        feedbackRespond = {
            feedbacks: {results: getFeedbackList().results.slice(0, 50)}
        }

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
    beforeEach(module('pbApp.feedback'));


    describe('FeedbackListCtrl', function() {
        beforeEach(inject(function(_$httpBackend_, $rootScope, $controller) {
            $httpBackend = _$httpBackend_;
            $httpBackend.whenGET('api/feedback/feedback/?limit=20&offset=0')
                        .respond(feedbackRespond.feedbacks);
            scope = $rootScope.$new();
            ctrl = $controller('FeedbackListCtrl', {$scope: scope});
        }));

        it('should fetch feedbacks list', function() {
            ctrl.feedbacks.nextPage();
            $httpBackend.flush();
            expect(ctrl.feedbacks.results).toEqualData(feedbackRespond.feedbacks.results);
        });
    });

});
