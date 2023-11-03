from django_components import component


@component.register("dropdown_profile")
class dropdown_profile(component.Component):
    template_name = "dropdown_profile/dropdown_profile.html"



# {% component "dropdown_profile" profile_icon="" %}
# 

# NOTE need to load following line at the top of component's html to do nested components
# {% load component_tags %}