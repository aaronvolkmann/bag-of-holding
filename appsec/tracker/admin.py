from django.contrib import admin
from tracker.models import Tag, Application, Environment, EnvironmentLocation, EnvironmentCredentials, Person, Relation, Engagement, Activity, EngagementNote, ActivityNote, ApplicationFileUpload

# Register your models here.

class EnvironmentCredentials(admin.StackedInline):
    model = EnvironmentCredentials
    extra = 0


class EnvironmentInline(admin.StackedInline):
    model = Environment
    extra = 0


class EnvironmentLocationInline(admin.StackedInline):
    model = EnvironmentLocation
    extra = 0


class RelationInline(admin.StackedInline):
    model = Relation
    fields = ['application', 'person', 'role', 'owner', 'notes']
    extra = 0


class EngagementInline(admin.StackedInline):
    model = Engagement
    fieldsets = [
        (None, {'fields': ['application', 'status', 'start_date', 'end_date']}),
        ('Advanced options', {
            'classes': ['collapse'],
            'fields': ['open_date', 'close_date']
        }),
    ]
    extra = 0


class ActivityInline(admin.StackedInline):
    model = Activity
    fieldsets = [
        (None, {'fields': ['activity_type', 'status', 'start_date', 'end_date', 'users']}),
        ('Advanced options', {
            'classes': ['collapse'],
            'fields': ['open_date', 'close_date']
        }),
    ]
    extra = 0


class EngagementNoteInline(admin.StackedInline):
    model = EngagementNote
    extra = 0


class ActivityNoteInline(admin.StackedInline):
    model = ActivityNote
    extra = 0


class ApplicationFileUploadInline(admin.StackedInline):
    model = ApplicationFileUpload
    extra = 0


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']
    search_fields = ['^name']

admin.site.register(Tag, TagAdmin)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'business_criticality', 'platform', 'origin', 'industry', 'external_audience', 'internet_accessible']
    list_filter = ('external_audience', 'internet_accessible')
    inlines = [EnvironmentInline, RelationInline, EngagementInline, ApplicationFileUploadInline]
    search_fields = ['^name']

admin.site.register(Application, ApplicationAdmin)


class EnvironmentAdmin(admin.ModelAdmin):
    fields = ['application', 'environment_type', 'description', 'testing_approved']
    list_display = ['__str__', 'environment_type', 'application', 'testing_approved']
    inlines = [EnvironmentLocationInline, EnvironmentCredentials]

admin.site.register(Environment, EnvironmentAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email', 'phone_work', 'phone_mobile']
    search_fields = ['^first_name', '^last_name', '^email']
    inlines = [RelationInline]

admin.site.register(Person, PersonAdmin)


class EngagementAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['application', 'status', 'start_date', 'end_date']}),
        ('Advanced options', {
            'classes': ['collapse'],
            'fields': ['open_date', 'close_date']
        }),
    ]
    list_display = ['__str__', 'start_date', 'end_date', 'status', 'application']
    inlines = [ActivityInline, EngagementNoteInline]

admin.site.register(Engagement, EngagementAdmin)


class ActivityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['engagement', 'activity_type', 'status', 'start_date', 'end_date']}),
        ('Advanced options', {
            'classes': ['collapse'],
            'fields': ['open_date', 'close_date']
        }),
    ]
    list_display = ['__str__', 'start_date', 'end_date', 'status', 'activity_type']
    inlines = [ActivityNoteInline]

admin.site.register(Activity, ActivityAdmin)