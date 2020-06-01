from django.contrib import admin
from .models import company

def closed(modeladmin, request, queryset):
        queryset.update(comp_status='CLOSED')
        closed.short_description = "Mark selected as closed!"

def inprocess(modeladmin, request, queryset):
        queryset.update(comp_status='IN PROCESS')
        inprocess.short_description = "Mark selected as in process!"

def comingsoon(modeladmin, request, queryset):
        queryset.update(comp_status='COMING SOON')
        comingsoon.short_description = "Mark selected as coming soon!"



class company1(admin.ModelAdmin):
    list_display = ['comp_id','comp_name','job_profile','comp_status','no_of_students_applied',]
    ordering = ['comp_id','comp_name','job_profile','comp_status','no_of_students_applied',]
    actions = [closed,inprocess,comingsoon]
    list_filter=['job_profile','comp_status',]

    save_as = True
    save_on_top = True
    change_list_template = 'admin/change_list_graph_company.html'
admin.site.register(company,company1)