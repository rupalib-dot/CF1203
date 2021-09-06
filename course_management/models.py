from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Category(models.Model):
    title = models.CharField(_('title'), 
        null = True, 
        max_length=150,
        blank=True, 
        help_text=_('Required. 150 characters or fewer. digits only.'),  
    ) 
    about = models.TextField(_('about'), null = True, blank=True)
    status = models.IntegerField(_('status'),null = True, blank=True)
    category_image = models.ImageField(_('category_image'),null = True,  blank=True, upload_to='category_image/')
    date = models.CharField(_('date'), null = True,  max_length=50, blank=True,) 

    def __str__(self):
        return self.title

class Course(models.Model):
    course_title = models.CharField(_('course_title'), 
        null = True, 
        max_length=250,
        blank=True, 
        help_text=_('Required. 250 characters or fewer. digits only.'),  
    ) 
    category_id = models.IntegerField(_('category_id'),null = True, blank=True)
    author = models.CharField(_('author'),  null = True,  max_length=150, blank=True,) 
    about = models.TextField(_('about'), null = True, blank=True)
    rating = models.IntegerField(_('rating'), null = True, blank=True)
    total_hours = models.CharField(_('total_hours'), max_length=6, null = True, blank=True)
    total_days = models.IntegerField(_('total_days'), null = True, blank=True)
    selling_price = models.CharField(_('selling_price'), max_length=6, null = True, blank=True)
    original_price = models.CharField(_('original_price'), max_length=6, null = True, blank=True)
    status = models.IntegerField(_('status'),null = True, blank=True)
    course_level = models.CharField(_('course_level'), max_length=20, null = True, blank=True)
    bestseller = models.IntegerField(_('bestseller'),null = True, blank=True) 
    course_file = models.FileField(_('course_file'),null = True,  blank=True, upload_to='course_file/')
    date = models.CharField(_('date'), null = True,  max_length=50, blank=True,) 

class Chapter(models.Model):
    chapter_name = models.CharField(_('chapter_name'), 
        null = True, 
        max_length=250,
        blank=True, 
        help_text=_('Required. 250 characters or fewer. digits only.'), 
    ) 
    category_id = models.IntegerField(_('category_id'),null = True, blank=True)
    course_id = models.IntegerField(_('course_id'),null = True, blank=True)
    about = models.TextField(_('about'), null = True, blank=True)
    discussions = models.TextField(_('discussions'), null = True, blank=True)
    bookmarks = models.TextField(_('bookmarks'), null = True, blank=True) 
    status = models.IntegerField(_('status'),null = True, blank=True)
    chapter_file = models.FileField(_('chapter_file'),null = True,  blank=True, upload_to='chapter_file/')
    date = models.CharField(_('date'), null = True,  max_length=50, blank=True,) 

class CourseAlloted(models.Model): 
    category_id = models.IntegerField(_('category_id'),null = True, blank=True)
    course_id = models.IntegerField(_('course_id'),null = True, blank=True)
    user_id = models.IntegerField(_('user_id'),null = True, blank=True)
    course_status = models.IntegerField(_('course_status'),null = True, blank=True)
    date = models.CharField(_('date'), null = True,  max_length=50, blank=True,) 