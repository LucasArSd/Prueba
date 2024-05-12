# Importar tus modelos
from models import Usuario

# Crear un nuevo usuario
usuario = Usuario.objects.create(nombre="Ejemplo", email="ejemplo@example.com")

# Consultar todos los usuarios
usuarios = Usuario.objects.all()

# Mostrar los usuarios
for usuario in usuarios:
    print(usuario.nombre, usuario.email)