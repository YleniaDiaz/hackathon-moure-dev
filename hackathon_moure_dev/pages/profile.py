import reflex as rx
import hackathon_moure_dev.styles.styles as styles
import hackathon_moure_dev.utils as utils
from hackathon_moure_dev.routes import Route
from hackathon_moure_dev.components.navbar import navbar
from hackathon_moure_dev.components.form_field import form_field

@rx.page(
    route=Route.PROFILE.value,
    title=utils.profile_title,
    description=utils.profile_description,
    meta=utils.profile_meta
)
def profile() -> rx.Component:
    return rx.chakra.box(
        utils.lang(),
        navbar(),
        rx.chakra.vstack(
            rx.chakra.card(
                rx.chakra.vstack(
                    rx.heading("Mi perfil", margin_bottom=styles.Size.SMALL),
                    rx.form.root(
                        form_field(
                            "name", 
                            "Nombre", 
                            "Nombre", 
                            "Usuario de prueba", 
                            "text", 
                            True
                        ),
                        form_field(
                            "email", 
                            "Email", 
                            "Email", 
                            "example@email.com", 
                            "email", 
                            True
                        ),
                        width= "60%"
                    )
                ),
                width= "60%"
            ),
            margin_top="5%"
        ),
        width= "100%",
        heigth="100%"
    )