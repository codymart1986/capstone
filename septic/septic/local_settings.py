DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'septic_company',
        'USER': 'root',
        'PASSWORD': '12password34',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}

SECRET_KEY = 'django-insecure-uv@e-8yepq@h7=1=!6&&lbr4&7c7-_n@m9@t789oew72t60f-+'
