import reflex as reflex
import hackathon_moure_dev.styles.styles as styles

rx = reflex.chakra

def content_card(title: str, description: str, annotations: list[str], url: str) -> reflex.Component:
    return rx.flex(
        rx.heading(title, margin_bottom=styles.Size.SMALL),
        rx.hstack(
            reflex.foreach(
                annotations,
                lambda index: rx.badge(
                    rx.flex(
                        rx.text(f"#{index}"),
                    ),
                    max_width="fit-content",
                    bg=styles.Colors.BACKGROUND,
                    radius="large",
                    padding="0.2em"
                ),
            ),
            margin_bottom=styles.Size.SMALL,
        ),
        rx.text(description, margin_bottom=styles.Size.DEFAULT),
        rx.flex(
            rx.button(
                rx.icon(tag="star", margin_right=styles.Size.SMALL),
                "Añadir a favoritos",
                bg=styles.Colors.SECONDARY,
                margin_right=styles.Size.SMALL
            ),
            rx.link(
                rx.button("Ir al recurso"), 
                href=url,
                is_external=True
            ),
            align="center",
            justify="end"
        ),
        direction="column",
        width="100%"
    )
    