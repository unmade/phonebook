angular.module("pbApp.feedback").run(["$templateCache", function($templateCache) {$templateCache.put("new-feedback.directive.html","<form name=\"newFeedbackForm\" layout=\"column\" layout-padding style=\"min-width:640px;min-height:480px;\">\n    <md-input-container class=\"md-block\">\n        <label>Представьтесь</label>\n        <input ng-model=\"newFeedback.sender\"\n               name=\"sender\"\n               md-maxlength=\"50\"\n               required\n               autofocus=\"true\">\n        <div ng-messages=\"NewFeedbackForm.sender.$error\">\n            <div ng-message=\"required\">Необходимо указать <b>своё</b> ФИО.</div>\n            <div ng-message=\"md-maxlength\">Убедитесь, что в этом поле не больше 50 символов</div>\n        </div>\n    </md-input-container>\n\n    <md-input-container class=\"md-block\" flex>\n        <label>Текст</label>\n        <textarea ng-model=\"newFeedback.text\"\n                  columns=\"1\"\n                  md-maxlength=\"500\"\n                  rows=\"6\"\n                  name=\"text\"\n                  required>\n        </textarea>\n        <div ng-messages=\"NewFeedbackForm.text.$error\">\n            <div ng-message=\"required\">Поле не может быть пустым!</div>\n            <div ng-message=\"md-maxlength\">Убедитесь, что в этом поле не больше 500 символов</div>\n        </div>\n    </md-input-container>\n    <div layout=\"row\">\n        <span flex></span>\n        <md-button ng-click=\"newFeedback.add()\"\n                   ng-disabled=\"!(newFeedback.sender && newFeedback.text)\"\n                   class=\"md-fab md-primary md-mini\"\n                   aria-label=\"Sent\">\n            <md-icon>send</md-icon>\n        </md-button>\n    </div>\n</form>\n");}]);