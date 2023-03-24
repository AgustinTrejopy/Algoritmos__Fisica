introduccion = input("""\nBIENVENIDO AL CONVERTIDOR DE UNIDADES DE MEDICION PARA FISICA:

<<<Unidad de longitud (Ingrese 'UDI')>>>
<<<Unidad de Medida de Capacidad (Ingrese 'UMC')>>>
<<<Unidad de tiempo (Ingrese 'UDT')>>>

Ingrese en que unidad de medicion desea calcular: """)


if introduccion == 'UDI' or introduccion == 'Udi' or introduccion == 'udi' or introduccion == 'UDi':

    datos = input("Las medidas son: \n<<<KM>>> \n<<<HM>>> \n<<<DECAM>>> \n<<<M>>> \n<<<DECIM>>> \n<<<CM>>> \n<<<MM>>> \nIngrese la medida que desea: ")
    
    try:
      
      if datos == 'KM' or datos == 'km':

        valor_km = input("Ingrese los kilometros: ")
        valor_km = float(valor_km)
        km_a_hm = valor_km * 10
        km_a_decam = valor_km * 10 * 10
        km_a_m = valor_km * 10 * 10 * 10
        km_a_decim = valor_km * 10 * 10 * 10 * 10
        km_a_cm = valor_km * 10 * 10 * 10 * 10 * 10
        km_a_mm = valor_km * 10 * 10 * 10 * 10 * 10 * 10

        valor_km = str(valor_km)
        km_a_hm = str(km_a_hm)
        km_a_decam = str(km_a_decam)
        km_a_m = str(km_a_m)
        km_a_decim = str(km_a_decim)
        km_a_cm = str(km_a_cm)
        km_a_mm = str(km_a_mm)

        print("\n|||LOS RESULTADOS SON...|||\n\nKilometros: " + valor_km +
              "\nHectometros: " + km_a_hm +
              "\nDecametros: " + km_a_decam +
              "\nMetros: " + km_a_m +
              "\nDecimetros: " + km_a_decim +
              "\nCentimetros: " + km_a_cm +
              "\nMilimetros: " + km_a_mm)

      elif datos == 'HM' or datos == 'hm':
         
         valor_hm = input("Ingrese los Hectometros: ")
         valor_hm = float(valor_hm)
         hm_a_km = valor_hm / 10
         hm_a_decam = valor_hm * 10
         hm_a_m = valor_hm * 10 * 10
         hm_a_decim = valor_hm * 10 * 10 * 10
         hm_a_cm = valor_hm * 10 * 10 * 10 * 10
         hm_a_mm = valor_hm * 10 * 10 * 10 * 10 * 10

         hm_a_km = str(hm_a_km)
         valor_hm = str(valor_hm)
         hm_a_decam = str(hm_a_decam)
         hm_a_m = str(hm_a_m)
         hm_a_decim = str(hm_a_decim)
         hm_a_cm = str(hm_a_cm)
         hm_a_mm = str(hm_a_mm)

         print("\n|||LOS RESULTADOS SON...|||\n\nKilometros: " + hm_a_km +
                "\nHectometros: " + valor_hm +
                "\nDecametros: " + hm_a_decam +
                "\nMetros: " + hm_a_m +
                "\nDecimetros: " + hm_a_decim +
                "\nCentimetros: " + hm_a_cm +
                "\nMilimetros: " + hm_a_mm)

      elif datos == 'DECAM' or datos == 'decam' or datos == 'Decam':
         
         valor_decam = input("Ingrese los Decametros: ")
         valor_decam = float(valor_decam)
         decam_a_km = valor_decam / 10 / 10 
         decam_a_hm = valor_decam / 10
         decam_a_m = valor_decam * 10
         decam_a_decim = valor_decam * 10 * 10
         decam_a_cm = valor_decam * 10 * 10 * 10
         decam_a_mm = valor_decam * 10 * 10 * 10 * 10

         decam_a_km = str(decam_a_km)
         decam_a_hm = str(decam_a_hm)
         valor_decam = str(valor_decam)
         decam_a_m = str(decam_a_m)
         decam_a_decim = str(decam_a_decim)
         decam_a_cm = str(decam_a_cm)
         decam_a_mm = str(decam_a_mm)

         print("\n|||LOS RESULTADOS SON...|||\n\nKilometros: " + decam_a_km +
                "\nHectometros: " + decam_a_hm +
                "\nDecametros: " + valor_decam +
                "\nMetros: " + decam_a_m +
                "\nDecimetros: " + decam_a_decim +
                "\nCentimetros: " + decam_a_cm +
                "\nMilimetros: " + decam_a_mm)  
          
      elif datos == 'M' or datos == 'm':
         
         valor_m = input("Ingrese los Metros: ")
         valor_m = float(valor_m)
         m_a_km = valor_m / 10 / 10 / 10
         m_a_hm = valor_m / 10 / 10
         m_a_decam = valor_m / 10
         m_a_decim = valor_m * 10 
         m_a_cm = valor_m * 10 * 10 
         m_a_mm = valor_m * 10 * 10 * 10 

         m_a_km = str(m_a_km)
         m_a_hm = str(m_a_hm)
         m_a_decam = str(m_a_decam)
         valor_m = str(valor_m)
         m_a_decim = str(m_a_decim)
         m_a_cm = str(m_a_cm)
         m_a_mm = str(m_a_mm)

         print("\n|||LOS RESULTADOS SON...|||\n\nKilometros: " + m_a_km +
                "\nHectometros: " + m_a_hm +
                "\nDecametros: " + m_a_decam +
                "\nMetros: " + valor_m +
                "\nDecimetros: " + m_a_decim +
                "\nCentimetros: " + m_a_cm +
                "\nMilimetros: " + m_a_mm)
        
      elif datos == 'DECIM' or datos == 'decim' or datos == 'Decim':
         
         valor_decim = input("Ingrese los Decimetros: ")
         valor_decim = float(valor_decim)
         decim_a_km = valor_decim / 10 / 10 / 10 / 10
         decim_a_hm = valor_decim / 10 / 10 / 10
         decim_a_m = valor_decim / 10 / 10
         decim_a_decam = valor_decim / 10
         decim_a_cm = valor_decim * 10 
         decim_a_mm = valor_decim * 10 * 10

         decim_a_km = str(decim_a_km)
         decim_a_hm = str(decim_a_hm)
         decim_a_decam = str(decim_a_decam)
         decim_a_m = str(decim_a_m)
         valor_decim = str(valor_decim)
         decim_a_cm = str(decim_a_cm)
         decim_a_mm = str(decim_a_mm)

         print("\n|||LOS RESULTADOS SON...|||\n\nKilometros: " + decim_a_km +
                "\nHectometros: " + decim_a_hm +
                "\nDecametros: " + decim_a_decam +
                "\nMetros: " + decim_a_m +
                "\nDecimetros: " + valor_decim +
                "\nCentimetros: " + decim_a_cm +
                "\nMilimetros: " + decim_a_mm)
        
      elif datos == 'CM' or datos == 'cm':
         
         valor_cm = input("Ingrese los Centimetros: ")
         valor_cm = float(valor_cm)
         cm_a_km = valor_cm / 10 / 10 / 10 / 10 / 10
         cm_a_hm = valor_cm / 10 / 10 / 10 / 10
         cm_a_decam = valor_cm / 10 / 10 / 10
         cm_a_m = valor_cm / 10 / 10 
         cm_a_decim = valor_cm / 10 
         cm_a_mm = valor_cm * 10  

         valor_cm = str(valor_cm)
         cm_a_km = str(cm_a_km)
         cm_a_hm = str(cm_a_hm)
         cm_a_decam = str(cm_a_decam)
         cm_a_m = str(cm_a_m)
         cm_a_decim = str(cm_a_decim)
         cm_a_cm = str(valor_cm)
         cm_a_mm = str(cm_a_mm)

         print("\n|||LOS RESULTADOS SON...|||\n\nKilometros: " + cm_a_km +
                "\nHectometros: " + cm_a_hm +
                "\nDecametros: " + cm_a_decam +
                "\nMetros: " + cm_a_m +
                "\nDecimetros: " + cm_a_decim +
                "\nCentimetros: " + valor_cm +
                "\nMilimetros: " + cm_a_mm)
        
      elif datos == 'MM' or datos == 'mm':
         
         valor_mm = input("Ingrese los Milimetros: ")
         valor_mm = float(valor_mm)
         mm_a_km = valor_mm / 10 / 10 / 10 / 10 / 10 / 10
         mm_a_hm = valor_mm / 10 / 10 / 10 / 10 / 10
         mm_a_decam = valor_mm / 10 / 10 / 10 / 10
         mm_a_m = valor_mm / 10 / 10 / 10
         mm_a_decim = valor_mm / 10 / 10 
         mm_a_cm = valor_mm / 10  

         valor_mm = str(valor_mm)
         mm_a_km = str(mm_a_km)
         mm_a_hm = str(mm_a_hm)
         mm_a_decam = str(mm_a_decam)
         mm_a_m = str(mm_a_m)
         mm_a_decim = str(mm_a_decim)
         mm_a_cm = str(mm_a_cm)
        

         print("\n|||LOS RESULTADOS SON...|||\n\nKilometros: " + mm_a_km +
                "\nHectometros: " + mm_a_hm +
                "\nDecametros: " + mm_a_decam +
                "\nMetros: " + mm_a_m +
                "\nDecimetros: " + mm_a_decim +
                "\nCentimetros: " + mm_a_cm +
                "\nMilimetros: " + valor_mm)
         
      else:
       print("\nERROR!!! \nINGRESE LOS DATOS CORRECTAMENTE")

    except ValueError:
       print("\nERROR!!!! \n\nINGRESE UN VALOR NUMERICO!!!")

