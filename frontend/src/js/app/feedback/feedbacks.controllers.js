(function() {
    'use strict';

    angular
        .module('pbApp.feedback')
        .controller('FeedbackListCtrl', FeedbackListCtrl);

    FeedbackListCtrl.$inject = ['FeedbackScroll'];

    function FeedbackListCtrl(FeedbackScroll) {
        var self = this;

        self.feedbacks = new FeedbackScroll();
    }

})();
