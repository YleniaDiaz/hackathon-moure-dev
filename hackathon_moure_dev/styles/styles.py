import reflex as rx
from enum import Enum


class Colors(Enum):
    PRIMARY="#BE111F"
    SECONDARY="#FF7364"
    BACKGROUND="#A2A7DE"
    DARK_BACKGROUND="#3A4473"
    WHITE="#FFFFFF"

# Sizes
class Size(Enum):
    SMALL="0.5em"
    DEFAULT="1em"
    BIG="2em",
    IMAGE="10em"


BASE_STYLE = {
    rx.chakra.Button: {
        "display": "block",
        "bg": Colors.PRIMARY,
        "color": Colors.WHITE,
        "_hover": {
            "background_color": Colors.BACKGROUND
        },
        "white_space": "pre-line"
    },
    rx.chakra.Link: {
        "text_decoration": "none",
        "_hover": {}
    }
}


navbar = dict(
    position="sticky",
    bg=Colors.DARK_BACKGROUND,
    padding=Size.SMALL,
    z_index="999",
    top=0
)