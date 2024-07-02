import matplotlib.pyplot as plt
import networkx as nx

# Crear el grafo
G = nx.DiGraph()

# Añadir nodos y aristas
nodes = {
    "Plan de Vida": ["Visión", "Misión", "Filosofía"],
    "Visión": ["Mejorar mi calidad de vida"],
    "Mejorar mi calidad de vida": ["Bienestar físico y mental", "Crecimiento profesional y personal", "Equilibrio entre trabajo y vida personal"],
    "Misión": ["Estudiante de Ingeniería en Sistemas"],
    "Estudiante de Ingeniería en Sistemas": ["Éxito académico", "Habilidades técnicas y blandas", "Proyectos relevantes", "Networking y colaboraciones"],
    "Filosofía": ["Valores personales", "Métodos y prácticas"],
    "Valores personales": ["Integridad", "Responsabilidad", "Perseverancia", "Innovación"],
    "Métodos y prácticas": ["Planificación y organización", "Aprendizaje continuo", "Adaptabilidad al cambio", "Trabajo en equipo"],
    "Objetivos a Corto Plazo": ["Completar sexto cuatrimestre", "Talleres y cursos extracurriculares", "Rutina de estudio efectiva"],
    "Objetivos a Mediano Plazo": ["Pasantía o trabajo relacionado", "Proyecto personal en sistemas", "Fortalecer red de contactos"],
    "Objetivos a Largo Plazo": ["Graduarme con honores", "Trabajo en empresa tecnológica", "Posgrados o certificaciones"],
    "Plan de Vida": ["Objetivos a Corto Plazo", "Objetivos a Mediano Plazo", "Objetivos a Largo Plazo"]
}

# Añadir nodos y aristas al grafo
for parent, children in nodes.items():
    for child in children:
        G.add_edge(parent, child)

# Dibujar el grafo
plt.figure(figsize=(14, 10))
pos = nx.spring_layout(G, k=0.5)
nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=3000, edge_color="gray", linewidths=1, font_size=10, font_weight='bold', arrowsize=20)

# Mostrar el gráfico
plt.title("Mapa Conceptual: Plan de Vida")
plt.show()
