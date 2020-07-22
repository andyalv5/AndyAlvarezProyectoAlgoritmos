import matplotlib.pyplot as plt
class Statistics:
  def check_average():
    check_name = []
    room_number = []
    with open('Administrator.txt') as f:
      for line in f:
        check_name.append(line.split(',')[0])
        room_numb = line.split(',')[1]
        room_number.append(room_numb)

#el user y el password se puede conseguir en el documento administrator.txt se puede usar cualquiera de esas contraseñas

    name=input('Ingrese el usuario de administrador: ').lower()
    name = name.title()
    room_number_id=input('Ingrese la contraseña: ')
    if not name in check_name and room_number_id in room_number:
      return
    else:
      name_list = []
      id_number = []
      tour_id = []
      tour_price = []
      cruise_client_price = []
      cruise_number = []
    
      with open('Bills.txt') as bill:
        for line in bill:
          name_list.append(line.split(',')[0])
          id_number.append(int(line.split(',')[1]))
          delete_symbol = line.split(',')[11].replace("\n",'')
          cruise_client_price.append(float(delete_symbol))
          cruise_number.append(int(line.split(',')[3]))

      with open('TourInfo.txt') as tour_ide:
        for line in tour_ide:
          tour_id.append(int(line.split(',')[0]))
          tour_price.append(float(line.split(',')[1]))
      
      restaurant_name_list = []
      with open('RestaurantBill.txt') as idtt:
        for line in idtt:
          restaurant_name_list.append(line.split(',')[0])
      if len(restaurant_name_list) != 0: 
        print(f'\n\nEste es el alimento o combo mas comprado por los clientes: {max(restaurant_name_list,key=restaurant_name_list.count)}')
      
      unique_elements=set(restaurant_name_list)
      y_counter_food=[]
      x_counter_food=[]
      for thda in unique_elements:
        y_counter_food.append(restaurant_name_list.count(thda))
      for kld in range(0,len(unique_elements)):
        x_counter_food.append(kld+1)

      is_the_end= int(input('Desea ver la grafica?, hacerlo detendra su programa [1]' ))
      if is_the_end == 1:
        plt.bar(x_counter_food,y_counter_food,label='products',color='orange')
        plt.title('Product and Combo Counter')
        plt.ylabel('productos')
        plt.xlabel('numero de personas')
        plt.legend()
        plt.show()






      cruise_client_price_copy=cruise_client_price
      
      tour_price_copy=tour_price 
      Statistics.average_per_person(cruise_client_price,tour_price)
   
      Statistics.not_buying_tour(id_number,tour_id)
      
      Statistics.best_three_clients(tour_price,cruise_client_price,id_number,tour_id,name_list,cruise_number)
      exit=input("Pulse cualquier tecla para cerrar el modulo")
    
        

  def average_per_person(cruise_client_price,tour_price):
    print(cruise_client_price)
    total_client_price =sum(cruise_client_price)
    total_tour_price =sum(tour_price)
    client_number =len(cruise_client_price)
    price_added = total_client_price + total_tour_price
    average = price_added/client_number
    average = average
    print(f"\n\nEl gasto promedio de una persona es: {average:.2f}")

    
    x_el1 = []
    y_el1 = cruise_client_price
    y_average=[]
    
    for de in range(0,len(y_el1)):
      x_el1.append(de)
      y_average.append(average)

    is_the_end_my_friend= int(input('Desea ver el grafico del promedio? Advertencia, detendra la ejecucion del programa, pulse [1] para ver la grafica'))
    if is_the_end_my_friend == 1:
      plt.plot(x_el1,y_el1,label='Cruise Line Price', color='blue')
      plt.plot(x_el1,y_average,label='Average Including Tours', color='red')
      plt.title('Average vs Cruise Ticket Income')
      plt.ylabel('Profit')
      plt.xlabel('Client Number')

      plt.legend()
      plt.grid()
      plt.show()
    
    return(average)

  def not_buying_tour(id_number,tour_id):
    client_number = len(id_number)
    tour_id_once=set(tour_id)
    tour_client_number = len(tour_id)
    not_buying_tour =client_number-tour_client_number
    average = (not_buying_tour*100)/client_number
    print(f"\n\nPorcentaje de personas que no compran el tour: {average:.2f}%")
    return average

  def best_three_clients(tour_price,cruise_client_price,id_number,tour_id,name_list):
    
    max_price = []
    for i in id_number:
      if i in tour_id:
        max_price.append(id_number.index(i))
     
    client_to_consider = []
    for w in max_price:
      client_to_consider.append(cruise_client_price[w])
      

    total_client_to_consider=[]
    for j in range(0,len(client_to_consider)):
      total_client_to_consider.append(client_to_consider[j]+tour_price[j])
    
   
    definitive_list = cruise_client_price
    for element in range(0,len(cruise_client_price)):
      if element in max_price:
        for ultimate_data in total_client_to_consider:
          
          definitive_list.insert(element,ultimate_data)
          definitive_list.pop(element+1)
          

    idx=definitive_list.index(max(definitive_list))
    print(f"\n\nEl cliente estrella es: {name_list[idx]} con {max(definitive_list)} dolares")
    definitive_list.remove(max(definitive_list))
    name_list.remove(name_list[idx])
    new_list = definitive_list
    if len(new_list) != 0:
      idx=new_list.index(max(new_list))
      print(f"\n\nEl cliente que le sigue en excelencia es: {name_list[idx]} con {max(new_list)} dolares")
      new_list.remove(max(new_list))
      name_list.remove(name_list[idx])
      if len(new_list) != 0:
        idx=new_list.index(max(new_list))
        print(f"\n\nEl tercer cliente con mayor fidelidad es: {name_list[idx]} con {max(new_list)} dolares\n\n")
      else:
        print("\n\nNo existe otro cliente\n\n")
    else:
      print("\n\nNo existe otro cliente")
     
  def best_three_clients(tour_price,cruise_client_price,id_number,tour_id,name_list,cruise_number):
    
    max_price = []
    for i in id_number:
      if i in tour_id:
        max_price.append(id_number.index(i))
     
    client_to_consider = []
    for w in max_price:
      client_to_consider.append(cruise_client_price[w])
      

    total_client_to_consider=[]
    for j in range(0,len(client_to_consider)):
      total_client_to_consider.append(client_to_consider[j]+tour_price[j])
    
   
    definitive_list = cruise_client_price
    for element in range(0,len(cruise_client_price)):
      if element in max_price:
        for ultimate_data in total_client_to_consider:
          
          definitive_list.insert(element,ultimate_data)
          definitive_list.pop(element+1)
    

    first_cruise_list=[]
    second_cruise_list=[]
    third_cruise_list=[]
    fourth_cruise_list=[]
    
    
    

    i=0
    for ou in cruise_number:
      if ou == 0:
        first_cruise_list.append(cruise_client_price[i])
        i+=1
      elif ou == 1:
        second_cruise_list.append(cruise_client_price[i])
        i+=1
      elif ou == 2:
        third_cruise_list.append(cruise_client_price[i])
        i+=1
      else:
        fourth_cruise_list.append(cruise_client_price[i])
        i+=1


    first_cruise_list=sum(first_cruise_list)
    second_cruise_list=sum(second_cruise_list)
    third_cruise_list=sum(third_cruise_list)
    fourth_cruise_list=sum(fourth_cruise_list)

    all_cruise_listed = [first_cruise_list,second_cruise_list,third_cruise_list,fourth_cruise_list]
    idx_cruise=all_cruise_listed.index(max(all_cruise_listed))
    if len(all_cruise_listed) !=0:
      print(f'El crucero numero {idx_cruise} ha recolectado más dinero, la cantidad: {max(all_cruise_listed):.2f}')
      all_cruise_listed.insert(idx_cruise,0)
      all_cruise_listed.pop(idx_cruise+1)
      idx_cruise=all_cruise_listed.index(max(all_cruise_listed))
      if len(all_cruise_listed) != 0:
        print(f'Luego, el crucero numero {idx_cruise} ha recolectado la cantidad: {max(all_cruise_listed):.2f}')
        all_cruise_listed.insert(idx_cruise,0)
        all_cruise_listed.pop(idx_cruise+1)
        idx_cruise=all_cruise_listed.index(max(all_cruise_listed))
        if len(all_cruise_listed) != 0:
          print(f'El crucero {idx_cruise} ha recolectado la cantidad: {max(all_cruise_listed):.2f}')
     
    idx=definitive_list.index(max(definitive_list))
    print(f"\n\nEl cliente estrella es: {name_list[idx]} con {max(definitive_list)} dolares")
    definitive_list.remove(max(definitive_list))
    name_list.remove(name_list[idx])
    new_list = definitive_list
    if len(new_list) != 0:
      idx=new_list.index(max(new_list))
      print(f"El cliente que le sigue en excelencia es: {name_list[idx]} con {max(new_list)} dolares")
      new_list.remove(max(new_list))
      name_list.remove(name_list[idx])
      if len(new_list) != 0:
        idx=new_list.index(max(new_list))
        print(f"El tercer cliente con mayor fidelidad es: {name_list[idx]} con {max(new_list)} dolares\n\n")
      else:
        print("No existe otro cliente\n\n")
    else:
      print("No existe otro cliente")
  