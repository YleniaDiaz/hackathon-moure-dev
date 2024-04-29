import reflex as reflex
import hackathon_moure_dev.styles.styles as styles

rx = reflex.chakra

def navbar() -> reflex.Component:
    return rx.hstack(
        rx.avatar(src="/alltech_logo.png"),
        rx.text("Recursos", 
                color=styles.Colors.WHITE,
                margin_left=styles.Size.DEFAULT,
                padding_top=styles.Size.SMALL
        ),
        rx.spacer(),
        rx.flex(
            rx.avatar(src="/user_avatar.png", alt="Icono de perfil"), 
            justify="end"
        ),
        style=styles.navbar
    )