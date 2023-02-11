# API básica de monitoramento do clima na região de certas cidades determinadas.
# A chave de API foi desativada por motivos de segurança,
# Basta fazer uma nova conta em openweathermap.org ou reativar a APIkey.


import requests
import datetime as dt
from PyQt5 import QtWidgets, QtGui

CITIES = []
CITY = ""

# Definir Classe da janela:

class JanelaApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clima das cidades")
        self.setGeometry(100,100,500,500)
        self.CITIES = ["Rio de Janeiro", "São Paulo", "Navegantes"]


# Criando um combo box:
    def init_ui(self):
        self.city_combo = QtWidgets.QComboBox(self)
        self.city_combo.addItems(self.CITIES)
        self.city_combo.move(50, 50)
        
        self.display_area = QtWidgets.QTextEdit(self)
        self.display_area.setReadOnly(True)
        self.display_area.move(50, 100)
        self.display_area.resize(400, 300)


        # Ligando o combo box a função display_clima:
        self.city_combo.activated.connect(self.display_clima)    


# Criando função Menu:

def menu():
    print("Menu de cidades para monitoramento do clima:")
    for c, city in enumerate(CITIES):
        print(f"{c+1}. {city}")
    choice = int(input("Digite o número da cidade que você deseja ver as informações: "))
    return CITIES[choice-1]


#Criando função para definir Kelvin como unidade padrão:

def Padrao_Kelvin(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) * 32
    return celsius, fahrenheit


# Obtendo e mostrando informações:
def display_clima(self):
    BASE_URL =  "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "d04ac5b90d03979302cf954cffa78825"
    CIDADES = ["Rio de janeiro", "São Paulo", "Navegantes"]
    
    
    cidadesele = self.city_combo.currentText()
    url = BASE_URL + "appid=" + API_KEY + "&q=" + cidadesele
    resposta = requests.get(url).json()
    temp_kelvin = resposta['main']['temp']
    temp_celsius, temp_fahrenheit = Padrao_Kelvin(temp_kelvin)
    sensacao_kelvin = resposta['main']['feels_like']
    sensacao_celsius, sensacao_fahrenheit = Padrao_Kelvin(sensacao_kelvin)
    umidade = resposta['main']['humidity']
    descricao = resposta['weather'][0]['description']
    vento_velo = resposta['wind']['speed']
    nascer_sol = dt.datetime.utcfromtimestamp(resposta['sys']['sunrise'] + resposta['timezone'])
    por_do_sol = dt.datetime.utcfromtimestamp(resposta['sys']['sunset'] + resposta['timezone'])

# Mostrando as informações ao Usuário:
    self.display_area.clear()
    self.display_area.append(f'Temperatura em {CITY}: {temp_celsius:.2f}C ou {temp_fahrenheit:.2f}F.')
    self.display_area.setText(f'Temperatura em {CITY}: {temp_celsius:.2f}C ou {temp_fahrenheit:.2f}F.\n'
                        f'Sensação térmica em {CITY} é de: {sensacao_celsius:.2f}C ou {sensacao_fahrenheit:.2f}F.\n'
                        f'Umidade relativa do ar em {CITY}: {umidade}%.\n'
                        f'Velocidade do vento em {CITY}: {vento_velo}km/h.\n'
                        f'Informações gerais em {CITY}: {descricao}.\n'
                        f'O sol nasce em {CITY}: {nascer_sol} hora local.\n'
                        f'O sol se põe em {CITY}: {por_do_sol} hora local.')


