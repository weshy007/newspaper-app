from django.contrib import admin
from .models import Article, Comment

# Register your models here.
class CommentInline(admin.StackedInline): # TabularInline(more info in less space) or 
                                        #StackedInline(more info in a larger space).
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
            CommentInline, 
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)



''' It turns out we can with a Django admin feature called inlines
which displays foreign key relationships in a nice, visual way.

There are two main inline views used: TabularInline and StackedInline. The only dif-
ference between the two is the template for displaying information. In a TabularInline
all model fields appear on one line while in a StackedInline each field has its own line.
We’ll implement both so you can decide which one you prefer.
'''