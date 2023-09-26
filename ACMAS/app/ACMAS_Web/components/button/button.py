from django_components import component

@component.register("button")
class Button(component.Component):
    template_name = "button/button.html"

    def get_context_data(self, text, type):
        return {
            "text": text,
            "type": type,
        }

    class Media:
        css = "button/button.css"
        js = "button/button.js"