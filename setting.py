INSTALLED_APPS = [
    ...
    'your_app', 
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  
]