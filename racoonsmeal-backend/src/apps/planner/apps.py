from django.apps import AppConfig


class PlannerConfig(AppConfig):
    name = "apps.planner"

    def ready(self):
        import apps.planner.signals
