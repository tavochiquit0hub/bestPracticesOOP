class Alumno:
    def __init__(self):
        # Constructor vacío: atributos privados sin valores iniciales
        self.__nombre = None
        self.__apellido_paterno = None
        self.__apellido_materno = None
        self.__no_control = None
        self.__semestre = None

    # Métodos para establecer (set) los valores de los atributos
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    # Métodos para obtener (get) los valores de los atributos
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre

#Crea diccionario
registro_alumnos = {}

#Ingresar 3 nombres
for i in range (3):
    print(f"\n Ingresa los datos del alumno {i+1}:")
    nombre = input("Ingresa el nombre:")
    apellido_paterno = input("Ingresa el apellido paterno:")
    apellido_materno = input("Ingresa el apellido materno:")
    no_control = input("Ingresa el numero de control del alumno:")
    semestre = input("Ingresa el semestre:")

    #Creamos el objeto Alumno y le asignamos los valores ingresados
    registro_alumno = Alumno()
    registro_alumno.set_nombre(nombre)
    registro_alumno.set_apellido_paterno(apellido_paterno)
    registro_alumno.set_apellido_materno(apellido_materno)
    registro_alumno.set_no_control(no_control)
    registro_alumno.set_semestre(semestre)

    #Registrar los datos en el diccionario
    registro_alumnos[f"Alumno_{i+1}"] = registro_alumno

#Mostrar la informacion
print(f"\nInformacion capturada:")
for i in range (3):
    alumno_key = f"Alumno_{i+1}"
    alumno_obj = registro_alumnos[alumno_key]
    print(f"{alumno_key}: {alumno_obj.get_nombre()}, {alumno_obj.get_apellido_paterno()}, {alumno_obj.get_apellido_materno()}, {alumno_obj.get_no_control()}, Semestre {alumno_obj.get_semestre()}")