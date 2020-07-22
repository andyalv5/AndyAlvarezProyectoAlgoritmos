class TourSells:

  def tour_check_in(n,m,p,course_selected):
    id_number=input('Ingrese su numero de identidad: ')
    check_id_number = []
    with open('Database.txt') as identity:
      for line in identity:
        check_id_number.append(line.split(',')[2])
    if not id_number in check_id_number:
      print('Su ID no esta en nuestra base de datos')
      return 0
    try:
      people_number=int(input('Ingrese el numero de personas'))
    except:
      print('Ingrese un tipo de dato valido')
  
    if course_selected== 1:
      
      if people_number >= 1 and people_number <= 4:
        course_sel_for_message= "'Tour en el puerto'"
        new_number=sum(n)
        validation = new_number+people_number
        if validation > 10:
          print("\n\nNo hay más cupo para este tour")
          return 0
        else:
          x=0
          hour='7AM'
          for i in range(1,people_number+1):
            if i >= 3:
              discount = 30*(10/100)
              x+= 30-discount
            else:
              x+= 30
          TourSells.print_tour_message(x,hour,course_sel_for_message,people_number)
          TourSells.save_reservation(id_number,x,hour,course_sel_for_message,people_number)
        return people_number
      else:
        return 0  
       
    elif course_selected== 2:
      course_sel_for_message= "'Degustacion de comida local'"
      new_number=sum(m)
      validation = new_number+people_number
      
      if people_number >= 1 and people_number <= 2:
        if validation > 100:
          print("No hay más cupo para este tour")
          return 0
        else:
          x = people_number*100
          hour='12PM'
          TourSells.print_tour_message(x,hour,course_sel_for_message,people_number)
          TourSells.save_reservation(id_number,x,hour,course_sel_for_message,people_number)
      else:
        return 0

    elif course_selected == 3:
        course_sel_for_message= "'Trota por el pueblo'"
        x = 0
        hour='6PM'
        TourSells.print_tour_message(x,hour,course_sel_for_message,people_number)
        TourSells.save_reservation(id_number,x,hour,course_sel_for_message,people_number)

    
    elif course_selected== 4:
      if people_number >= 1 and people_number <= 4:
        course_sel_for_message= "'Visita lugares historicos'"
        new_number=sum(p)
        validation = new_number+people_number
        if validation > 15:
          print("No hay más cupo para este tour")
          return 0
        else:
          x=0
          hour='10AM'
          for i in range(1,people_number+1):
            if i >= 3:
              discount = 30*(10/100)
              x+= 30-discount
              TourSells.print_tour_message(x,hour,course_sel_for_message,people_number)
              TourSells.save_reservation(id_number,x,hour,course_sel_for_message,people_number)
              return people_number
            else:
              x+= 30
              TourSells.print_tour_message(x,hour,course_sel_for_message,people_number)
              TourSells.save_reservation(id_number,x,hour,course_sel_for_message,people_number)
              return people_number
      else:
        return 0
  def print_tour_message(x,hour,course_sel_for_message,people_number):
    if x == 0:
      print(f'''
Usted se ha suscrito al curso {course_sel_for_message}
    El curso es gratuito y empieza a {hour}
    numero de personas registradas {people_number}
    
    ''')
    else:
      print(f'''
Usted se ha suscrito al curso {course_sel_for_message}
    El curso tiene un precio de {x} dolares y empieza a {hour}
    numero de personas registradas {people_number}
    
    ''')

  def save_reservation(id_number,x,hour,course_sel_for_message,people_number):
    with open("TourInfo.txt", "a+") as a:
      a.write(f"{id_number},{x},{hour},  {course_sel_for_message}, {people_number}\n")