from cruise import Cruise
from internet_info import InternetInfo

class CruiseManagement:

  def show_all_cruises():
    cruises = CruiseManagement.cruise_list() 
    for i in cruises:
      print(f"{i.name} [{cruises.index(i)+1}]")
    return cruises

  def print_info(cruises,input_index):
    print(f'''Crucero: "{cruises[input_index].name}"
    Rutas:{cruises[input_index].route}
    Fecha de partida: {cruises[input_index].departure}

    El precio del boleto simple es: {cruises[input_index].cost["simple"]}
    Cantidad de pasillos: {cruises[input_index].rooms["simple"][0]} 
    Cantidad de habitaciones por pasillo: {cruises[input_index].rooms["simple"][1]}
    Capacidad de las habitaciones: máximo {cruises[input_index].capacity["simple"]} personas

    El precio del boleto premium es: {cruises[input_index].cost["premium"]}
    Cantidad de pasillos: {cruises[input_index].rooms["premium"][0]}
    Cantidad de habitaciones por pasillo: {cruises[input_index].rooms["premium"][1]}
    Capacidad de las habitaciones: máximo {cruises[input_index].capacity["premium"]} personas

    El precio del boleto vip es: {cruises[input_index].cost["vip"]} 
    Cantidad de pasillos: {cruises[input_index].rooms["vip"][0]} 
    Cantidad de habitaciones por pasillo: {cruises[input_index].rooms["vip"][1]}
    Capacidad de las habitaciones: máximo {cruises[input_index].capacity["vip"]} personas''')

  def cruise_list():
    cruise_data = InternetInfo.api_saman_caribbean()
    cruise_object_list=[]
    for x in cruise_data:
      cruise_object_list.append(Cruise(x["name"],x["route"],x["departure"],x["cost"],x["rooms"],x["capacity"],x["sells"]))
    return cruise_object_list

  def cruises_available():
#los tipos de boletos disponibles son: {list(i.cost.keys())}
    cruises = CruiseManagement.show_all_cruises()
    module_running = True
    while module_running == True:
      try:
        input_index = int(input("\n\nDe que barco desea obtener información?\n\n"))
        if input_index >= 1:
          CruiseManagement.print_info(cruises,input_index-1)
        else:
          print("opción no válida")
      except:
        print("opción no válida")
    
      exit_module= input("\n\npulse 'e' para salir del modulo o cualquier tecla para continuar viendo los barcos: ").lower()
      if exit_module == "e":
        module_running=False