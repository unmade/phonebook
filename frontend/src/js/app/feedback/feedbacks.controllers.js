(function() {
    'use strict';

    angular
        .module('pbApp.feedback')
        .controller('FeedbackListCtrl', FeedbackListCtrl);

    FeedbackListCtrl.$inject = ['Scroll', 'feedbackService'];

    function FeedbackListCtrl(Scroll, feedbackService) {
        var self = this;

        self.feedbacks = new Scroll(feedbackService);
    }

})();
