import importlib

from django.conf import settings

PLUGINS = {}

for plugin in settings.PLUGINS.get("MONITORING_SOURCES").get("INSTALLED", []):
    full_module_name = "monitoring.plugins.sources.{}".format(plugin.lower())
    mymodule = importlib.import_module(full_module_name)
    PLUGINS[plugin] = mymodule.Plugin()