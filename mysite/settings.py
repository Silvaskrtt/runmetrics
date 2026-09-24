import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Define o diretório base do projeto (dois níveis acima deste arquivo)
BASE_DIR = Path(__file__).resolve().parent.parent

# Adiciona o diretório 'apps' ao PATH do Python para permitir importações dos apps customizados
sys.path.insert(0, str(BASE_DIR / 'apps'))

# ============================================================================
# CONFIGURAÇÕES PRINCIPAIS DO DJANGO
# ============================================================================

# Chave secreta da aplicação (obtida das variáveis de ambiente)
SECRET_KEY = os.getenv("SECRET_KEY")

# Modo de depuração (True apenas em desenvolvimento)
DEBUG = True

# Hosts permitidos para acessar a aplicação (vazio em desenvolvimento)
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Django-allauth - Autenticação social e gerenciamento de contas
    'django.contrib.sites', # Framework de sites do Django (requerido pelo allauth)
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # Apps customizados do projeto
    'accounts',
    'goals.apps.GoalsConfig',
    'metrics.apps.MetricsConfig',
    'records.apps.RecordsConfig',
    'workouts.apps.WorkoutsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # middleware do Django-allauth (gerencia Autenticação e contas)
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # SGBD: PostgreSQL
        'NAME': os.getenv('DB_NAME'),               # Nome do banco de dados
        'USER': os.getenv('DB_USER'),               # Usuário do banco
        'PASSWORD': os.getenv('DB_PASSWORD'),       # Senha do banco
        'HOST': os.getenv('DB_HOST'),               # Host do banco de dados
        'PORT': os.getenv('DB_PORT'),               # Porta do banco
        'OPTIONS': {
            'client_encoding': 'UTF8',              # Codificação UTF-8 para compatibilidade com caracteres acentuados
        },
    }
}


# Password validation

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


# ============================================================================
# INTERNACIONALIZAÇÃO E LOCALIZAÇÃO
# ============================================================================

# Idioma padrão: Português Brasileiro
LANGUAGE_CODE = 'pt-br'

# Fuso horário padrão
TIME_ZONE = 'America/Sao_Paulo'

# Habilita sistema de internacionalização
USE_I18N = True

# Habilita suporte a timezone
USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = 'static/'


# Email

MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}
