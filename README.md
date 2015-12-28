# Material Design Date Picker

![Date picker image](demo/images/picker.png?raw=true "Title")

This module is a simple date picker for those who writes project with [Angular Material](https://material.angularjs.org/latest/#/) and wants an alternative date picker to the standard one. It built with [Angular Material](https://material.angularjs.org/latest/#/) and [Moment.js](http://momentjs.com/). I used [lumX's](http://ui.lumapps.com/directives/date-picker) date picker controller as a basement for my own one. Design was inspired by [Google Material Design specifications](https://www.google.com/design/spec/components/pickers.html#pickers-date-pickers).

* [Demo](#demo)
* [License](#license)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [API Documentation](#api-documentation)
* [Contributing](#contributing)

## Demo

Live demo available [here](http://codepen.io/anon/pen/RrwYoz).

## License

This software is provided free of change and without restriction under the [MIT License](LICENSE.md)

## Requirements

[Angular Material](https://material.angularjs.org/latest/#/)

[Moment.js](http://momentjs.com/)

## Installation


This package is installable through the Bower package manager.

```
bower install angular-material-date-picker --save
```

In your `index.html` file, include the data picker module and style sheet

```html
<!-- style sheet -->
<link href="bower_components/angular-material-date-picker/dist/css/am-date-picker_light-theme.css" rel="stylesheet" type="text/css"/>
<!-- module -->
<script type="text/javascript" src="bower_components/angular-material-date-picker/dist/am-date-picker.min.js"></script>
```

Include the `am.date-picker` module as a dependency in your application.

```javascript
angular.module('myApp', ['ngMaterial', 'am.date-picker']);
```

## Usage

**controller**

```javascript
angular
    .module('myApp', [
        'ngMaterial',
        'am.date-picker',
    ])
    .config(['amDatePickerConfigProvider', function(amDatePickerConfigProvider) {
        amDatePickerConfigProvider.setOptions({
            popupDateFormat: 'Do of MMMM',
            calendarIcon: '/static/images/icons/ic_today_24px.svg',
            clearIcon: '/static/images/icons/ic_close_24px.svg',
            nextIcon: '/static/images/icons/ic_chevron_right_18px.svg',
            prevIcon: '/static/images/icons/ic_chevron_left_18px.svg'
        })
    }])
    .controller('MainCtrl', ['$scope', function ($scope) {
        $scope.minDate = new Date('2014-01-05');
        $scope.maxDate = new Date('2014-01-15');
        $scope.date = new Date('2014-01-10');
    }]);
```

> Note that images for icons have to be set globally through the `amDatepickerConfig`.

**markup**

```html
<am-date-picker ng-model="date"
                am-input-date-format="L"
                am-input-label="Pick a Date"
                am-max-date="maxDate"
                am-max-year="2015"
                am-min-date="minDate"
                am-min-year="2000"
                am-popup-date-format="D/M"
                am-today-button="Today"
                am-show-input-icon="true">
</am-date-picker>
```

## API Documentation

All settings can be provided as attributes in the `am-date-picker` or globally configured through the `amDatepickerConfig`.

| Attribute              | Type          | Description |
| :--------------------- | :------------ | :---------- |
| `ng-model`             | `Date Object` | Two-way data-binding date property. |
| `am-allow-clear`       | `Boolean`     | Whether the input could be clear (default: `true`). |
| `am-input-date-format` | `String`      | The format for displayed date in input (default: `LL`). |
| `am-input-label`       | `String`      | The text to display as input label. |
| `am-max-date`          | `Date Object` | Defines the maximum selectable date. |
| `am-min-date`          | `Date Object` | Defines the minimum selectable date. |
| `am-max-year`          | `Number`      | Defines the maximum year displayed in year selection (default: `2020`). |
| `am-min-year`          | `Number`      | Defines the minimum year displayed in year selection (default: `1920`). |
| `am-popup-date-format` | `String`      | The format for displayed date in popup header (default: `ddd, MMM D`). |
| `am-show-input-icon`   | `Boolean`     | Whether to display the calendar icon (default: `false`). |
| `am-today-button`      | `String`      | The text for today button. If not provided the button won't be shown. |

Specific settings that can be globally configured through the `amDatepickerConfig` only.

| Attribute              | Type          | Description |
| :--------------------- | :------------ | :---------- |
| `locale`               | `String`      | Set locale (default: `en`). |
| `calendarIcon`         | `String`      | Path to the calendar icon. |
| `clearIcon`            | `String`      | Path to the clear icon. |
| `nextIcon`             | `String`      | Path to the chevron right icon. |
| `prevIcon`             | `String`      | Path to the chevron left icon. |

> Date formats and locale should correspond MomentJS ones.

## Contributing

If you have an improvement, bug report or request please let me know or post a pull request

See how to [run app locally](demo/README.md).

See how to [run test](test/README.md).
