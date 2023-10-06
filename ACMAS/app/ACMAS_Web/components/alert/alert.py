from django_components import component


@component.register("alert")
class Button(component.Component):
    template_name = "alert/alert.html"

    def get_context_data(self, type, color, text):
        return {
            "type": type,
            "color": color,
            "text": text,
        }
