from django.contrib import admin
from .models import Post

# 💻 Registramos nuestro modelo de Post
# para que se muestre en nuestro sitio de administración
admin.site.register(Post)
