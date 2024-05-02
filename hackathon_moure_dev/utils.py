import reflex as rx

# COMÚN
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

#preview = ""
_meta = [
    {"name": "og:type", "content": "website"}
]

# INDEX
index_title = "resources4dev | Recursos"
index_description = "En esta web podrás encontrar recursos interesantes sobre programación."
index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description}
]
index_meta.extend(_meta)

# PROFILE
profile_title = "resources4dev | Perfil"
profile_description = "Registrate en la web y guárdate tus recursos favoritos."
profile_meta = [
    {"name": "og:title", "content": profile_title},
    {"name": "og:description", "content": profile_description}
]
profile_meta.extend(_meta)