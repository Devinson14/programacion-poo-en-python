class Botella:
    
    # 2. Crear el Constructor
    def __init__(self, material, capacidad, forma, diseno, tapa, grabados):
        # 3. Crear Atributos
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseno = diseno
        self.tapa = tapa
        self.grabados = grabados
    
    # 4. Crear Métodos (lleno -> parámetros / Recibir datos)
    def contener_liquidos(self, cantidad):
        print(f"Conteniendo {cantidad}L de líquido en la botella")
    
    def facilitar_vertido(self):
        print("Facilitando el vertido del líquido")
    
    def cierre_hermetico(self, estado):
        print(f"Botella {estado} herméticamente con tapa {self.tapa}")
    
    def transporte(self, destino):
        print(f"Transportando botella a {destino}")
    
    def manejo(self):
        print(f"Manejando botella de forma {self.forma}")
    
    def compatibilidad_bebidas_calientes_frias(self, tipo_bebida):
        print(f"Compatible con bebidas {tipo_bebida}")
    
    def reutilizacion(self):
        print("Botella lista para reutilización")
    
    def transparencia(self):
        print(f"Transparencia del diseño: {self.diseno}")
    
    # 7. Retorno -> Almacenamiento de datos
    def mostrar_info(self):
        info = f"""
Material: {self.material}
Capacidad: {self.capacidad}L
Forma: {self.forma}
Diseño: {self.diseno}
Tapa: {self.tapa}
Grabados: {self.grabados}
"""
        return info
