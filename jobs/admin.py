from django.contrib import admin
from jobs.models import Emploi
# Register your models here.

class EmploiAdmin(admin.ModelAdmin):
    
    # def thumbnail(self, object):
    #     return format_html('<img src="{}" width="40">'.format(object.image.url))
    
    # Display columns in horizontal list
    list_display = ('reference','job_title', 'entreprise_name', 'close', )
    
    # Columns having links
    list_display_links = ('reference',)

    # Editable columns
    #list_editable = ('job_title', 'entreprise_name', 'entreprise_location', 'job_type', 'job_type2', 'job_duration', 'description', 'responsabilities', 'qualifications', 'deadline' ,'close',) 

    # Filterable columns
    list_filter = ( 'job_title', 'entreprise_name', 'reference', 'job_type', 'job_duration')

'''
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','email',  'phone', 'content', 'sent_date')
    list_filter = ('name',)
'''

admin.site.register(Emploi, EmploiAdmin)
#admin.site.register(Message, MessageAdmin)