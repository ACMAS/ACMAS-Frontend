from django_components import component


@component.register("alert")
class Button(component.Component):
    template_name = "alert/alert.html"

    def get_context_data(self, component_type, color, text):
        return {
            "component_type": component_type,
            "color": color,
            "text": text,
        }
