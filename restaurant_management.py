from food_courses import FoodCourses
from cruise_management import CruiseManagement
class RestaurantManagement:

  def food_info_list():
    cruises = CruiseManagement.cruise_list()
    food_object_list = []
    for i in cruises:
      food_object_list.append(i.sells)
    return food_object_list
  
  def process_of_selection():
    check_name = []
    room_number = []
    with open('Administrator.txt') as f:
      for line in f:
        check_name.append(line.split(',')[0])
        room_numb = line.split(',')[1]
        room_number.append(room_numb)

#el password se puede conseguir en el documento administrator.txt y da acceso a los productos de los 4 barcos para agregar a un sistema global, nota: el nombre de usuario y la contraseña están en orden de arriba a abajo por cada index del crucero

    name=input('Ingrese el usuario de administrador: ').lower()
    name = name.title()
    room_number_id=input('Ingrese la contraseña: ')
    
    if name in check_name and room_number_id in room_number:
      index_name = check_name.index(name)
      cruise_index = []
      with open('Administrator.txt') as l:
        for lines in l:
          cruise_index.append(lines.split(',')[2])
      input_index= cruise_index[index_name]
      input_index=int(input_index)
      all_product_listed=[]
      all_combo_listed=[]
      while True:
        selector= int(input('''
    Desea agregar platos a su menu[1]
    Eliminar productos del menu[2]
    Modificar producto del menu[3]
    Agregar combos a un menu de combos[4]
    Eliminar combo del menu de combos[5]
    Buscar productos por nombre o rango de precio[6]
    Buscar combos por nombre o rango de precio[7]
    finalizar y guardar los cambios[8]
    '''))
        
        if selector==1:
          all_product_listed.append(RestaurantManagement.food_object_menu(input_index))
        elif selector ==2:
          delete_element_index=RestaurantManagement.delete_product(all_product_listed)
          if all_product_listed!=[]:
            if delete_element_index != None:
              all_product_listed.pop(delete_element_index)
        elif selector == 3:
          delete_element_index= RestaurantManagement.delete_product(all_product_listed)
          if delete_element_index != None:
            new_food_course=RestaurantManagement.modify_product(all_product_listed,delete_element_index)
            all_product_listed.insert(delete_element_index, new_food_course)
            all_product_listed.pop(delete_element_index+1)
        elif selector == 4:
          all_combo_listed.append(RestaurantManagement.combo_object_menu(input_index))
        elif selector == 5:
          delete_element_index=RestaurantManagement.delete_combo(all_combo_listed)
          if all_combo_listed!=[]:
            if delete_element_index != None:
              all_combo_listed.pop(delete_element_index)
        elif selector == 6:
          RestaurantManagement.search_food_in_list(all_product_listed)
        elif selector == 7:
          RestaurantManagement.search_combo_in_list(all_combo_listed)
        elif selector == 8:
          for m in range(0,len(all_product_listed)):
            with open("ProductListed.txt","w") as db:
                db.write(f'{all_product_listed[m].name},{all_product_listed[m].price},{all_product_listed[m].quantity},{all_product_listed[m]},{all_product_listed[m].clasification}')
          
          for z in all_combo_listed:
            with open("ComboListed.txt","w") as xs:
                xs.write(f'{z[0]}||{z[1]}||{z[2]}')
          break  
    else:
      print('usuario o password incorrecto')

  def food_object_menu(input_index):
    cruise_food_list=RestaurantManagement.food_info_list()[input_index]
    
    food_combo = ['Cofuta & Refresco','Hamburguesa & Refresco']
    drink_list = ['Coca Cola','Ron','Cerveza']
    

    print('Estos son los alimentos disponibles seleccione alguno para agregarlo al menu:')
    for x in cruise_food_list:
      if x["name"] not in food_combo:
        print(f'{x["name"]} [{cruise_food_list.index(x)}]')
      else:
        cruise_food_list.remove(x)
    idx_food= int(input(''))
    product_name= cruise_food_list[idx_food]['name']
    price= cruise_food_list[idx_food]['price']
    taxes=price*(16/100)
    price_with_taxes=price+taxes
    price_with_taxes=f"{price_with_taxes:.2f}"
    print(f'este es el precio: {price_with_taxes}')
    quantity= cruise_food_list[idx_food]['amount']
    if cruise_food_list[idx_food]['name'] in drink_list:
      input_clasification = int(input('\n\nTamaño pequeño[0], mediano[1] o grande[2]'))
      if input_clasification == 0:
        clasification = 'pequeño'
        return FoodCourses(product_name,price_with_taxes,clasification,quantity)
      elif input_clasification == 1:
        clasification = 'mediano'
        return FoodCourses(product_name,price_with_taxes,clasification,quantity)
      else:
        clasification = 'grande'
        return FoodCourses(product_name,price_with_taxes,clasification,quantity)
    else:
      input_clasification = int(input('\n\npara llevar[0] o de preparación[1]'))
      if input_clasification == 0:
        clasification = 'empaque'
        return FoodCourses(product_name,price_with_taxes,clasification,quantity)
      else:
        clasification = 'preparación'
        return FoodCourses(product_name,price_with_taxes,clasification,quantity)
  
  def delete_product(all_product_listed):
    index_available =[]
    if all_product_listed!=[]:
      for product in all_product_listed:
        index_available.append(all_product_listed.index(product))
        print(f'{product.name} [{all_product_listed.index(product)}]:\n Precio:{product.price} Tamaño:{product.clasification} Cantidad:{product.quantity}')
      delete_index =int(input('\n\nIngrese el numero del producto'))
      if delete_index in index_available:
        return delete_index
      else:
        print('introduzca el numero correcto')
    
  def modify_product(all_product_listed,index_to_modify):
    if index_to_modify != None:
      modify_index=int(input('''Modificar nombre [0]
Modificar precio [1]
Modificar informacion [2]
Modificar cantidad [3]
'''))
      if modify_index == 0:
        food_object=all_product_listed[index_to_modify]
        new_name=input('introduzca el nuevo nombre: ').lower
        new_name = new_name.title()
        return FoodCourses(new_name,food_object.price,food_object.clasification,food_object.quantity)

      elif modify_index == 1:
        food_object=all_product_listed[index_to_modify]
        new_name=input('introduzca el nuevo precio: ')
        return FoodCourses(food_object.name,new_name,food_object.clasification,food_object.quantity)

      elif modify_index ==2:
        food_object=all_product_listed[index_to_modify]
        new_name=input('introduzca la nueva clasificacion: ')
        return FoodCourses(food_object.name,food_object.price,new_name,food_object.quantity)

      elif modify_index ==3:
        food_object=all_product_listed[index_to_modify]
        new_name=input('introduzca la nueva cantidad: ')
        return FoodCourses(food_object.name,food_object.price,food_object.clasification,new_name)
      else:
        food_object=all_product_listed[index_to_modify]
        return FoodCourses(food_object.name,food_object.price,food_object.clasification,food_object.quantity)
