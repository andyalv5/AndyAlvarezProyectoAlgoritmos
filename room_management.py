from cruise_management import CruiseManagement
from room import Room
class RoomManagement:

#Este es el diccionario que contiene todas las habitaciones de cada crucero ordenado por "simple", "premium" y "vip"
  def room_object_dictionary():
    cruises = CruiseManagement.cruise_list()
    room_object_dictionary = []
    for i in cruises:
      simple_room_array = RoomManagement.define_room(i,"simple","buen precio y con comodidades adecuadas como tv y radio","si puede solicitar servicio a la habitación")
      premium_room_array= RoomManagement.define_room(i,"premium","habitación con las mejores vistas del crucero, perfecta para una luna de miel,descanso del trabajo o posible jubilación","si posee vista al mar")
      vip_room_array= RoomManagement.define_room(i,"vip","si te gusta la fiesta esta es tu habitación, bastante espaciosa y con jacuzzi","si puede albergar fiestas privadas")
      room_object_dictionary.append({"simple":simple_room_array,"premium": premium_room_array,"vip": vip_room_array})
    return room_object_dictionary

#Esta función fue creada para evitar que el código en la función room_object_dictionary se repita
  def define_room(cruise,description="",reference="",add_info=""):
    room_info = []
    simple_room = cruise.rooms[description][0]*cruise.rooms[description][1]
    for i in range (1 ,simple_room+1):
      room_info.append(Room(chr(64+i),i,cruise.capacity[description], reference,add_info))
    return room_info

#función creada para correr el proceso de compra
  def room_check_in():
    val = int(input('\n\nPara comprar un boleto con base al barco teclee (1), o si lo prefiere puede elegir el boleto por destino (2): '))
    if val == 1:
      print("\n\nLos cruceros disponibles son:")
      CruiseManagement.show_all_cruises()
      input_index = int(input("\n\nPulse la tecla del barco al que usted desea comprar un boleto: "))
      #En caso de aumentar el numero de barcos el programador debera cambiar el numero de opciones válidas como entradas del sistema
      if input_index >= 0 and input_index<=4:
        RoomManagement.run_check_in(input_index)  
      else:
        return
    elif val == 2:
      destination=input('Ingrese el destino: ').lower()
      destination= destination.title()
      cruise_list=CruiseManagement.cruise_list()
      is_a_valid_option=[]
      for i in cruise_list:
        if destination in i.route:
          print(f"\n\nLos cruceros disponibles con estas rutas son:{i.name} [{cruise_list.index(i)+1}]")
          is_a_valid_option.append(cruise_list.index(i)+1)
      if is_a_valid_option != []:
        input_index = int(input("\n\nPulse la tecla del barco al que usted desea comprar un boleto: "))
        if input_index in is_a_valid_option:
          RoomManagement.run_check_in(input_index)  

