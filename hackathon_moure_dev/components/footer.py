import reflex as rx
import hackathon_moure_dev.styles.styles as styles

def footer() -> rx.Component:
    return rx.vstack(
        rx.text("Web elaborada para una hackaton"),
        margin_top=styles.Size.DEFAULT,
        bg=styles.Colors.BACKGROUND,
        height="100%"
    )