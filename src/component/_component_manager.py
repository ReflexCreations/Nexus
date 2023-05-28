import os
from importlib import import_module
from injector import Module, Binder, Injector, SingletonScope

class Component(Module):
    def __init__(self, model_class, view_class, controller_class):
        self.model_class = model_class
        self.view_class = view_class
        self.controller_class = controller_class

    def configure(self, binder: Binder):
        binder.bind(self.model_class, scope=SingletonScope)
        binder.bind(self.view_class, scope=SingletonScope)
        binder.bind(self.controller_class, scope=SingletonScope)

class ComponentsModule(Module):
    def __init__(self, components):
        self.components = components

    def configure(self, binder: Binder):
        for component in self.components:
            binder.install(component)

component_directories = [d for d in os.listdir(os.path.dirname(__file__)) if os.path.isdir(os.path.join(os.path.dirname(__file__), d))]
components = []

for component_directory in component_directories:
    try:
        component_module = import_module(f"components.{component_directory}")
        model_class = getattr(component_module, "Model", None)
        view_class = getattr(component_module, "View", None)
        controller_class = getattr(component_module, "Controller", None)
        if model_class and view_class and controller_class:
            component = Component(model_class, view_class, controller_class)
            components.append(component)
        else:
            print(f"Invalid component: {component_directory}")
    except Exception as e:
        print(f"Error building component {component_directory}: {str(e)}")

def setup_injector():
    injector = Injector(modules=[ComponentsModule(components)])
    return injector