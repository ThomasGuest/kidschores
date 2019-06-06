from django.apps import AppConfig


class ChoresConfig(AppConfig):
    name = 'chores'

    def ready(self):
        import chores.signals
