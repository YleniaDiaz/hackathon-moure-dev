import reflex as reflex
from hackathon_moure_dev.components.resource_card import resource_card
import hackathon_moure_dev.styles.styles as styles
from hackathon_moure_dev.api.api import resource_list

rx = reflex.chakra

class ResourceState(reflex.State):
    resources: list[list[str]] = []

    @reflex.var
    def get_resources(self) -> dict:
        self.resources = resource_list()["resources"]


def list() -> reflex.Component:
    return rx.box(
        reflex.foreach(
            ResourceState.resources,
            lambda resource, index: rx.box(
                resource_card(
                    resource[1],
                    resource[2], 
                    resource[3],
                    resource[4],
                    resource[5]
                ),
            ),
        )
    )