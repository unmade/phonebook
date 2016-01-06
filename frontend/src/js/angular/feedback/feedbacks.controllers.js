(function() {
    'use strict';

    angular
        .module('pbApp.feedback')
        .controller('FeedbackListCtrl', FeedbackListCtrl);

    FeedbackListCtrl.$inject = ['$mdDialog', '$mdToast', 'feedbackService'];

    function FeedbackListCtrl($mdDialog, $mdToast, feedbackService) {
        var self = this;
        self.feedbacks = feedbackService.query({limit: 50, offset: 0});
        self.showNewFeedbackDialog = showNewFeedbackDialog;

        function showNewFeedbackDialog(ev) {
            $mdDialog.show({
                templateUrl: 'new-feedback-dialog.tmpl.html',
                targetEvent: ev,
                clickOutsideToClose: true,
                controller: DialogCtrl,
                controllerAs: 'dialog'
            });
        }

        function DialogCtrl() {
            var dialog = this;
            dialog.hide = hide;

            function hide() {
                $mdDialog.hide();
                feedbackService.query({limit: 50, offset: 0}, function(data) {
                    self.feedbacks = data;
                })
            }
        }

    }
})();
