from django_components import component

@component.register("button")
class Button(component.Component):
    template_name = "button/button.html"

    def get_context_data(self, text, type, value, name=""):
        return {
            "text": text,
            "type": type,
            "value": value,
            "name": name,
        }
