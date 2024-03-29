from django_components import component


@component.register("field")
class Field(component.Component):
    template_name = "field/field.html"

    def get_context_data(self, placeholder, name, component_type, icon_name):
        return {
            "placeholder": placeholder,
            "name": name,
            "component_type": component_type,
            "icon_name": icon_name,
        }