elif introduccion == 'UMC' or introduccion == 'umc' or introduccion == 'Umc':

    datos = input("Las medidas son: \n<<<KL>>> \n<<<HL>>> \n<<<DECAL>>> \n<<<L>>> \n<<<DECIL>>> \n<<<CL>>> \n<<<ML>>> \nIngrese la medida que desea: ")

    try:
        if datos == 'KL' or datos == 'kl' or datos == 'Kl':
            valor_kl = input("Ingrese los Kilolitros: ")
            valor_kl = float(valor_kl)
            kl_a_hl = valor_kl * 10
            kl_a_decal = valor_kl * 10 * 10
            kl_a_l = valor_kl * 10 * 10 * 10
            kl_a_decil = valor_kl * 10 * 10 * 10 * 10
            kl_a_cl = valor_kl * 10 * 10 * 10 * 10 * 10
            kl_a_ml = valor_kl * 10 * 10 * 10 * 10 * 10 * 10

            valor_kl = str(valor_kl)
            kl_a_hl = str(kl_a_hl)
            kl_a_decal = str(kl_a_decal)
            kl_a_l = str(kl_a_l)
            kl_a_decil = str(kl_a_decil)
            kl_a_cl = str(kl_a_cl)
            kl_a_ml = str(kl_a_ml)

            print("\n|||LOS RESULTADOS SON...|||\n\nKilolitros: " + valor_kl +
                "\nHectolitros: " + kl_a_hl +
                "\nDecalitros: " + kl_a_decal +
                "\nLitros: " + kl_a_l +
                "\nDecilitros: " + kl_a_decil +
                "\nCentilitros: " + kl_a_cl +
                "\nMililitros: " + kl_a_ml)

        elif datos == 'HL' or datos == 'hl' or datos == 'Hl':

            valor_hl = input("Ingrese los Hectolitros: ")
            valor_hl = float(valor_hl)
            hl_a_kl = valor_hl / 10
            hl_a_decal = valor_hl * 10
            hl_a_l = valor_hl * 10 * 10
            hl_a_decil = valor_hl * 10 * 10 * 10
            hl_a_cl = valor_hl * 10 * 10 * 10 * 10
            hl_a_ml = valor_hl * 10 * 10 * 10 * 10 * 10

            hl_a_kl = str(hl_a_kl)
            valor_hl = str(valor_hl)
            hl_a_decal = str(hl_a_decal)
            hl_a_l = str(hl_a_l)
            hl_a_decil = str(hl_a_decil)
            hl_a_cl = str(hl_a_cl)
            hl_a_ml = str(hl_a_ml)

            print("\n|||LOS RESULTADOS SON...|||\n\nKilolitros: " + hl_a_kl +
                "\nHectolitros: " + valor_hl +
                "\nDecalitros: " + hl_a_decal +
                "\nLitros: " + hl_a_l +
                "\nDecimetros: " + hl_a_decil +
                "\nCentimetros: " + hl_a_cl +
                "\nMilimetros: " + hl_a_ml)
 
        elif datos == 'DECAL' or datos == 'decal' or datos == 'Decal':

            valor_decal = input("Ingrese los Decalitros: ")
            valor_decal = float(valor_decal)
            decal_a_kl = valor_decal / 10 / 10 
            decal_a_hl = valor_decal / 10
            decal_a_l = valor_decal * 10
            decal_a_decil = valor_decal * 10 * 10
            decal_a_cl = valor_decal * 10 * 10 * 10
            decal_a_ml = valor_decal * 10 * 10 * 10 * 10

            decal_a_kl = str(decal_a_kl)
            decal_a_hl = str(decal_a_hl)
            valor_decal = str(valor_decal)
            decal_a_l = str(decal_a_l)
            decal_a_decil = str(decal_a_decil)
            decal_a_cl = str(decal_a_cl)
            decal_a_ml = str(decal_a_ml)

            print("\n|||LOS RESULTADOS SON...|||\n\nKilolitros: " + decal_a_kl +
                "\nHectolitros: " + decal_a_hl +
                "\nDecalitros: " + valor_decal +
                "\nLitros: " + decal_a_l +
                "\nDecilitros: " + decal_a_decil +
                "\nCentilitros: " + decal_a_cl +
                "\nMililitros: " + decal_a_ml)  
          
        elif datos == 'L' or datos == 'l':

            valor_l = input("Ingrese los Litros: ")
            valor_l = float(valor_l)
            l_a_kl = valor_l / 10 / 10 / 10
            l_a_hl = valor_l / 10 / 10
            l_a_decal = valor_l / 10
            l_a_decil = valor_l * 10 
            l_a_cl = valor_l * 10 * 10 
            l_a_ml = valor_l * 10 * 10 * 10 

            l_a_kl = str(l_a_kl)
            l_a_hl = str(l_a_hl)
            l_a_decal = str(l_a_decal)
            lvalor_l = str(valor_l)
            l_a_decil = str(l_a_decil)
            l_a_cl = str(l_a_cl)
            l_a_ml = str(l_a_ml)

            print("\n|||LOS RESULTADOS SON...|||\n\nKilolitros: " + l_a_kl +
                "\nHectolitros: " + l_a_hl +
                "\nDecalitros: " + l_a_decal +
                "\nLitros: " + valor_l +
                "\nDecilitros: " + l_a_decil +
                "\nCentilitros: " + l_a_cl +
                "\nMililitros: " + l_a_ml)
        
        elif datos == 'DECIL' or datos == 'decil' or datos == 'Decil':

            valor_decil = input("Ingrese los Decilitros: ")
            valor_decil = float(valor_decil)
            decil_a_kl = valor_decil / 10 / 10 / 10 / 10
            decil_a_hl = valor_decil / 10 / 10 / 10
            decil_a_l = valor_decil / 10 / 10
            decil_a_decal = valor_decil / 10
            decil_a_cl = valor_decil * 10 
            decil_a_ml = valor_decil * 10 * 10

            decil_a_kl = str(decil_a_kl)
            decil_a_hl = str(decil_a_hl)
            decil_a_decal = str(decil_a_decal)
            decil_a_l = str(decil_a_l)
            valor_decil = str(valor_decil)
            decil_a_cl = str(decil_a_cl)
            decil_a_ml = str(decil_a_ml)

            print("\n|||LOS RESULTADOS SON...|||\n\nKilolitros: " + decil_a_kl +
                "\nHectolitros: " + decil_a_hl +
                "\nDecalitros: " + decil_a_decal +
                "\nLitros: " + decil_a_l +
                "\nDecilitros: " + valor_decil +
                "\nCentilitros: " + decil_a_cl +
                "\nMililitros: " + decil_a_ml)
        
        elif datos == 'CL' or datos == 'cl' or datos == 'Cl':

            valor_cl = input("Ingrese los Centilitros: ")
            valor_cl = float(valor_cl)
            cl_a_kl = valor_cl / 10 / 10 / 10 / 10 / 10
            cl_a_hl = valor_cl / 10 / 10 / 10 / 10
            cl_a_decal = valor_cl / 10 / 10 / 10
            cl_a_l = valor_cl / 10 / 10 
            cl_a_decil = valor_cl / 10 
            cl_a_ml = valor_cl * 10  

            valor_cl = str(valor_cl)
            cl_a_kl = str(cl_a_kl)
            cl_a_hl = str(cl_a_hl)
            cl_a_decal = str(cl_a_decal)
            cl_a_l = str(cl_a_l)
            cl_a_decil = str(cl_a_decil)
            cl_a_cl = str(valor_cl)
            cl_a_ml = str(cl_a_ml)

            print("\n|||LOS RESULTADOS SON...|||\n\nKilolitros: " + cl_a_kl +
                "\nHectolitros: " + cl_a_hl +
                "\nDecalitros: " + cl_a_decal +
                "\nLitros: " + cl_a_l +
                "\nDecilitros: " + cl_a_decil +
                "\nCentilitros: " + valor_cl +
                "\nMililitros: " + cl_a_ml)
        
        elif datos == 'ML' or datos == 'ml' or datos == 'Ml':

            valor_ml= input("Ingrese los Mililitros: ")
            valor_ml = float(valor_ml)
            ml_a_kl = valor_ml / 10 / 10 / 10 / 10 / 10 / 10
            ml_a_hl = valor_ml / 10 / 10 / 10 / 10 / 10
            ml_a_decal = valor_ml / 10 / 10 / 10 / 10
            ml_a_l = valor_ml / 10 / 10 / 10
            ml_a_decil = valor_ml / 10 / 10 
            ml_a_cl = valor_ml / 10  

            valor_ml = str(valor_ml)
            ml_a_kl = str(ml_a_kl)
            ml_a_hl = str(ml_a_hl)
            ml_a_decal = str(ml_a_decal)
            ml_a_l = str(ml_a_l)
            ml_a_decil = str(ml_a_decil)
            ml_a_cl = str(ml_a_cl)
            

            print("\n|||LOS RESULTADOS SON...|||\n\nKilolitros: " + ml_a_kl +
                "\nHectolitros: " + ml_a_hl +
                "\nDecalitros: " + ml_a_decal +
                "\nLitros: " + ml_a_l +
                "\nDecilitros: " + ml_a_decil +
                "\nCentilitros: " + ml_a_cl +
                "\nMililitros: " + valor_ml)
        
        else:
            print("ERROR!!! \nINGRESE LOS DATOS CORRECTAMENTE")

    except ValueError:
        print("ERROR!!!! \n\nINGRESE UN VALOR NUMERICO!!!")

elif introduccion == 'UDT' or introduccion == 'udt' or introduccion == 'Udt':

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
    
else:
    print("\nERROR!!!! \nINGRESE LOS DATOS  CORRECTAMENTE")