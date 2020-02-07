daemon = False
cmdir = '/src/instagram/app'
bind = 'unix:/run/instagram.sock'
accesslog = '/var/log/gunicorn/instagram-access.log'
errorlog = '/var/log/gunicorn/instagram-error.log'
capture_output = True