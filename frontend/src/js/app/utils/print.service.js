(function() {
    'use strict';

    angular
        .module('pbApp.utils')
        .factory('printerService', printerService);


    printerService.$inject = ['$rootScope', '$compile', '$http', '$timeout'];

    function printerService($rootScope, $compile, $http, $timeout) {

        function printHtml(html) {
            var hiddenFrame = $("<iframe style='display: none'></iframe>").appendTo('body')[0];
            hiddenFrame.contentWindow.printAndRemove = function() {
                hiddenFrame.contentWindow.print();
                $(hiddenFrame).remove();
            };
            var htmlContent = "<!doctype html>" +
                              "  <html>" +
                              "    <body onload='printAndRemove();'>" +
                                   html +
                              "    </body>" +
                              "</html>",
                doc = hiddenFrame.contentWindow.document.open("text/html", "replace");
            doc.write(htmlContent);
            doc.close();
        };

        function openNewWindow(html) {
            var newWindow = window.open("printTest.html");
            newWindow.addEventListener('load', function() {
                $(newWindow.document.body).html(html);
           }, false);
       };

        function print(templateUrl, data) {
            $http.get(templateUrl).success(function(template) {
                var printScope = $rootScope.$new();
                angular.extend(printScope, data);
                var element = $compile($('<div>' + template + '</div>'))(printScope),
                    waitForRenderAndPrint = function() {
                        if(printScope.$$phase || $http.pendingRequests.length) {
                            $timeout(waitForRenderAndPrint);
                        } else {
                            // Replace printHtml with openNewWindow for debugging
                            printHtml(element.html());
                            printScope.$destroy();
                        }
                    };
                waitForRenderAndPrint();
            });
        };

        return {
            print: print
        }
    }
})();
