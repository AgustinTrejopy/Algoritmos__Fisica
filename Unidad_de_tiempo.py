datos = input("Las medidas son: \n<<<H>>> \n<<<M>>> \n<<<S>>> \nIngrese la medida que desea: ")

try:
    if datos == 'H' or datos == 'h':
       valor_h = input("Ingrese la cantidad de horas: ")
       valor_h = float(valor_h)
       h_a_m = valor_h * 60
       h_a_s = valor_h * 60 * 60

       valor_h = str(valor_h)
       h_a_m = str(h_a_m)
       h_a_s = str(h_a_s)

       print("\n|||LOS RESULTADOS SON...|||  \n\nHoras: " + valor_h +
          "\nMinutos: " + h_a_m +
          "\nSegundos: " + h_a_s)
     
    elif datos == 'M' or datos == 'm':
       valor_m = input("Ingrese la cantidad de minutos: ")
       valor_m = float(valor_m)
       m_a_h = valor_m / 60
       m_a_s = valor_m * 60

       valor_m = str(valor_m)
       m_a_h = str(m_a_h)
       m_a_s = str(m_a_s)

       print("\n|||LOS RESULTADOS SON...|||  \n\nHoras: " + m_a_h +
          "\nMinutos: " + valor_m +
          "\nSegundos: " + m_a_s)
       
    elif datos == 'S' or datos == 's':
       valor_s = input("Ingrese la cantidad de minutos: ")
       valor_s = float(valor_s)
       s_a_h = valor_s / 60 / 60
       s_a_m = valor_s / 60

       valor_s = str(valor_s)
       s_a_h = str(s_a_h)
       s_a_m = str(s_a_m)

       print("\n|||LOS RESULTADOS SON...|||  \n\nHoras: " + s_a_h +
          "\nMinutos: " + s_a_m +
          "\nSegundos: " + valor_s)

    else:
       print("ERROR!!! \nINGRESE LOS DATOS CORRECTAMENTE")

except ValueError:
   print("ERROR!!!! \n\nINGRESE UN VALOR NUMERICO!!!")
    