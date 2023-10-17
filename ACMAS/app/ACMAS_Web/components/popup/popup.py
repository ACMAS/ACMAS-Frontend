from django_components import component


@component.register("popup")
class Popup(component.Component):
    template_name = "popup/popup.html"

    def get_context_data(
        self, component_type, behavior, position, icon_name, color, text
    ):
        return {
            "component_type": component_type,
            "behavior": behavior,
            "position": position,
            "icon_name": icon_name,
            "color": color,
            "text": text,
        }
    
# {% component "popup" component_type="" behavior="" position="" icon_name="" color="" text="" %}

# component_type: "alert", "toast"
# behavior: "dismiss" (click to dismiss), "fade" (timed dismiss),
# position: "top", "bottom", "center" (cause alert to be focused),
# icon_name: "information-circle", "exclamation-circle", "check-circle", "exclamation-triangle"
# color: "blue", "red", "green", "yellow", "gray", any color given in tailwind for both bg- and text-
# text: "..."

# NOTE that all parameters have to be included within a component to avoid error during template rendering
