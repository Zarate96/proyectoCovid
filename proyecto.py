'''
Código de proyecto final
'''

import os
import matplotlib.pyplot as plt

def get_data():
    data = []
    cifras = []
    with open("data.csv", "r") as file:
        for readline in file: 
            data.append((readline.split(',')))
    
    return data

def opc1():
    estados = []
    data_inicial = get_data()
    for estado in data_inicial[1:len(data_inicial)-1]:
        current = []
        current.append(estado[2])
        valores = estado[3:len(estado)]
        valores_enteros = [int(i) for i in valores]
        maximo = max(valores_enteros)
        maximo_index = valores_enteros.index(maximo)
        fecha = data_inicial[0][maximo_index+3]
        current.append(fecha)
        current.append(maximo)
        estados.append(current)
    
    nombre_estados = []
    valores = []
    for estado in estados:
        nombre_estados.append(estado[0])
        valores.append(estado[2])
    
    fig, (ax, ax2) =plt.subplots(1,2,figsize=(21,9))
    column_labels=["Estado", "Fecha", "Máximo"]
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=estados,colLabels=column_labels,loc="center")
    ax.set_title('Tabla con día con más casos a nivel nacional')
    ax2.plot(nombre_estados,valores)
    ax2.grid(True)
    ax2.set_ylim([0, 20000])
    ax2.set_ylabel('Contagios')
    plt.margins(0,1)
    plt.xticks(nombre_estados,rotation=90)
    plt.subplots_adjust(bottom=0.25)
    plt.show()

def opc2():
    estados = []
    data_inicial = get_data()
    for estado in data_inicial[1:len(data_inicial)]:
        current = []
        poblacion = int(estado[1])
        valores = estado[3:len(estado)]
        valores_enteros = [int(i) for i in valores]
        suma = sum(valores_enteros)
        porcentaje = round(((suma/poblacion)*100),2) 
        current.append(estado[2])
        current.append(poblacion)
        current.append(suma)
        current.append(porcentaje)
        estados.append(current)
    
    nombre_estados = []
    valores = []
    for estado in estados:
        nombre_estados.append(estado[0])
        valores.append(estado[3])

    fig, (ax, ax2) =plt.subplots(1,2,figsize=(20,9))
    column_labels=["Estado", "Población", "#Contagiados","Porcentaje"]
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=estados,colLabels=column_labels,loc="center")
    ax.set_title('Tabla con % Casos confirmados de acuerdo a la población')
    ax2.bar(nombre_estados,valores)
    ax2.grid(True)
    ax2.set_ylim([0, 16])
    ax2.set_ylabel('Porcentaje')
    plt.margins(0,1)
    plt.xticks(nombre_estados,rotation=90)
    plt.subplots_adjust(bottom=0.25)
    plt.show()

def opc3():
    rangos_meses = [[0,3],[4,34],[35,64],[65,95],[96,125],[126,156],[157,187],[188,217],[218,248],
                    [249,278],[279,309],[310,340],[341,368],[369,399],[400,429],[430,460],[461,490],
                    [491,521],[522,552],[553,582],[583,613],[614,643],[644,674],[675,705],[706,733],
                    [734,764],[765,794],[795,825],[826,837]]
    meses = ['AGUASCALIENTES','BAJA CALIFORNIA','BAJA CALIFORNIA SUR','CAMPECHE','CHIAPAS','CHIHUAHUA','DISTRITO FEDERAL','COAHUILA','COLIMA',
             'DURANGO','GUANAJUATO','GUERRERO','HIDALGO','JALISCO','MEXICO','MICHOACAN','MORELOS','NAYARIT','NUEVO LEON','OAXACA','PUEBLA','QUERETARO',
             'QUINTANA ROO','SAN LUIS POTOSI','SINALOA','SONORA','TABASCO','TAMAULIPAS','TLAXCALA','VERACRUZ','YUCATAN','ZACATECAS','Nacional']
    estados = []
    numero_meses = []
    suma_mes = []
    data_inicial = get_data()
    fechas = data_inicial[0][3:len(data_inicial[0])]
    flag = False
    while flag == False:
        mes = input("\n\tNombre de estado o Nacional: ")
        if mes in meses:
            flag = True
        else:
            print("Lugar inválido")
    
    estado_index = meses.index(mes)
    estado = data_inicial[estado_index+1]
    valores = estado[3:len(estado)]
    valores_enteros = [int(i) for i in valores]
    #print(valores_enteros)
    for i in range(0,len(rangos_meses)):
        pos1 = rangos_meses[i][0]
        pos2 = rangos_meses[i][1]
        suma = sum(valores_enteros[pos1:pos2+1])
        numero_meses.append(fechas[pos1])
        suma_mes.append(suma)
    
    maximo = max(suma_mes) 
    fig, ax =plt.subplots(figsize=(10,15))
    ax.set_title(f'Serie de tiempo mensual para {mes}')
    ax.grid(True)
    ax.plot(numero_meses,suma_mes)
    ax.set_ylim([0, maximo])
    plt.margins(0,1)
    plt.xticks(numero_meses,rotation=90)
    plt.subplots_adjust(bottom=0.25)
    plt.show()

def main():
    opc = ""
    while opc != "9":
        #Para Unix/Linux/MacOS/BSD
        #os.system ("clear") 
        #Para DOS/Windows
        os.system ("cls")
        try:
            print("\n\t" + "==== PROYECTO FINAL COVID19 ====")
            print("\t" + " ''' Por Hugo Zarate Ortiz '''")
            print("\n\t Menú de opciones ")
            print("\t 1. Día con más casos a nivel nacional ")
            print("\t 2. Proyectos no vencidos ")
            print("\t 3. Verificacion de envío de correo proyectos vencidos ")
            print("\t 9. Salir ")
            opc = input("\n\tIngrese una opción: ")
            
            if (opc == "1"):
                print("\n\t"+'*'*51) 
                print('\t\t Día con más casos a nivel nacional ')
                print("\t"+'*'*51)
                print("") 
                opc1()
            elif (opc == "2"):
                print("\n\t"+'*'*51) 
                print('\t\t  % Casos confirmados de acuerdo a la población ')
                print("\t"+'*'*51)
                print("") 
                opc2()
            elif (opc == "3"):
                print("\n\t"+'*'*51) 
                print('\t\t  Series de tiempo ')
                print("\t"+'*'*51)
                print("") 
                opc3()                

            elif (opc == "9"):
                print("\n ****** FIN DE LA EJECUCIÓN *******")
                break

            else:
                print("\n ****** OPCIÓN INVALIDA *******")
                input("\t Enter para continuar")
                
        except Exception as e:
            print("\n ****** Ha ocurrido un error *******")
            print(f'\n{e}') 

if __name__=='__main__':
    main()
