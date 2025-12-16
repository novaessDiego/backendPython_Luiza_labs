class Bicicleta: 
    def __init__(self, valor, cor, modelo, ano):
        self.valor = valor
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def buzinar(self):
        return "Buzina: Biiiiii"
    
    def parar(self):
        return "Parando a bicicleta"
    
    def acelerar(self):
        return "Acelerando a bicicleta"
    
    def trocar_marcha(self, marcha):
        if marcha < 1:
            return "Marcha inválida. A marcha mínima é 1."  
        elif marcha > 10:
            return "Marcha inválida. A marcha máxima é 10."     
        return f"Trocando para a marcha {marcha}"
    
        
    def __str__(self):
        return f"{self.__class__.__name__} : {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
b1 = Bicicleta(1200, "vermelha", "caloi", 2020)
print(b1)
print(b1.buzinar())
print(b1.parar())
print(b1.acelerar())