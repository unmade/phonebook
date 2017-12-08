(function() {
    'use strict';

    angular
        .module('pbApp.utils')
        .filter('age', getAge)
        .filter('agePlural', pluralAge);

    function getAge() {
        return function(dateStr) {
            if (dateStr === undefined || dateStr === null) return;
            var today = Date.parse(new Date()),
                birthday = Date.parse(dateStr),
                age;
            return new Date(today - birthday).getFullYear() - 1970;

        }
    }

    function pluralAge() {
        return function(age) {
            if (age === 11 || age === 12 || age === 13 || age === 14) {
                return age + ' лет';
            }

            switch (age % 10) {
                case 1:
                    return age + ' год';
                case 2:
                case 3:
                case 4:
                    return age + ' года';
                default:
                    return age + ' лет';
            }
        }
    }
})();
