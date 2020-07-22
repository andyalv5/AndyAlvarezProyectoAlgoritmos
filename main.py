from room_management import RoomManagement
from cruise_management import CruiseManagement
from restaurant_management import RestaurantManagement
from tour_sells import TourSells
from statistics import Statistics
class main:
  def main():
    print("Bienvenido a Saman Caribbean!\n\n")
    n=[0]
    m=[0]
    p=[0]
    while True:
    
      try:
        data_input = int(input('''
Pulse (1) para consultar el catálogo de nuestros barcos disponibles
      
Pulse (2) para comprar billetes de crucero

Pulse (3) para hacer checkout

Pulse (4) para registrarse a un Tour

Pulse (5) para administrar el restaurante

Pulse (6) para comprobar las estadísticas

Pulse (7) para comprar la comida administrada por el restaurante
\n\n'''))
        if data_input == 1:
          CruiseManagement.cruises_available()
        elif data_input == 2:
          RoomManagement.room_check_in()
        elif data_input == 3:
          RoomManagement.check_out()
        elif data_input == 4:
          course_selected=int(input('''
Tour en el puerto [1]: 
    Precio de 30 dolares por persona,con descuento del 10% para la tercera y cuarta persona. empieza a las 7 AM.

Degustacion de comida local [2]:
    el precio es de 100 dolares por persona empieza a las 12 PM, es hasta 2 personas

Trotar por el pueblo/ciudad [3]:
    es gratis, empieza a las 6 AM

Visita a lugares historicos [4]:
    el precio es de 40 dolares por persona, con descuento de 10% a partir de la tercera, empieza a las 10 AM y es hasta 4 personas:
    '''))
          if course_selected == 1:
            n.append(TourSells.tour_check_in(n,m,p,course_selected))
          elif course_selected == 2:
            m.append(TourSells.tour_check_in(n,m,p,course_selected))
          elif course_selected == 3:
            TourSells.tour_check_in(n,m,p,course_selected)
          elif course_selected ==4:
            p.append(TourSells.tour_check_in(n,m,p,course_selected))

        elif data_input == 5:
          RestaurantManagement.process_of_selection()
        elif data_input==6:
          Statistics.check_average()
        elif data_input==7:
          RestaurantManagement.food_supplier()
      except:
        exit = input("\n\nDesea salir completamente del programa (y) or (n):").lower()
        if exit == "y":
          break
    

main.main()
