import reflex as rx
import hackathon_moure_dev.styles.styles as styles
import hackathon_moure_dev.utils as utils
from hackathon_moure_dev.routes import Route
from hackathon_moure_dev.components.navbar import navbar
from hackathon_moure_dev.components.footer import footer
from hackathon_moure_dev.views.header.filters import filters
from hackathon_moure_dev.views.list.resources import resources
from hackathon_moure_dev.api.api import resource_list

class IndexState(rx.State):
    
    resources: list[tuple] = []

    @rx.var
    def get_resources(self) -> dict:
        self.resources = resource_list()["resources"]

@rx.page(
    route=Route.INDEX.value,
    title=utils.index_title,
    description=utils.index_description,
    meta=utils.index_meta
)
def index() -> rx.Component:
    return rx.chakra.box(
        utils.lang(),
        navbar(),
        rx.chakra.vstack(
            filters(),
            resources(),
            width="100%"
        ),
        #footer()
    )