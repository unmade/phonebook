(function() {
    'use strict';

    angular
        .module('pbApp.employees')
        .filter('toFullname', toFullname);

    function toFullname() {
        return function(employee) {
            var strOrEmpty = function(str) {
                return (str) ? str : "";
            }
            return (strOrEmpty(employee.surname) + ' ' +
                    strOrEmpty(employee.firstname) + ' ' +
                    strOrEmpty(employee.patronymic)).trim();
        }
    }
})();
