(function() {
    'use strict';

    angular
        .module('pbApp')
        .config(config);

    config.$inject = ['$httpProvider', '$resourceProvider'];

    function config($httpProvider, $resourceProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

        $resourceProvider.defaults.stripTrailingSlashes = false;
    }

})();
