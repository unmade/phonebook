var gulp = require('gulp'),
    concat = require('gulp-concat'),
    less = require('gulp-less'),
    minifyCss = require('gulp-minify-css'),
    templateCache = require('gulp-angular-templatecache'),
    uglify = require('gulp-uglify'),
    path = require('path');

var pathToSrc = 'src/',
    pathToBuild = 'build/',
    pathToStatic = '../backend/phonebook/static/',
    pathToLess = pathToSrc + 'less/**/*.less'
    paths = {
        dependenciesCss: [
            'bower_components/angular-material/angular-material.min.css'
        ],
        dependenciesScripts: [
            'bower_components/jquery/dist/jquery.min.js',
            'bower_components/angular/angular.min.js',
            'bower_components/angular-resource/angular-resource.min.js',
            'bower_components/angular-route/angular-route.min.js',
            'bower_components/angular-animate/angular-animate.min.js',
            'bower_components/angular-aria/angular-aria.min.js',
            'bower_components/angular-material/angular-material.min.js',
            'bower_components/ngInfiniteScroll/build/ng-infinite-scroll.min.js'
        ],
        appStyles: [
            pathToSrc + 'less/main.less'
        ],
        appScripts: [
            pathToSrc + 'js/app/**/*.module.js',
            pathToSrc + 'js/app/**/*.js',
            pathToBuild + 'js/templates/*.js'
        ],
        partials: [
            pathToSrc + 'js/app/**/*.html',
            '!' + pathToSrc + 'js/app/**/*.directive.html'
        ],
        companiesTemplates: [pathToSrc + 'js/app/companies/**/*.directive.html'],
        employeesTemplates: [pathToSrc + 'js/app/employees/**/*.directive.html'],
        feedbackTemplates: [pathToSrc + 'js/app/feedback/**/*.directive.html']
    };


gulp.task('dependencies-css', function() {
    return gulp.src(paths.dependenciesCss)
        .pipe(concat('dependencies.min.css'))
        .pipe(gulp.dest('build/css'));
});


gulp.task('dependencies-scripts', function() {
  return gulp.src(paths.dependenciesScripts)
    .pipe(concat('dependencies.min.js'))
    .pipe(gulp.dest('build/js'));
});


gulp.task('app-less', function () {
  return gulp.src(paths.appStyles)
    .pipe(less({
      paths: [ path.join(__dirname, 'less', 'includes') ]
    }))
    .pipe(concat('pb-app.min.css'))
    .pipe(minifyCss())
    .pipe(gulp.dest('build/css'));
});


gulp.task('copy-partials', function () {
    return gulp.src(paths.partials)
        .pipe(gulp.dest(pathToStatic + 'partials/'));
});


gulp.task('companies-templates', function () {
  return gulp.src(paths.companiesTemplates)
    .pipe(templateCache('pb-app.companies.tmpl.js', {module:'pbApp.companies'}))
    .pipe(gulp.dest('build/js/templates'));
});


gulp.task('employees-templates', function () {
  return gulp.src(paths.employeesTemplates)
    .pipe(templateCache('pb-app.employees.tmpl.js', {module:'pbApp.employees'}))
    .pipe(gulp.dest('build/js/templates'));
});

gulp.task('feedback-templates', function () {
  return gulp.src(paths.feedbackTemplates)
    .pipe(templateCache('pb-app.feedback.tmpl.js', {module:'pbApp.feedback'}))
    .pipe(gulp.dest('build/js/templates'));
});


gulp.task('app-scripts', ['companies-templates', 'employees-templates', 'feedback-templates'], function() {
  return gulp.src(paths.appScripts)
    .pipe(uglify())
    .pipe(concat('pb-app.min.js'))
    .pipe(gulp.dest('build/js'));
});


gulp.task('watch', function() {
  gulp.watch(paths.partials, ['copy-partials']);
  gulp.watch([paths.companiesTemplates, paths.employeesTemplates, paths.feedbackTemplates], ['copy-to-static']);
  gulp.watch(paths.appScripts, ['copy-to-static']);
  gulp.watch(pathToLess, ['copy-to-static']);
});


gulp.task('copy-to-static', [
    'dependencies-css',
    'dependencies-scripts',
    'app-scripts',
    'app-less'
], function() {
    return gulp.src([pathToBuild + '**/*', '!' + pathToBuild + '**/templates/*'])
        .pipe(gulp.dest(pathToStatic))
});


gulp.task('default', [
    'watch',
    'copy-partials',
    'copy-to-static',
]);