#función creada para reducir líneas de código.
  def run_check_in(input_index):
    if input_index >= 1:
      
      room_type_id = int(input("\n\nDesea una habitación 'simple'(1),'premium'(2) o 'vip'(3): "))
      if room_type_id >= 0 and room_type_id <=4:
        client_tickets = int(input("\n\nCuantas personas viajan con usted, incluyendose?: "))
        if client_tickets > 10:
          print("\n\nSon demasiadas personas")
          return
        if client_tickets > 0:
          if room_type_id == 3:
            RoomManagement.registration_by_room_type(client_tickets,input_index,3)
          elif room_type_id == 2:
            RoomManagement.registration_by_room_type(client_tickets,input_index,2)
          elif room_type_id == 1:
            RoomManagement.registration_by_room_type(client_tickets,input_index,1)
          else:
            return
      
      
  def registration_by_room_type(client_tickets,input_index,num):
    if num == 1:
      important_tag = "simple"
      room_capacity = RoomManagement.return_room_capacity(input_index,"simple")
      RoomManagement.print_available_room(input_index,"simple")
    if num== 2:
      important_tag = "premium"
      room_capacity = RoomManagement.return_room_capacity(input_index,"premium")
      RoomManagement.print_available_room(input_index,"premium")
    if num==3:
      important_tag = "vip"
      room_capacity=RoomManagement.return_room_capacity(input_index,"vip")
      RoomManagement.print_available_room(input_index,"vip")
    do_not_register = input('\n\nA continuación se procederá a realizar la operación de compra si desea salir introduzca la tecla "s": ')
    if do_not_register.lower() == "s":
      return False
    else:
      if client_tickets == room_capacity:
        room_list_check_in = RoomManagement.client_register(input_index,num,important_tag)
        RoomManagement.client_bill(room_list_check_in,input_index)
        
      else:
        for x in range(0,client_tickets):
          room_list_check_in = RoomManagement.client_register(input_index,num,important_tag)
          RoomManagement.client_bill(room_list_check_in,input_index)
            
  def client_bill(room_list_check_in,input_index):
    cruise_cost = CruiseManagement.cruise_list()[room_list_check_in[6]].cost
    cost_by_room= cruise_cost[room_list_check_in[7]]
    discount = cost_by_room *(room_list_check_in[3]/100)
    payment= cost_by_room-discount
    taxes= payment*(16/100)
    total_payment = payment+taxes
    with open("Bills.txt", "a+") as a:
      a.write(f"{room_list_check_in[0]},{room_list_check_in[1]},{room_list_check_in[2]},{input_index},{room_list_check_in[4]},{room_list_check_in[5]},{room_list_check_in[7]},{cost_by_room:.3f},{discount:.3f},{payment:.3f},{taxes:.3f},{total_payment:.3f}\n")  

    print(f'''
Señor {room_list_check_in[0]}
ID: {room_list_check_in[1]}
Edad: {room_list_check_in[2]}
Numero de Habitación: {room_list_check_in[4],
room_list_check_in[5]}
Tipo de Habitación: {room_list_check_in[7]}
Costo sin descuentos: {cost_by_room:.3f}
Descuento: {discount:.3f}
Pago con deducibles: {payment:.3f}
impuestos del 16%: {taxes:.3f}
                            
                            
                            
                            Pago total
                            {total_payment:.3f}
''')
      
  def print_available_room(input_index,type_room=""):
    room_available=RoomManagement.room_info(input_index-1,type_room)
    empty_list = []
    for x in room_available:
      if x != '':
        empty_list.append((x.number,x.letter))
      else:
        empty_list.append('')
    
    matrix=[empty_list[i:i+4] for i in range(0,len(empty_list),4)]
    print(f"\n\nlas habitaciones disponibles son:")
    for l in matrix:
      print(l)

  def _cifratedClientBill(input_index):
    RoomManagement.run_check_in(input_index)


  def return_room_capacity(input_index,num):
    if num == 1:
      important_tag = "simple"
      room_capacity =CruiseManagement.cruise_list()[input].capacity["simple"]
      return room_capacity
    if num== 2:
      important_tag = "premium"
      room_capacity = CruiseManagement.cruise_list()[input].capacity["premium"]
      return room_capacity
    if num==3:
      important_tag = "vip"
      CruiseManagement.cruise_list()[input].capacity["vip"]
      return room_capacity


#función que muestra solo las habitaciones disponibles con su index

#función que retorna la lista de habitaciones por tipo de habitación, es decir si es 'simple','standard' o 'Vip'
  def room_info(input_index,type_room=""):
    room_dictionary_list = RoomManagement.room_object_dictionary()
    #aqui se debe eliminar
    #room_dictionary_list[0]['simple'].pop(0)
    idx_room = []
    ty_room = []
    room_selec = []
    with open('Database.txt') as f:
      for line in f:
        idx_r = int(line.split(',')[1])
        idx_room.append(idx_r)
        room_se = int(line.split(',')[5])
        room_selec.append(room_se)
        idx_r = line.split(',')[6].replace('\n','')
        ty_room.append(idx_r)
    if idx_room != '':
      for i in range (0, len(idx_room)):
        room_dictionary_list[idx_room[i]-1][ty_room[i]].pop(room_selec[i]-1)

        room_dictionary_list[idx_room[i]-1][ty_room[i]].insert(room_selec[i]-1,'')

    return(room_dictionary_list[input_index][type_room])

  

