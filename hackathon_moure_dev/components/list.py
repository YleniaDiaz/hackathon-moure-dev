import reflex as reflex
from hackathon_moure_dev.components.resource_card import resource_card
import hackathon_moure_dev.styles.styles as styles

rx = reflex.chakra

def list() -> reflex.Component:
    return rx.box(
        resource_card(
            "/img/python.svg",
            "Curso de Python - 6h", 
            """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
            nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa 
            qui officia deserunt mollit anim id est laborum.""",
            ["python"],
            "https://www.youtube.com/watch?v=n2YrGsXJC6Y"
        ),
        resource_card(
            "/img/diagram-project.svg",
            "Patrones de diseño",
            """Bacon ipsum dolor amet shank bresaola bacon picanha pig. 
            Short loin filet mignon hamburger, pig brisket frankfurter 
            cupim short ribs meatloaf sirloin biltong strip steak prosciutto 
            beef ribs. Buffalo shoulder tri-tip jowl pancetta ground round swine. 
            Chicken tenderloin capicola, swine sirloin biltong leberkas ground 
            round pancetta salami venison pork loin kevin.""",
            ["Patrones de diseño", "Diseño"],
            "https://refactoring.guru/es/design-patterns"
        ),
        resource_card(
            "/img/java.svg",
            "Java",
            """Esta descripción es más corta""",
            ["Java", "Backend"],
            "https://refactoring.guru/es/design-patterns"
        )
    )