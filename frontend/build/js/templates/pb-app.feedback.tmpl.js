angular.module("pbApp.feedback").run(["$templateCache", function($templateCache) {$templateCache.put("new-feedback.directive.html","<div>\n\n<md-button class=\"{{ newFeedback.buttonClass }}\" aria-label=\"Add\"\n           ng-click=\"newFeedback.showNewFeedbackDialog($event)\">\n    <md-icon>create</md-icon>\n    <md-tooltip>Новое сообщение</md-tooltip>\n</md-button>\n\n<script type=\"text/ng-template\" id=\"new-feedback-dialog.tmpl.html\">\n    <md-dialog aria-label=\"New Feedback\" layout=\"column\" class=\"pb-dialog\">\n        <md-dialog-content flex>\n            <form name=\"newFeedbackForm\" layout=\"column\" layout-padding>\n                <div layout=\"row\" layout-padding>\n                    <h1 class=\"md-title\">Обратная связь</h1>\n                    <span flex></span>\n                    <md-button class=\"md-icon-button\" ng-click=\"nfdCtrl.cancel()\">\n                        <md-icon>close</md-icon>\n                    </md-button>\n                </div>\n\n                <md-input-container class=\"md-block\">\n                    <label>Представьтесь</label>\n                    <input ng-model=\"nfdCtrl.feedback.sender\"\n                           name=\"sender\"\n                           md-maxlength=\"50\"\n                           required\n                           autofocus=\"true\">\n                    <div class=\"pb-input-hint\">Введите Вашу фамилию и инициалы</div>\n                    <div ng-messages=\"newFeedbackForm.sender.$error\">\n                        <div ng-message=\"required\">Необходимо указать <b>свою</b> фамилию.</div>\n                        <div ng-message=\"md-maxlength\">Убедитесь, что в этом поле не больше 50 символов</div>\n                    </div>\n                </md-input-container>\n\n                <md-input-container class=\"md-block\" flex>\n                    <label>Текст</label>\n                    <textarea ng-model=\"nfdCtrl.feedback.text\"\n                              columns=\"1\"\n                              md-maxlength=\"500\"\n                              rows=\"6\"\n                              name=\"text\"\n                              required>\n                    </textarea>\n                    <div class=\"pb-input-hint\">Введите Ваше сообщение</div>\n                    <div ng-messages=\"newFeedbackForm.text.$error\">\n                        <div ng-message=\"required\">Поле не может быть пустым!</div>\n                        <div ng-message=\"md-maxlength\">Убедитесь, что в этом поле не больше 500 символов</div>\n                    </div>\n                </md-input-container>\n            </form>\n        </md-dialog-content>\n\n        <md-dialog-actions layout-padding>\n            <md-button ng-click=\"nfdCtrl.cancel()\"\n                       class=\"md-raised\"\n                       aria-label=\"Cancel\">\n                Отмена\n            </md-button>\n            <md-button ng-click=\"nfdCtrl.send()\"\n                       ng-disabled=\"!(nfdCtrl.feedback.sender && nfdCtrl.feedback.text)\"\n                       class=\"md-raised md-primary\"\n                       aria-label=\"Send\">\n                Отправить\n            </md-button>\n        </md-dialog-action>\n    </md-dialog>\n</script>\n\n</div>\n");}]);