#formulario para registrar al cliente
  def client_register(input_index,ticket_type_index,important_tag):
    client_name = input('\n\nIntroduzca su nombre: ').lower()
    client_name = client_name.title() 
    id_number = int(input('Introduzca el número de su documento de identidad: '))
    is_prime_boolean = RoomManagement.check_prime(id_number)
    discount = 0
    if is_prime_boolean == 99:
      discount+=10
    is_abundant_boolean = RoomManagement.is_abundant(id_number)
    if is_abundant_boolean == 34:
      discount+=15
    while True:
      disability_condition = input('Posee alguna discapacidad sí(1), no(2): ')
      if disability_condition == '1':
        discount += 30
        break
      elif disability_condition == "2":
        break
    age_client = int(input('Introduzca su edad: '))
    if age_client > 65 and ticket_type_index == 1:
      ticket_upgrade = int(input('Desea mejorar su paquete gratuitamente a premium sí(1), no(2): '))
      if ticket_upgrade == 1:
        room_lenght = len(RoomManagement.room_info(input_index-1,"premium"))
        RoomManagement.print_available_room(input_index,"premium")
        room_selected = int(input('Ingrese el número de la habitación que desea: '))
        if room_selected <= 0:
          return
        true_room = RoomManagement.room_object_dictionary()[input_index]["premium"][room_selected-1]
        all_client_data_list = [client_name,id_number,age_client,discount,true_room.number,true_room.letter, input_index ,"premium"]
        room_selected=room_selected-1
        for x in range(0,room_lenght):
          if room_selected == x:
            RoomManagement.save_client(client_name,input_index,id_number,age_client,discount,room_selected+1,"premium")  
        return all_client_data_list
     
    RoomManagement.print_available_room(input_index,important_tag)
    room_lenght = len(RoomManagement.room_info(input_index-1,important_tag))
    room_selected = int(input('Ingrese el número de la habitación que desea: '))
    if room_selected <=0:
      return
     #aquieiieiieieiuwiquiefhbhfw!!!!!!
    true_room = RoomManagement.room_object_dictionary()[input_index][important_tag][room_selected-1]
    all_client_data_list = [client_name,id_number,age_client,discount,true_room.number,true_room.letter, input_index ,important_tag]
    room_selected=room_selected-1
    for x in range(0,room_lenght):
      if room_selected == x:
        RoomManagement.save_client(client_name,input_index,id_number,age_client,discount,room_selected+1,important_tag)

    return all_client_data_list
      


  def save_client(client_name,cruise_index,id_number,age_client,discount,room_selected,type_room):
    with open("Database.txt", "a") as a:
      a.write(f"{client_name},{cruise_index},{id_number},{age_client},{discount},{room_selected},{type_room}\n")      

  #def check_prime(n,m=2):
  #  is_prime = True
  #  if m*100000 < n-1:
  #    if n % m == 0:
  #      is_prime= False
  #    else:
  #      RoomManagement.check_prime(n,m+1)
  #  elif n == 1 or n == 0:
  #    is_prime= False
  #  return is_prime
  def check_prime(id_number):
    counter=0
    for i in range(1,id_number+1):
      if id_number % i == 0:
        counter+=1
    if counter == 2:
      return 99
    else:
      return 3

  def is_abundant(n):
    factor_sum = sum([factor for factor in range(1, n) if n % factor == 0])
    if factor_sum > n:
      return 34



  def check_out():
    room_dictionary_list = RoomManagement.room_object_dictionary()
    idx_room = []
    ty_room = []
    room_selec = []
    name = []
    cruise_ind = []

    input_name=input('cual es su nombre? ')
    input_room=int(input('cual es el numero de su habitacion? '))
    with open('Database.txt') as f:
      for line in f:
        idx_r = int(line.split(',')[1])
        idx_room.append(idx_r)
        room_se = int(line.split(',')[5])
        room_selec.append(room_se)
        cruise_index = int(line.split(',')[1])
        cruise_ind.append(cruise_index)
        idx_r = line.split(',')[6].replace('\n','')
        ty_room.append(idx_r)
        name.append(line.split(',')[0])
    
    for x in name:
      if x == input_name:
        index = name.index(input_name)
        cruise_index= cruise_ind[index]
        print(cruise_index)
        cruise_capacity = CruiseManagement.cruise_list()[cruise_index].capacity

        simple_room = Room(chr(64+input_room),input_room, cruise_capacity[ty_room[index]],"utilizada recientemente","mismas condiciones que las habitaciones de la clase")
        


        room_dictionary_list[idx_room[index]][ty_room[index]].insert(index,simple_room)
        print('\n\nSe ha procesado su solicitud, la habitacion esta disponible de nuevo para su uso')
        with open("Database.txt") as db:
          datos = db.readlines()
          eliminar = datos[index]
        with open("Database.txt","w") as db:
          for dato in datos:
            if dato != eliminar:
              db.write(dato)
        with open("CheckOutList.txt", "a+") as a:
          a.write(f"{input_name} de la habitacion {input_room} ha procedido al checkout\n")
