(function() {
    'use strict';

    angular
        .module('pbApp.utils')
        .filter('englishCharsToRussian', englishCharsToRussian);

    function englishCharsToRussian() {
        return function(str) {
            if (!typeof(str) === 'string') return "";

            var letters = {
                'q': 'й',
                'w': 'ц',
                'e': 'у',
                'r': 'к',
                't': 'е',
                'y': 'н',
                'u': 'г',
                'i': 'ш',
                'o': 'щ',
                'p': 'з',
                '[': 'х',
                '{': 'х',
                ']': 'ъ',
                '}': 'ъ',
                'a': 'ф',
                's': 'ы',
                'd': 'в',
                'f': 'а',
                'g': 'п',
                'h': 'р',
                'j': 'о',
                'k': 'л',
                'l': 'д',
                ';': 'ж',
                ':': 'ж',
                '\'': 'э',
                '"': 'э',
                '\\': 'ё',
                '`': 'ё',
                '|': 'ё',
                'z': 'я',
                'x': 'ч',
                'c': 'с',
                'v': 'м',
                'b': 'и',
                'n': 'т',
                'm': 'ь',
                ',': 'б',
                '<': 'б',
                '.': 'ю',
                '>': 'ю',
            }

            var lower = str.toLowerCase(),
                i,
                newStrArr = [];

            for (i = 0; i < lower.length; i += 1) {
                (letters[lower[i]]) ? newStrArr.push(letters[lower[i]]) : newStrArr.push(lower[i]);
            }

            return newStrArr.join('');
        }
    }
})()
