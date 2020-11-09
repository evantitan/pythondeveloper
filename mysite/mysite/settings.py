import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir))))
SECRET_KEY = '0ps^di56=278+7t^_-nk$#+lh%^^d^eos%d6_mgh0_$9^d3+aj'

PROJECT_ROOT = os.path.join(os.path.abspath(__file__))

#SECURE_HSTS_SECONDS = 31536000   #4
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True   #5
#SECURE_SSL_REDIRECT = True  #it redirect over ssl  #8
#SESSION_COOKIE_SECURE = True   #12
#CSRF_COOKIE_SECURE = True    #16


STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')



DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.43.177']
AUTH_USER_MODEL = 'account.User'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '698030897211-ipfn9lh0f2tc4jeuf0teudhd814r2veu.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'ZNM_h4YWR3nGJM8CxBOt6kuv'

SOCIAL_AUTH_FACEBOOK_KEY = '307756280410313'
SOCIAL_AUTH_FACEBOOK_SECRET = '9a3c8259f21cbd103b3992f44089ac16'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email','user_link']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email, picture.type(large), link'
}
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [
    ('name', 'name'),
    ('email', 'email'),
    ('picture', 'picture'),
    ('link', 'profile_url'),
]


SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend'
)


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'account',
    'social_django',
    'django_social_share',
    'taggit',
    'crispy_forms',
    'bootstrap4',
    'django_summernote',
    'django_extensions',
    'django_user_agents'
]

MIDDLEWARE = [
    'django_user_agents.middleware.UserAgentMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware'
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKENDS = 'django.core.mail.backends.smtp.EmailBackends'
EMAIL_HOST = 'smtp.gmail.com' # mail service smtp
EMAIL_HOST_USER = 'casonjose52@gmail.com' # email id
EMAIL_HOST_PASSWORD = 'get2hell@20203' #password
EMAIL_PORT = 587
EMAIL_USE_TLS = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
X_FRAME_OPTIONS = 'SAEMORIGIN'
#X_FRAME_OPTIONS = 'DENY'

lOGIN_URL = '/account/login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'home'


#CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


#import dj_database_url
#prod_db  =  dj_database_url.config(conn_max_age=500)
#DATABASES['default'].update(prod_db)


# Activate Django-Heroku.
#django_heroku.settings(locals())
