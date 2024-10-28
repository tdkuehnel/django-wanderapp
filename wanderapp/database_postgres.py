with open('/etc/wanderapp/wanderapp_dbpw.txt') as f:
    DATABASE_PW = f.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'e_01_wanderapp',
        'USER': 'postgis',
        'PASSWORD': DATABASE_PW,
        'HOST': '127.0.0.1',
        'PORT': '5434',
    }
}

INSTANCE_NAME = "Testumgebung 0.1"
