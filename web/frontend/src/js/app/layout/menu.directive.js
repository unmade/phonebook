(function() {
    'use strict';

    angular
        .module('pbApp.layout')
        .directive('mainMenu', mainMenu);

    mainMenu.$inject = [];

    function mainMenu() {
        return {
            controller: MainMenuCtrl,
            controllerAs: 'menu',
            restrict: 'AE',
            replace: true,
            templateUrl: 'menu.directive.html'
        }
    }

    MainMenuCtrl.$inject = ['$mdSidenav'];

    function MainMenuCtrl($mdSidenav) {
        var self = this;

        self.pages = [
            {'url': 'employees', name: 'Сотрудники', icon: 'contact_phone'},
            {'url': 'companies', name: 'Организации', icon: 'business'},
            {'url': 'feedback', name: 'Обратная связь', icon: 'feedback'},
        ]

        self.closeMenu = closeMenu;
        self.openMenu = openMenu;

        function closeMenu() {
            $mdSidenav('left-menu').close();
        }

        function openMenu() {
            $mdSidenav('left-menu').toggle();
        }
    }
})();
