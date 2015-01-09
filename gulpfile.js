var gulp = require('gulp'),
	compass = require('gulp-compass'),
	browserSync = require('browser-sync'),
	path = require('path'),
	reload = browserSync.reload;

var static_dir = './stoppaniarch/static',
	assets_dir = './stoppaniarch/assets',
	templates_dir = './stoppaniarch/templates';

gulp.task('compass', function() {
	return gulp.src(path.join(assets_dir, '**/*.scss'))
		.pipe(compass({
			css: path.join(static_dir, 'styles'),
			sass: path.join(assets_dir, 'scss'),
		}))
		.pipe(gulp.dest(path.join(static_dir, 'styles')))
		.pipe(reload({stream:true}));
});

gulp.task('serve', function() {
	browserSync({
		open: false,
		online: false,
		ghostMode: false,
		server: {baseDir: '__nonexisting__'},
	});
});

gulp.task('watch', ['compass', 'serve'], function () {
	gulp.watch(path.join(templates_dir, '**/*.html'), reload);
	gulp.watch(path.join(assets_dir, '**/*.scss'), ['compass']);
});
