from django_components import component


@component.register("dropdown_profile")
class dropdown_profile(component.Component):
    template_name = "dropdown_profile/dropdown_profile.html"


# {% component "dropdown_profile" %}
