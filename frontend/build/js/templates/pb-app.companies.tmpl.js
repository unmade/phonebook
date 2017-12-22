angular.module("pbApp.companies").run(["$templateCache", function($templateCache) {$templateCache.put("company-detail.directive.html","<md-content layout=\"column\">\n    <div class=\"company-detail_logo\">\n        <img ng-src=\"{{ company.logo }}\" />\n    </div>\n\n    <div class=\"company-detail_name\">\n        <h3 class=\"md-title\">{{ company.name }}</h3>\n        <p class=\"md-caption\" ng-if=\"company.ceo\">{{ company.ceo.position }}: {{ company.ceo | toFullname }}</p>\n    </div>\n\n    <div class=\"md-whiteframe-4dp\">\n        <md-list>\n            <md-list-item class=\"md-1-line\" ng-show=\"company.address\">\n                <md-icon>place</md-icon>\n                <p>{{ company.address }}</p>\n            </md-list-item>\n            <md-list-item class=\"md-2-line\"\n                          ng-repeat=\"phone in company.phones\">\n                <md-icon ng-if=\"$first\">phone</md-icon>\n                <div class=\"md-list-item-text\" ng-class=\"{\'md-offset\': !$first}\">\n                    <h3>{{ phone.number }}</h3>\n                    <p>\n                        {{ phone.category }}\n                        <span ng-show=\"phone.comment\"> ({{ phone.comment }})</span>\n                    </p>\n                </div>\n            </md-list-item>\n            <md-list-item class=\"md-2-line\"\n                          ng-repeat=\"email in company.emails\">\n                <md-icon ng-if=\"$first\">email</md-icon>\n                <div class=\"md-list-item-text\" ng-class=\"{\'md-offset\': !$first}\">\n                    <h3>{{ email.email }}</h3>\n                    <p>\n                        {{ email.category }}\n                        <span ng-show=\"email.comment\"> ({{ email.comment }})</span>\n                    </p>\n                </div>\n            </md-list-item>\n        </md-list>\n\n        <md-divider ng-show=\"company.full_name || company.comment\"></md-divider>\n\n        <md-list>\n            <md-list-item class=\"md-1-line\" ng-show=\"company.full_name\">\n                <md-icon>description</md-icon>\n                <p>{{ company.full_name }}</p>\n            </md-list-item>\n\n            <md-list-item class=\"md-1-line\" ng-show=\"company.comment\">\n                <md-icon>info</md-icon>\n                <p>{{ company.comment }}</p>\n            </md-list-item>\n        </md-list>\n\n    </div>\n</md-content>\n");}]);