from estudiantes import estudiantes

class App:
    def __init__(self):
        self.main()

    def borrarPantalla(self):
        print("\033c")

    def esperarTecla(self):
        input("Espere porfavor... ")

    def menu_acciones(self, tipo):
        print(f"\n\t\t\t...::: Menu de {tipo} :::... \n")
        opcion = input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Salir \n\t\t Elige una opcion: ").strip()
        return opcion

    def respuesta_sql(self, respuesta):
        if respuesta:
            input("\n\t ✅ ¡Accion Realizada con Exito! ✅ \n")
        else:
            input("\n\t ❌ ¡Opcion invalida! Oprima cualquier tecla para continuar... ❌ \n")

    def datos_coche(self, tipo):
        self.borrarPantalla()
        print(f"\n\t ...Ingresar los datos del {tipo}...")
        estudiantitos = {}
        estudiantitos['nombre'] = input("nombre: ").upper().strip()
        estudiantitos['nota'] = input("Calificacion: ").upper().strip()
        return estudiantitos
#Metodos estaticos
    def menu_coches(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            opcion=self.menu_acciones("Estudiantes")
            match opcion:
                case '1':
                #crear objeto

                    #coche1= cochesBD.CochesBD("Nissan", "Azul", "2020", 180, 150, 6)
                    #respuesta=coche1.insertar()
                    #self.respuesta_sql(respuesta)
                
                    Estudiantitos = self.datos_coche("Estudiante")      
                    estudiante1 = estudiantes.Estudiantes(Estudiantitos['nombre'], Estudiantitos['nota'])                    
                    estudiante1 = estudiantes.Estudiantes(Estudiantitos['nombre'], Estudiantitos['nota'])
                    respuesta = estudiante1.insertar()
                    self.respuesta_sql(respuesta)
                    del estudiante1
                case "2":
                    self.borrarPantalla()
                    id=input("Ingresa el ID del estudiante a eliminar: ").strip()
                    respuesta = estudiantes.Estudiantes.eliminar(id)
                    self.respuesta_sql(respuesta)
                    del estudiante1
                case "3":
                    id=input("Ingresa el ID del estudiante a actualizar: ").strip()
                    Estudiantitos = self.datos_coche("Estudiante")      
                    estudiante1 = estudiantes.Estudiantes(Estudiantitos['nombre'], Estudiantitos['nota'])                    
                    coche1 = estudiantes.Estudiantes(Estudiantitos['nombre'], Estudiantitos['nota'])
                    respuesta = estudiante1.actualizar(id)
                    self.respuesta_sql(respuesta)
                    del estudiante1
                case "4":
                    self.borrarPantalla()
                    estudiante1=estudiantes.Estudiantes('',0)
                    registros=estudiante1.consultar()
                    if len(registros) > 0:
                        numero_estudiantes=1
                        for fila in registros:
                            print(f"Estudiante #{numero_estudiantes}\n\t ID: {fila[0]}\n\t nombre: {fila[1]}\n\t calificacion: {fila[2]}")
                            numero_estudiantes += 1
                            self.esperarTecla()
                    else:
                        print("\n\n\t ¡No existen datos que mostrar por el momento ...!")
                    del estudiante1
                case "5":
                    opcion = False
                case _:
                    input("\n\t ... Opcion invalida, vuelve a intentarlo por favor ...") 

    def main(self):
        opcion=True
        while opcion:
                    self.borrarPantalla()
                    opcion = input("\n\t\t\t...:: M E N U  P R I N C I P A L ::...\n\n\t 1.- Estudiantes \n\t 2.- Salir \n \t\t Elige una opcion: ").strip().lower()
                    match opcion:
                        case "1":
                            self.borrarPantalla()
                            self.menu_coches()
                            print("Menu de coches")
                        case "2":
                            self.borrarPantalla()
                            input("Saliendo del sistema... ")
                            opcion = False
                        case _:
                            input("\n\t ... Opcion invalida, vuelve a intentarlo por favor ... ")

if __name__=="__main__":
    app=App()
