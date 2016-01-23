(function() {
    'use strict';

    angular
        .module('pbApp.companies')
        .factory('companyScroll', companyScroll);

    companyScroll.$inject = ['companyService'];

    function companyScroll(companyService) {
        var CompanyScroll = function(params) {
            this.results = [];
            this.after = undefined;
            this.params = angular.copy(params) || {};
            if (params) {
                this.params.offset = params.offset;
                this.params.limit = params.limit;
            }
            else {
                this.params.offset = 0;
                this.params.limit = 20;
            }

            this.busy = false;
        }

        CompanyScroll.prototype.nextPage = function() {
            if (this.busy) return;
            if (this.after === null) return;
            this.busy = true;

            companyService.query(this.params, function(data) {
                this.results = this.results.concat(data.results);
                this.params.offset += this.params.limit;
                this.after = data.next;
                this.busy = false;
            }.bind(this));
        };

        return CompanyScroll;
    }
})();
