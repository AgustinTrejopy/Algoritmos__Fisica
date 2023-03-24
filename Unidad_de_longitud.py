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
     print("ERROR!!!! \n\nINGRESE UN VALOR NUMERICO!!!")
