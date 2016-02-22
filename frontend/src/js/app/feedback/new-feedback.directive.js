(function() {
    'use strict';

    angular
        .module('pbApp.feedback')
        .directive('newFeedback', newFeedback);

    function newFeedback() {
        return {
            bindToController: true,
            controller: newFeedbackCtrl,
            controllerAs: 'newFeedback',
            replace: true,
            restrict: 'AE',
            scope: {
                'buttonClass': '@buttonClass'
            },
            templateUrl: 'new-feedback.directive.html',
        }
    }

    newFeedbackCtrl.$inject = ['$scope', '$mdDialog', '$mdToast', 'feedbackService'];

    function newFeedbackCtrl($scope, $mdDialog, $mdToast, feedbackService) {
        var self = this;

        self.showNewFeedbackDialog = showNewFeedbackDialog;

        function add(feedback) {
            if (!feedback.sender || !feedback.text) return;
            feedbackService.save({
                sender: feedback.sender,
                text: feedback.text
            }, function(response) {
                showSuccessToast();
            }, function(error) {
                showFailedToast();
            });
        }

        function showFailedToast() {
            $mdToast.show(
                $mdToast.simple()
                    .textContent('Отправка не удалась!')
                    .position('top right')
                    .hideDelay(3000)
            );
        }

        function showSuccessToast() {
            $mdToast.show(
                $mdToast.simple()
                    .textContent('Ваше сообщение принято!')
                    .position('top right')
                    .hideDelay(3000)
            );
        }

        function showNewFeedbackDialog(ev) {
            $mdDialog.show({
                templateUrl: 'new-feedback-dialog.tmpl.html',
                targetEvent: ev,
                clickOutsideToClose: true,
                controller: newFeedbackDialogCtrl,
                controllerAs: 'nfdCtrl',
                fullscreen: true
            }).then(function(feedback) {
                add(feedback);
            });
        }
    }

    newFeedbackDialogCtrl.$inject = ['$mdDialog'];

    function newFeedbackDialogCtrl($mdDialog) {
        var self = this;

        self.feedback = {sender: null, text: null};

        self.cancel = cancel;
        self.send = send;

        function cancel() {
            $mdDialog.cancel();
        }

        function send() {
            $mdDialog.hide(self.feedback);
        }
    }
})();
