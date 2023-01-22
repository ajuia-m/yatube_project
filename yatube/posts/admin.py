from django.contrib import admin

# Register your models here.
from .models import Post, Group

class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'pub_date', 'author','group') 
    # Добавляем интерфейс для поиска по тексту постов
    list_editable = ('group',)
    search_fields = ('text',) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-' 

class GroupAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'description') 
    search_fields = ('slug', 'title') 
    # Добавляем возможность фильтрации по дате
    list_filter = ('slug', 'title')
    empty_value_display = '-пусто-'


# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
admin.site.register(Post, PostAdmin, Group, GroupAdmin)  