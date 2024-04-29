import reflex as rx
import hackathon_moure_dev.styles.styles as styles
from hackathon_moure_dev.components.navbar import navbar
from hackathon_moure_dev.components.footer import footer
from hackathon_moure_dev.views.header.filters import filters
from hackathon_moure_dev.views.list.resources import resources

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.chakra.box(
        navbar(),
        rx.chakra.vstack(
            filters(),
            resources(),
            width="100%"
        ),
        #footer()
    )

app = rx.App(
    style = styles.BASE_STYLE
)
app.add_page(index)
#app.compile()
