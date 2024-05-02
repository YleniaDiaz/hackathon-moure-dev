import reflex as rx
import hackathon_moure_dev.styles.styles as styles
from hackathon_moure_dev.api.api import resource_list
from hackathon_moure_dev.pages.index import index
from hackathon_moure_dev.pages.profile import profile

class State(rx.State):
    pass

app = rx.App(
    style = styles.BASE_STYLE
)

app.api.add_api_route("/", resource_list)