#Aqui empiezan los combos
  def combo_object_menu(input_index):
    cruise_food_list=RestaurantManagement.food_info_list()[input_index]
    price_list = []

    
    combo =[]
    
    combo_name = input("Nombre del combo: ")
    i=0
    
    while True:
      print('\n\nEstos son los alimentos disponibles seleccione alguno para agregarlo al combo:')
      for x in cruise_food_list:
        print(f'{x["name"]} [{cruise_food_list.index(x)}]')
      idx_food= int(input(''))
      product_name= cruise_food_list[idx_food]['name']
      price= cruise_food_list[idx_food]['price']
      price = int(price)
      
      quantity= cruise_food_list[idx_food]['amount']
      clasification = "combo_element"
      combo.append(product_name)
      price_list.append(price)
      i+=1
      if i>=2:
        exit = input("para salir pulse ['e'], de otra forma continue agregando elementos al combo: ").lower()
        if exit == 'e':
          break
    
    total_price=sum(price_list)
    taxes=total_price*(16/100)
    price_with_taxes=total_price+taxes
    price_with_taxes=f"{price_with_taxes:.2f}"
    data_combo=[combo_name,price_with_taxes,combo]
    return data_combo
      
  def delete_combo(all_product_listed):
    index_available =[]
    if all_product_listed!=[]:
      food_content = []
      for product in all_product_listed:
        for x in product[2]:
          food_content.append(x.name)
      for product in all_product_listed:
        index_available.append(all_product_listed.index(product))
        print(f'{product[0]} [{all_product_listed.index(product)}]:\n Precio:{product[1]}\n contenido:{food_content}')
      delete_index =int(input('\n\nIngrese el numero del producto'))
      if delete_index in index_available:
        return delete_index
      else:
        print('introduzca el numero correcto')

  def binarySearch (array, start, end, x):
    if end >= start:
      mid = start + (end- start)//2
      if array[mid] == x:
        return mid
      elif array[mid] > x:
        return RestaurantManagement.binarySearch(array, start, mid-1, x)
      else:
        return RestaurantManagement.binarySearch(array, mid+1, end, x)
    else:
      return -1

  def search_food_in_list(all_product_listed):
    name_array=[]
    price_array=[]
    clasification_array=[]
    quantity_array=[]
    validation=int(input('Desea hacer la busqueda por nombre [0] o por precio [1]: '))
    if validation == 0:
      x = input('Ingrese el nombre del producto').lower()
      x = x.title()
      for i in range(0,len(all_product_listed)):
        name_array.append(all_product_listed[i].name)
        price_array.append(all_product_listed[i].price)
        clasification_array.append(all_product_listed[i].clasification)
        quantity_array.append(all_product_listed[i].quantity)
      target=RestaurantManagement.binarySearch (name_array, 0, len(name_array)-1, x)
      if target != -1:
        print(f'''
        Nombre: {name_array[target]}
  Precio: {price_array[target]}
  Clasificacion: {clasification_array[target]}
  Cantidad: {quantity_array[target]}''')
      else:
        print('No existe ningun alimento con ese nombre registrado en la base de datos')
    elif validation == 1:
      x = input('Ingrese el precio')
      for i in range(0,len(all_product_listed)):
        name_array.append(all_product_listed[i].name)
        price_array.append(all_product_listed[i].price)
        clasification_array.append(all_product_listed[i].clasification)
        quantity_array.append(all_product_listed[i].quantity)
      target=RestaurantManagement.binarySearch (price_array, 0, len(name_array)-1, x)
      if target != -1:
        print(f'''
        Nombre: {name_array[target]}
  Precio: {price_array[target]}
  Clasificacion: {clasification_array[target]}
  Cantidad: {quantity_array[target]}''')
      else:
        print('No existe ningun alimento con ese nombre registrado en la base de datos')
  
  def search_combo_in_list(all_combo_listed):
      name_array=[]
      price_array=[]
      
      validation=int(input('Desea hacer la busqueda por nombre [0] o por precio [1]?'))
      if validation == 0:
        x = input('Ingrese el nombre del combo')
        for i in all_combo_listed:
          name_array.append(i[0])
          price_array.append(i[1])
          
          target=RestaurantManagement.binarySearch (name_array, 0, len(name_array)-1, x)
        if target != -1:
          print(f'''
          Nombre: {name_array[target]}
    Precio: {price_array[target]}''')
        else:
          print('No existe ningun alimento con ese nombre registrado en la base de datos')
      elif validation == 1:
        x = input('Ingrese el precio del combo')
        for i in all_combo_listed:
          name_array.append(i[0])
          price_array.append(i[1])
          
          target=RestaurantManagement.binarySearch (name_array, 0, len(name_array)-1, x)
        if target != -1:
          print(f'''
          Nombre: {name_array[target]}
    Precio: {price_array[target]}''')
        else:
          print('No existe ningun combo con ese nombre registrado en la base de datos')

        target=RestaurantManagement.binarySearch (price_array, 0, len(name_array)-1, x)
        if target != -1:
          print(f'''
          Nombre: {name_array[target]}
    Precio: {price_array[target]}''')
        else:
          print('No existe ningun combo con ese nombre registrado en la base de datos')
  
  def food_supplier():
    product_name = []
    product_price= []
    product_quantity= []
    product_clasification= []

    with open('ProductListed.txt') as pro:
      for line in pro:
        product_name.append(line.split(',')[0])
        product_price.append(float(line.split(',')[1]))
        product_quantity.append(int(line.split(',')[2]))
        product_clasification.append(line.split(',')[4])
    
    combo_name = []
    combo_price= []
    combo_product= []

    with open('ComboListed.txt') as pro:
      for line in pro:
        combo_name.append(line.split('||')[0])
        combo_price.append(float(line.split('||')[1]))
        combo_product.append(line.split('||')[2])

    
    while True:

      sel = int(input('\nseleccionar producto[1] o combo[2]: '))
      if sel == 1:
        print('Selecciona el producto deseado:')
        for i in product_name:
          print(f"{i} [{product_name.index(i)+1}]")
        index_product=int(input(''))
        print(f'''Precio: {product_price}
Clasificacion: {product_clasification}''')
        save=int(input('\n\nAcepta el pedido si[1] no[2]: '))
        if save==1:
          with open("RestaurantBill.txt","a") as xsuj:
            xsuj.write(f'{product_name[index_product -1]},{product_price[index_product -1]}\n')
      elif sel == 2:
        print('Selecciona el combo deseado:')
        for j in combo_name:
          print(f"{j} [{combo_name.index(j)+1}]")
        index_product=int(input(''))
        print(f'''Precio: {combo_price[index_product -1]}
Contiene: {combo_product[index_product -1]}''')
        saves=int(input('\n\nAcepta el pedido si[1] no[2]: '))
        if saves==1:
          with open("RestaurantBill.txt","a") as fguj:
            fguj.write(f'{combo_name[index_product -1]},{combo_price[index_product -1]}\n')
      exit=input('\n\npulse ("e") para salir del modulo, o cualquier tecla para continuar comprando: ').lower()
      if exit == 'e':
        break
  
      
        