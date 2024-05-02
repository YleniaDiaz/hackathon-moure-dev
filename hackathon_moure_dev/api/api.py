
def resource_list() -> dict:
    resource1 = [
        1,
        "/img/python.svg", 
        "Curso de python con Reflex (Nivel básico)", 
        """Este curso realizado por @mouredev nos enseña a desarrollar una web básica usando Python y Reflex""",
        ["python"],
        "https://www.youtube.com/watch?v=n2YrGsXJC6Y"
    ]
    
    resource2 = [
        2,
        "/img/diagram-project.svg", 
        "Patrones de diseño", 
        """Esta web recoge los distintos patrones de diseño sobre diferentes lenguajes""",
        ["Patrones de diseño", "Diseño"],
        "https://refactoring.guru/es/design-patterns"
    ]

    resource3 = [
        3,
        "/img/java.svg", 
        "Curso de Java", 
        """Esto es un curso de Java""",
        ["Java"],
        "https://refactoring.guru/es/design-patterns"
    ]

    return {"resources": [resource1, resource2, resource3]}
