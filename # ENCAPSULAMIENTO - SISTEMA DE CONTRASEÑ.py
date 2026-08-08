# ENCAPSULAMIENTO - SISTEMA DE CONTRASEÑAS

class Usuario:

    # Constructor
    def __init__(self, contraseña):
        # atributo privado
        self.__contraseña = contraseña

    # Método para cambiar contraseña
    def cambiar_contraseña(self, nueva):

        # Validar mínimo 8 caracteres
        if len(nueva) >= 8:
            self.__contraseña = nueva
            print("Contraseña cambiada correctamente")
        else:
            print("Error: mínimo 8 caracteres")

    # Método para verificar contraseña
    def verificar_contraseña(self, clave):

        if clave == self.__contraseña:
            print("Contraseña correcta")
        else:
            print("Contraseña incorrecta")

# Método principal
def main():

    print("=== SISTEMA DE CONTRASEÑAS ===")
    print()

    # Ingreso de datos
    clave_inicial = input("Ingrese contraseña inicial: ")

    usuario = Usuario(clave_inicial)

    nueva = input("Ingrese nueva contraseña: ")
    usuario.cambiar_contraseña(nueva)

    verificar = input("Ingrese contraseña para verificar: ")
    usuario.verificar_contraseña(verificar)

# Ejecutar programa
main()