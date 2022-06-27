from .base import *
from .base import env

#general
SECRET_KEY=env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS=env.list("DJANGO_ALLOWED_HOSTS", default=["*.herokuapp.com"])

#data base
DATABASES["default"]=env.db("DATABASE_URL")
DATABASES["default"]["ATOMIC_REQUESTS"] =True
DATABASES["defautl"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)

#security

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", defautl=True)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
# TODO:
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)

#whitenoise
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"