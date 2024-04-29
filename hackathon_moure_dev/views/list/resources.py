import reflex as reflex
from hackathon_moure_dev.components.list import list

rx = reflex.chakra

def resources() -> reflex.Component:
    return rx.box(
        list(),
        width="75%"
    )