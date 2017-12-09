(function() {
    'use strict';

    angular
        .module('pbApp.feedback')
        .factory('feedbackService', feedbackService);

    feedbackService.$inject = ['$resource'];

    function feedbackService($resource) {
        return $resource('feedback/api/feedback/', {}, {
            query: {
                method: 'GET',
                isArray: false
            }
        });
    }

})();
