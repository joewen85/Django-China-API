from .common import *

DEBUG = False
ALLOWED_HOSTS = ['.dj-china.org', 'localhost', '127.0.0.1', '0.0.0.0']
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# 生产环境使用 MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DJANGO_DATABASE_NAME'],
        'USER': os.environ['DJANGO_DATABASE_USER'],
        'PASSWORD': os.environ['DJANGO_DATABASE_PASSWORD'],
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

# 邮件配置，使用腾讯云企业邮箱
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_USE_LOCALTIME = True
EMAIL_HOST_USER = 'master@dj-china.org'
EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_EMAIL_HOST_PASSWORD', 'fallback_value')

# Default email address to use for various automated correspondence from the site manager(s).
DEFAULT_FROM_EMAIL = 'Django中文社区 <%s>' % EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
