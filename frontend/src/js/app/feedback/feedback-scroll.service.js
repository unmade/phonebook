(function() {
    'use strict'

    angular
        .module('pbApp.feedback')
        .factory('FeedbackScroll', FeedbackScroll);

    FeedbackScroll.$inject = ['feedbackService'];

    function FeedbackScroll(feedbackService) {
        var Scroll = function(params) {
            this.results = [];
            this.after = undefined;
            this.params = angular.copy(params) || {};
            this.params.offset = (params && params.offset) ? params.offset : 0;
            this.params.limit = (params && params.limit) ? params.limit : 20;
            this.busy = false;
        };

        Scroll.prototype.nextPage = function() {
            if (this.busy) return;
            if (this.after === null) return;
            this.busy = true;

            feedbackService.query(this.params, function(data) {
                this.results = this.results.concat(data.results);
                this.params.offset += this.params.limit;
                this.after = data.next;
                this.busy = false;
            }.bind(this));
        };

        return Scroll;
    }

})();
