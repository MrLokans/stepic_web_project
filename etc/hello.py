CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web/ask',
    # 'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:8000',
        '--access-logfile gunicorn_acc.log',
        '--error-logfile gunicorn_err.log',
        '--workers=4',
        '--timeout=60',
        'ask.wsgi:application',
    ),
}