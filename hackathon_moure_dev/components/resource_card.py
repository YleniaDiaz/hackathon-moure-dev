import reflex as reflex
import hackathon_moure_dev.styles.styles as styles
from hackathon_moure_dev.components.content_card import content_card

rx = reflex.chakra

def resource_card(img: str, title: str, description: str, annotations: list[str], url: str) -> reflex.Component:
    return rx.card(
        rx.flex(
            reflex.tablet_and_desktop(
                rx.image(src=img,
                    width=styles.Size.IMAGE, 
                    height=styles.Size.IMAGE
                ),
                margin_right=styles.Size.DEFAULT
            ),
            content_card(title, description, annotations, url),
            align="center"
        ),
        as_child=True,
        margin_bottom=styles.Size.DEFAULT
    )
    