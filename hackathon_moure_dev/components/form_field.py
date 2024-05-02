import reflex as rx
import hackathon_moure_dev.styles.styles as styles

def form_field(name, label, placeholder, value, type, disabled) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input.input(
                    placeholder=placeholder,
                    value=value,
                    type=type,
                    disabled=disabled
                ),
                as_child=True,
            ),
            direction="column",
            spacing="2",
        ),
        name=name,
        margin_bottom=styles.Size.DEFAULT
    )