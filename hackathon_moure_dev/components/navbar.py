import reflex as reflex
from hackathon_moure_dev.routes import Route
import hackathon_moure_dev.styles.styles as styles

rx = reflex.chakra

def navbar() -> reflex.Component:
    return rx.hstack(
        rx.avatar(src="/resources4dev_logo.png"),
        rx.link(
            rx.button("Recursos", bg=styles.Colors.DARK_BACKGROUND),
            href=Route.INDEX.value,
            margin_left=styles.Size.DEFAULT
        ),
        rx.spacer(),
        reflex.menu.root(
            reflex.menu.trigger(
                rx.flex(
                    rx.avatar(src="/user_avatar.png", alt="Icono de perfil"), 
                    justify="end"
                )
            ),
            reflex.menu.content(
                rx.link(
                    rx.button("Perfil", 
                        bg=styles.Colors.WHITE, 
                        color=styles.Colors.GRAY.value
                    ),
                    href=Route.PROFILE.value,
                    is_external=False
                )
            ),
        ),
        style=styles.navbar
    )