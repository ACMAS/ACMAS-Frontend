from django_components import component


@component.register("icon")
class Icon(component.Component):
    template_name = "icon/icon.html"

    def get_context_data(self, icon, icon_type, icon_class):
        return {
            "icon": icon,
            "icon_type": icon_type,
            "icon_class": icon_class,
        }

# {% component "icon" icon="" icon_type="" icon_class="" %}
# icon: "information-circle", ... (same naming as the website: https://heroicons.com/)
# icon_type: "outline", "solid", "mini"
# icon_class: defaults with "w-5 h-5", you can add other classes for tailwind "..."

# NOTE need to load following line at the top of component's html to do nested components
# {% load component_tags %}