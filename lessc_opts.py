lessc_opts = {
    #each one of the directories to scan should be finished with / (Linux / OSX) or \ (Windows)
    '/media/samba/devel.ulabox.com/htdocs/css/less/': {
        #css path finished with / (Linux / OSX) or \ (Windows)
        'css_path': '/media/samba/devel.ulabox.com/htdocs/css/',
        #cssembed JAR
        'cssembed_path': '/media/samba/lib/cssembed-0.4.5.jar',
        #lessc binary path
        'lessc_bin': 'lessc',
        #java binary path
        'java_bin': 'java'
    },
    '/media/samba/devel.ulabox.com/htdocs/static/less/': {
        'css_path': '/media/samba/devel.ulabox.com/htdocs/static/css/',
        'cssembed_path': '/media/samba/lib/cssembed-0.4.5.jar',
        'lessc_bin': 'lessc',
        'java_bin': 'java'
    }
}
