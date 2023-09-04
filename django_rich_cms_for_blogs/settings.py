

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m&jdb4c-tm@=86pvb656hhj7xz61^di*9+hos44sa3)o5!-#96'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps', # Responsável para gerar sitemaps de um blog ou site
    'ckeditor', # Editor de texto rico para criação de postagens
    'ckeditor_uploader', # Um plugin adicional que permite termos as funções mais avançadas para carregar arquivos
    'autoslug', # Uma biblioteca que criar slugs automáticos para cada página
    'demo', # Aqui é o nosso app demo! OBS: Você pode alterar isso aqui para o seu aplicativo desejado
    
]

# == ID DO SITE == 
SITE_ID = 1 # Defina aqui as IDs do seu site caso tenha mais de um aplicativo em seu projeto!

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_rich_cms_for_blogs.urls'

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
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_rich_cms_for_blogs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'Africa/Maputo' # Aqui estou usando fuso horário de Moçambique para fins exemplares, lembrando que você pode alterar de acordo com a sua localidade.

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# == DEFINIÇÃO DOS DIRETÓRIOS PARA ARQUIVOS UPADOS COM CKEDITOR ==

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGEM_BACKEND = 'pillow'

# == CONFIGURAÇÃO PARA ADICIONAR PLUGINS EXTRAS PARA O CKEDITOR
CKEDITOR_CONFIGS = {
	'default':{
		'toolbar':'full',
		'removePlugins':'',
		'extraPlugins': ','.join(
			[
				'codesnippet', 'youtube',
			]
		)
		
	}
	
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
