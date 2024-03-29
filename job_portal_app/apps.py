from django.apps import AppConfig


class JobPortalAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "job_portal_app"

    def ready(self):
        import job_portal_app.signals
