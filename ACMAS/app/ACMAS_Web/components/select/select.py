from django_components import component

@component.register("select")
class Field(component.Component):
    template_name = "select/select.html"

    def get_context_date(self, name, options, placeholder):
        return {
            "name": name,
            "options": options,
            "placeholder": placeholder,
        }

    class Media:
        css = "select/select.css"
        js = "select/select.js"
