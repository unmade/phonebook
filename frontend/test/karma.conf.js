module.exports = function(config){
  config.set({

    basePath : '../',

    files : [
      'build/js/dependencies.min.js',
      'bower_components/angular-mocks/angular-mocks.js',
      'build/js/pb-app.min.js',
      'build/js/pb-app.tmpl.js',
      'test/unit/responds/*.js',
      'test/unit/**/*.js',
    ],

    autoWatch : true,

    frameworks: ['jasmine'],

    browsers : ['Chrome'],

    plugins : [
            'karma-chrome-launcher',
            'karma-firefox-launcher',
            'karma-jasmine',
            'karma-junit-reporter',
            ],

    junitReporter : {
      outputFile: 'test_out/unit.xml',
      suite: 'unit'
    }

  });
};
