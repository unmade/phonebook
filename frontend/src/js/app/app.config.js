(function() {
    'use strict';

    angular
        .module('pbApp')
        .config(config);

    config.$inject = ['$httpProvider', '$resourceProvider', '$mdThemingProvider'];

    function config($httpProvider, $resourceProvider, $mdThemingProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

        $resourceProvider.defaults.stripTrailingSlashes = false;

        $mdThemingProvider.theme('default')
            .accentPalette('red');
    }

})();
