(function() {
    'use strict';

    angular
        .module('pbApp.employees.services')
        .factory('Employee', ['$resource', Employee])
        .factory('EmployeeScroll', ['Employee', EmployeeScroll]);

    function Employee($resource) {
        return $resource('api/employees/employee/:id', {}, {
            query: {method: 'GET', isArray: false}
        })
    };

    function EmployeeScroll(Employee) {
      var EmployeeScroll = function(params) {
        this.results = [];
        this.after = undefined;
        this.params = angular.copy(params) || {};
        this.params.offset = 0;
        this.params.limit = 20;
        this.busy = false;
      };

      EmployeeScroll.prototype.nextPage = function() {
        if (this.busy) return;
        if (this.after === null) return;
        this.busy = true;

        Employee.query(this.params, function(data) {
            this.results = this.results.concat(data.results);
            this.params.offset += this.params.limit;
            this.after = data.next;
            this.busy = false;
        }.bind(this));
      };

      return EmployeeScroll;
    };

})();
