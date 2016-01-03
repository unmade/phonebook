angular.module("pbApp.employees.directives").run(["$templateCache", function($templateCache) {$templateCache.put("employees/directives/templates/employee-detail.html","<div layout=\"row\" class=\"md-dialog-content employee-detail\">\n    <div layout=\"column\" layout-align=\"center center\" class=\"employee-detail_name\" layout-padding>\n        <md-icon>account_circle</md-icon>\n        <h3 class=\"md-headline\">{{ employee.surname }}</h3>\n        <p class=\"md-title\">{{ employee.firstname }} {{ employee.patronymic }}</p>\n        <span class=\"md-caption\">{{ employee.birthday | date:\'dd.MM.yyyy\' }}</span>\n    </div>\n    <div layout=\"column\" layout-padding layout-margin class=\"employee-detail_info\">\n        <div class=\"md-whiteframe-2dp\" ng-if=\"employee.phones.length || employee.emails.length\">\n            <div class=\"employee-detail_contacts\">\n                <h2 class=\"md-title\">Контактные данные</h2>\n                <md-list>\n                    <md-list-item class=\"md-1-line\" ng-repeat=\"phone in employee.phones\">\n                        <md-icon ng-if=\"$first\">phone</md-icon>\n                        <p ng-class=\"{\'pb-offset\': !$first}\">{{ phone.number | formatPhone }}</p>\n                        <p class=\"md-secondary pb-text-muted\">{{ phone.category }}</p>\n                    </md-list-item>\n                    <md-list-item class=\"md-1-line\" ng-repeat=\"email in employee.emails\">\n                        <md-icon ng-if=\"$first\">email</md-icon>\n                        <p ng-class=\"{\'pb-offset\': !$first}\">{{ email.email }}</p>\n                        <p class=\"md-secondary pb-text-muted\">{{ email.category }} </p>\n                    </md-list-item>\n                </md-list>\n            </div>\n        </div>\n\n        <div class=\"md-whiteframe-2dp\" ng-if=\"employee.company\">\n            <h2 class=\"md-title\">Место работы</h2>\n            <md-list ng-if=\"employee.company\">\n                <md-list-item class=\"md-2-line\">\n                    <md-icon>work</md-icon>\n                    <div class=\"md-list-item-text\">\n                        <h4>{{ employee.position }}</h4>\n                        <p>\n                            {{ employee.company.name }}\n                            <md-icon ng-show=\"employee.center.name\">chevron_right</md-icon>\n\n                            {{ employee.center.number }}\n                            <span ng-show=\"employee.center.number && employee.center.name\">&nbsp-&nbsp</span>\n                            {{ employee.center.name }}\n\n                            <md-icon ng-show=\"employee.division.name\">chevron_right</md-icon>\n\n                            {{ employee.division.number }}\n                            <span ng-show=\"employee.division.number && employee.division.name\">&nbsp-&nbsp</span>\n                            {{ employee.division.name }}\n                            &nbsp\n                        </p>\n                    </div>\n                </md-list-item>\n            </md-list>\n        </div>\n    </div>\n</div>\n");
$templateCache.put("employees/directives/templates/employees-list-item.html","<div layout=\"row\" layout-padding layout-align=\"start center\" class=\"employees-list-item\">\n    <div flex=\"33\">\n        <h4 class=\"md-subhead\">{{ employee.surname }} {{ employee.firstname }} {{ employee.patronymic }}</h4>\n        <p class=\"md-caption pb-text-muted\">{{ employee.position }}</p>\n    </div>\n    <div layout=\"row\" class=\"employee-list-item_contacts\" flex=\"40\">\n        <md-list flex>\n            <md-list-item ng-repeat=\"phone in employee.phones\" ng-show=\"$even\">\n                <md-tooltip md-direction=\"left\">{{ phone.category }}</md-tooltip>\n                <p>{{ phone.number | formatPhone }}</p>\n            </md-list-item>\n        </md-list>\n        <md-list flex>\n            <md-list-item ng-repeat=\"phone in employee.phones\" ng-show=\"$odd\">\n                <md-tooltip md-direction=\"left\">{{ phone.category }}</md-tooltip>\n                <p>{{ phone.number | formatPhone }}</p>\n            </md-list-item>\n        </md-list>\n    </div>\n    <div class=\"employee-list-item_contacts\">\n        <md-list>\n            <md-list-item ng-repeat=\"email in employee.emails\">\n                <md-tooltip md-direction=\"left\">{{ email.category }}</md-tooltip>\n                <p>{{ email.email }}</p>\n            </md-list-item>\n        </md-list>\n    </div>\n    <span flex></span>\n    <div class=\"employee-list-item_company\" ng-show=\"employee.company\">\n        <md-tooltip>\n            {{ employee.company.name }}\n        </md-tooltip>\n        <img ng-src=\"{{ employee.company.logo }}\" alt=\"{{ employee.company.name }}\" />\n        <p class=\"pb-text-muted\">\n            {{ employee.center.number }}\n            <md-icon ng-show=\"employee.division\">chevron_right</md-icon>\n            {{ employee.division.number }}\n        </p>\n    </div>\n</div>\n");}]);