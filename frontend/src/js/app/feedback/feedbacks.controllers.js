(function() {
    'use strict';

    angular
        .module('pbApp.feedback')
        .controller('FeedbackListCtrl', FeedbackListCtrl);

    FeedbackListCtrl.$inject = ['$mdDialog', '$mdToast', 'feedbackService'];

    function FeedbackListCtrl($mdDialog, $mdToast, feedbackService) {
        var self = this;
        self.feedbacks = feedbackService.query({limit: 50, offset: 0});

    }
})();
