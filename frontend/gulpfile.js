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
            pathToSrc + 'less/*.less'
        ],
        appScripts: [
            pathToSrc + 'js/*.js',
            pathToSrc + 'js/angular/app.js',
            pathToSrc + 'js/angular/app.config.js',
            pathToSrc + 'js/angular/app.routes.js',

            pathToSrc + 'js/angular/employees/employees.module.js',
            pathToSrc + 'js/angular/employees/employees.controllers.js',
            pathToSrc + 'js/angular/employees/employees.services.js',
            pathToSrc + 'js/angular/employees/directives/*.js',
            //
            pathToSrc + 'js/angular/companies/companies.module.js',
            pathToSrc + 'js/angular/companies/companies.services.js'
        ],
        partials: [pathToSrc + 'js/angular/partials/**/*.html'],
        templates: [pathToSrc + 'js/angular/**/templates/*.html']
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
    .pipe(minifyCss())
    .pipe(gulp.dest('build/css'));
});


gulp.task('copy-partials', function () {
    return gulp.src(paths.partials)
        .pipe(gulp.dest(pathToStatic + 'partials/'));
});


gulp.task('templates', function () {
  return gulp.src(paths.templates)
    .pipe(templateCache('pb-app.tmpl.js', {module:'pbApp.employees.directives'}))
    .pipe(gulp.dest('build/js'));
});


gulp.task('app-scripts', ['templates'], function() {
  return gulp.src(paths.appScripts)
    .pipe(uglify())
    .pipe(concat('pb-app.min.js'))
    .pipe(gulp.dest('build/js'));
});


gulp.task('watch', function() {
  gulp.watch(paths.partials, ['copy-partials']);
  gulp.watch(paths.templates, ['copy-partials']);
  gulp.watch(paths.appScripts, ['copy-to-static']);
  gulp.watch(paths.appStyles, ['copy-to-static']);
});


gulp.task('copy-to-static', ['dependencies-css', 'dependencies-scripts', 'app-scripts', 'app-less'], function() {
    return gulp.src(pathToBuild + '**/*')
        .pipe(gulp.dest(pathToStatic))
});


gulp.task('default', [
    'watch',
    'copy-partials',
    'copy-to-static',
]);
