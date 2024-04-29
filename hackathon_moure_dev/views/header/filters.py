import reflex as reflex
import hackathon_moure_dev.styles.styles as styles

rx = reflex.chakra

def filters() -> reflex.Component:
    return rx.box(
        rx.form(
            rx.vstack(
                rx.input(
                    name="search",
                    placeholder="Buscar...",
                    type="search",
                    radius="large"
                ),
                rx.hstack(
                    rx.select(
                        ["Python", "Java", "JavaScript", "SQL", "Ruby"],
                        placeholder="Lenguaje",
                        label="Lenguaje",
                    ),
                    rx.select(
                        ["Front-end", "Back-end", "Full-stack", "BBDD", "API"],
                        placeholder="Tipo",
                        label="Lenguaje",
                    ),
                    width="100%"
                )
            )
        ),
        margin=styles.Size.SMALL,
        width="75%"
    )