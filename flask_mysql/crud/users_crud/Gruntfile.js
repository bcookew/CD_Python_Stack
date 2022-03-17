module.exports = function(grunt) {

    grunt.initConfig({
        sass: {
            dist: {
                options: {
                    loadPath: ['node_modules/foundation-sites/scss']
                },
                files: {
                    'flask_app/static/css/style.css' : 'flask_app/static/css/style.scss'
                }
            }
        }
    });
    
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.registerTask('default', ['sass']);
    };