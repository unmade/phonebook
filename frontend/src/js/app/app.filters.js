(function() {
    'use strict';
    angular
        .module('pbApp')
        .filter('formatPhone', formatPhone);

    function formatPhone() {
        return function (phoneNumber) {
            if (!phoneNumber) { return ''; }

            var country, city, number,
                value = phoneNumber.toString().replace(/[()-\s]+/g, '');

            function formatNumber(value) {
                if (value.length == 4)
                    return value.slice(0, 2) + '-' + value.slice(2);
                if (value.length == 7)
                    return value.slice(0, 3) + '-' + value.slice(3, 5) + '-' + value.slice(5, 7);
                return value;
            };

            switch (value.length) {
                case 4: // #### -> ##-##
                case 7: // ####### -> ###-##-##
                   return formatNumber(value);
                   break;
                case 10: // PPP####### -> (PPP) ###-##-##
                    country = "";
                    city = value.slice(0, 3);
                    number = formatNumber(value.slice(3));
                    break;
                case 11: // CPPP####### -> C (PPP) ###-##-##
                    country = value[0];
                    city = value.slice(1, 4);
                    number = formatNumber(value.slice(4));
                    break;
                case 12: // +CPPP####### -> C (PPP) ###-##-##
                    country = value.slice(0, 2);
                    city = value.slice(2, 5);
                    number = formatNumber(value.slice(5));
                    break;
                default:
                    return phoneNumber;
            }

            return (country + " (" + city + ") " + number).trim();
        };
    };
})();
