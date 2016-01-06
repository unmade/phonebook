(function() {
    'use strict';

    angular
        .module('pbApp.feedback')
        .filter('getStatusName', getStatusName);

    function getStatusName() {
        return function(code) {
            switch(code) {
                case 'DF':
                    return '';
                case 'PR':
                    return 'В процессе';
                case 'NW':
                    return 'Новое';
                case 'SL':
                    return 'Выполнено';
                case 'RJ':
                    return 'Не будет выполнено';
                default:
                    return "";
            }
        }
    }
})();
