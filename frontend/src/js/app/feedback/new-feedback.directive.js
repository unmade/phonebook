(function() {
    'use strict';

    angular
        .module('pbApp.feedback')
        .directive('newFeedback', newFeedback);

    function newFeedback() {
        return {
            bindToController: true,
            controller: NewFeedbackCtrl,
            controllerAs: 'newFeedback',
            replace: true,
            restrict: 'AE',
            scope: {
                onSend: '&'
            },
            templateUrl: 'new-feedback.directive.html',
        }
    }

    NewFeedbackCtrl.$inject = ['$scope', '$mdDialog', '$mdToast', 'feedbackService'];

    function NewFeedbackCtrl($scope, $mdDialog, $mdToast, feedbackService) {
        var self = this;
        self.add = add;
        self.showSuccessToast = showSuccessToast;
        self.showFailedToast = showFailedToast;

        function add() {
            if (!self.sender || !self.text) return;
            feedbackService.save({
                sender: self.sender,
                text: self.text
            }, function(response) {
                self.status = '';
                if (self.onSend) self.onSend();
                self.showSuccessToast();
            }, function(error) {
                self.status = 'Error';
                self.showFailedToast();
            });
        }

        function showSuccessToast() {
            $mdToast.show(
                $mdToast.simple()
                    .textContent('Ваше сообщение принято!')
                    .position('top right')
                    .hideDelay(3000)
            );
        }

        function showFailedToast() {
            $mdToast.show(
                $mdToast.simple()
                    .textContent('Отправка не удалась!')
                    .position('top right')
                    .hideDelay(3000)
            );
        }
    }
})();
