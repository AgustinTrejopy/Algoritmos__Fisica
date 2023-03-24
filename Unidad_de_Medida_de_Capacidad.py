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
