from django.contrib import admin

from .models import (About, Category, Contact, Course, File, Gallery,
                     Subscriber, Tag, Testimonials)

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'created_at')
    search_fields = ('name', 'email', 'phone', 'message', 'created_at')
    list_filter = ('created_at',)


class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'qualification', 'address', 'updated_at')
    search_fields = ('name',)
    list_filter = ('updated_at',)


class FileInline(admin.TabularInline):
    model = File


class GalleryAdmin(admin.ModelAdmin):
    inlines = [FileInline]
    list_display = ('title',)
    search_fields = ('title',)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'created_at')
    search_fields = ('name', 'message', 'created_at')
    list_filter = ('created_at',)

#  Change logo, title and header of admin site
admin.site.site_header = "Elin Admin"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Testimonials, TestimonialAdmin)
