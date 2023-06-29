# Написать парсер ASCII символов для прибора, работающего по serial интерфейсу.
# Запрос занчений: “GET_A” , “GET_B”, “GET_C”
# Ответ: “A_10V”,  “B_5V”, “C_15A”
# Предусмотреть смену с serial интерфейса на TCP.
#!/usr/bin/python3
'''
Для получения данных и отладки по serial используется макет с мк. Код макета добавил в проект.
Так же полагаю, что в реальном проекте отправка данных будет осущетсвляться с контролем целостности,
и потребуются дополнительные настройки serial port
'''
import serial, socket
DATA = {"A": "A_10V", "B": "B_5V", "C": "A_15V" } #
serial_port = None
cmd_stop = True #команда для управления циклом while для остановки цикла нужно отправить 'stop'
method = 'com' #выбор интерфеса приема данных  com | tcp.
def get_source():
    if method == 'com':
        global serial_port
        serial_port = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)
    if method == 'tcp':
        # checkount
        # with socket.socket() as sock:
        #     sock = socket.socket()
        #     sock.connect_ex(("localhost",3000))
        pass #тут по аналогии с com-порто будет проводиться инициализация tcp

get_source()
def read_serial_data(cmd): #чтение данных по serial
    if(cmd.lower()=='stop'):
        global cmd_stop
        cmd_stop = False
    if cmd.upper().startswith('GET_') == True:
        serial_port.write(cmd.upper().encode())
        rx = serial_port.readline()
        string_rx = str(rx, "UTF-8").strip()
        if len(string_rx)>0:
            print(parse_data(string_rx))
        # возможно не совсе корретная обработка ошибки.
        # Если бы была такая возможность данную обработку я бы перенес на сторону устройства

def read_tcp_data(cmd): #чтение данных по tcp
    #     if sock.connect_ex(("localhost",3000))== 0:
    #         sock.send(cmd.encode())
    #         data = sock.recv()
    #         parse_data(data)
    #     else:
            if mock(cmd) is not None:
                print(mock(cmd))
def parse_data(data): # Обработка данных. Например: на входе A_10V на выходе 10
     try:
        symb = data.split("_")
        number = symb[1][:-1]
        return number
     except IndexError: # возможно, это не совсем корретная обработка ошибки
          print("Input error")
def mock(command):#иммитация отправки сообщения с сервера. Отправляем команду типа GET_A ищем значение в словаре по ключу
    if (command.lower() == 'stop'):
        global cmd_stop
        cmd_stop = False
    if command.upper().startswith('GET_') == True:
        cmd = command.split("_")
        symb = DATA[cmd[1]].split("_")
        number = symb[1][:-1]
        return number

def get_data(cmd):
    if(method=="com"):
        read_serial_data(cmd)
    if(method == "tcp"):
        read_tcp_data(cmd)

if __name__ == '__main__':
    while cmd_stop:
        get_data(input('Send command: ').upper())

