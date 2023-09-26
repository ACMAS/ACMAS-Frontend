from django_components import component

@component.register("field")
class Field(component.Component):
    template_name = "field/field.html"

    def get_context_data(self, placeholder, name):
        return {
            "placeholder": placeholder,
            "name": name,
        }

    class Media:
        css = "field/field.css"
        js = "field/field.js"