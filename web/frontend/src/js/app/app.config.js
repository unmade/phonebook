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


        var myBlue = $mdThemingProvider.extendPalette('blue', {
          '400': '4688f1',
          '500': '4688f1',
          '600': '4688f1'
        });
        $mdThemingProvider.definePalette('myBlue', myBlue);
        $mdThemingProvider.theme('default')
            .primaryPalette('myBlue')
            .accentPalette('red');
    }

})();
