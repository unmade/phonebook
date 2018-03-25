from django.apps import AppConfig


class SearchConfig(AppConfig):
    name = 'search'

    def ready(self):
        from elasticsearch_dsl import connections
        connections.create_connection(hosts=['elasticsearch'])
