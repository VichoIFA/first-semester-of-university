import random
print('1-Hervidor')
print('2-Remedios')
print('3-Serie')
print('4-Mano de poker')
print('5-Usuarios')
print('6-Subsecuencia comun mas larga')
Npregunta=int(input('Ingrese el numero de la pregunta que desea revisar\n'))
#########################################
if Npregunta==1:
    x=random.randint(18,25)
    #seleccion de temperatura inicial
    while x<=94:
        print(x)
        x=x+2
    #bucle que se repite hasta llegar a los 94 grados celcius
        if x==93:
            x=x+1
    #opcion en caso de que el nunmero inicial fuese impar, esto hace que llegue hasta 93, pero 
    #esta esta opcion especifica para llegar a los 94 grados
            print(x)
    print('su cafe esta listo para servirse')
#########################################
if Npregunta==2:
    remedio=input('ingrese el tipo de medicamente para su abuela = ')
    año=int(input('ingrese el año del primer consumo = '))
    mes=int(input('ingrese el mes del primer consumo = '))
    fecha=int(input('ingrese el dia del consumo primer dosis = '))
    hora=int(input('ingrese la hora del consumo de la primera dosis = '))
    #ingreso de datos
    #para funcion de este programa, se fija la duracion de los meses a 30 dias, pero a diciembre
    #se le fija a 31 dias
    contador=0
    #la variable 'contador' indica los dias que han pasado, cuando llega a 14 es porque pasaron 
    #las 2 semanas
    if remedio=='a':
    #caso demedio a
        while contador<=14:
            print(año,'- Mes:',mes,', dia:',fecha,'-',hora,':00')
            hora=hora+8
            #suma de 8 horas a los datos iniciales
            if hora>24:
                fecha=fecha+1
                restante=hora-24
                hora=0
                hora=hora+restante
                contador=contador+1
                #caso de pasar de dia, es decir, que se superen las 24 horas
                #aca se suma uno a el contador para que pase de dia
                if mes==12:
                    if fecha==31:
                        año=año+1
                        fecha=1
                        mes=1
                        #caso de que se pase de diciembre, se suma un año
                if fecha>30:
                    mes=mes+1
                    fecha=1
                    #caso de que se pase de mes y este no sea diciembre
    if remedio=='b':
    #caso remedio b
        while contador<=14:
            print(año,'- Mes:',mes,', dia:',fecha,'-',hora,':00')
            hora=hora+12
            #suma de 12 horas a los datos iniciales
            if hora>24:
                fecha=fecha+1
                restante=hora-24
                hora=0
                hora=hora+restante
                contador=contador+1
                #caso de pasar de dia, es decir, que se superen las 24 horas
                #aca se suma uno a el contador para que pase de dia
                if mes==12:
                    if fecha==31:
                        año=año+1
                        fecha=1
                        mes=1
                        #caso de que se pase de diciembre, se suma un año
                if fecha>30:
                    mes=mes+1
                    fecha=1
                    #caso de que se pase de mes y este no sea diciembre
#########################################
if Npregunta==3:
    x=int(input('ingrese un numero = '))
    
    while (x)!=(1):
        #inicio de la cuenta
        print(x)
        if (x%2)!=0:
            x=(3*x)+1
            #caso de que x sea impar
        else:
            x=x/2
            #caso de que x sea par
    print('1.0')
    #fin de la serie
#########################################
if Npregunta==4:
    mazo_v=[]
    mazo_t=[]
    z=0
    cuenta=[]
    #creacion de las listas para guardar los datos
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10','Jota', 'Reina', 'Rey','As']
    tipos = ['Picas', 'Diamantes', 'Treboles', 'Corazones']
    
    while z<7:
        y=random.randint(0,3)
        y_tipos=tipos[y]
        x=random.randint(0,12)
        x_valores=valores[x]
        mazo_v.append(x_valores)
        mazo_t.append(y_tipos)
        z=z+1
        #seleccion de las cartas opara el mazo del jugador
    print(mazo_v)
    print(mazo_t)
    for w in mazo_v:
        if mazo_v.count(w)>=3:
            cuenta.append(w)
            #deteccion de los trios
 
    a=set(cuenta)
    b=list(a)
    #se eliminan los elementos repetidos de la lista cuenta, ya que con la fucnion anterior
    #se agrega 3 veces un mismo valor
    while len(b)>0:
        if len(b)==1:
            print('Con el mazo entregado ustedes puede formar un trio de ',*(b))
            break
        #se imprime un trio
        if len(b)==2:
            print('Con el mazo entregado ustedes puede formar un trio de ',b[0],'y',b[1])
            break
        #se imprimen los 2 tios
    if len(cuenta)==0:
        print('no con dicho mazo no puede formar ningun trio')
        #caso de no haber ningun trio
#########################################
if Npregunta==5:
    correo=[]
    Lcontraseña=[]
    usuario=[]
    llave=0
    gmail=input('ingrese su correo\n')
    if '@gmail.com' not in gmail:
        print('debe ingresar un correo valido')
        #caso de que el correo ingresado no sea @gmail.com
    else:    
        nombre_usuario=input('ingrese su nombre de usuario\n')
        correo.append(gmail[:-10:])
        usuario.append(nombre_usuario)
        a=False
        
        if correo[0]==usuario[0]:
            print('el nombre de usuario no puede ser igual al correo')
            #caso en el que el correo (sin el @gmail.com) sea igual a el nombre de usuario
        else:
            contraseña=input('ingrese su contraseña (debe tener minimo 8 caracteres, con al menos un numero y no puede tener los caracteres $, #, %, &, /)\n')
            if len(contraseña)<8:
                print('su contraseña no tiene 8 caracteres')
                #caso de que la contraseña no tenga minimo 8 caracteres
            else:
                if contraseña.isalpha():
                    #la funcion isalpha() corrobora si todos los elementos de un imput son texto
                    #en caso de que sea True significa que no hay un numero, por lo que lo saca del codigo
                    print('su contraseña necesita minimo un numero')
                    llave=1
                    #llave cambia a uno para que no desencadene otro mensaje que este con la misma tabulacion
                for z in contraseña:
                    if z=='$' or z=='#' or z=='%' or z=='&' or z=='/':
                        a=False
                        llave=2
                        #caso en el que la contraseña tenga estos simbolos, y llave cambia a 2
                        #debido a lo mismo mencionado anteriormente
                    else:
                        a=True
                        #a cambia a true para mostrar que se completo todo correctamente
                        
                if a and llave==0:
                    print('Su cuenta ha sido creada correctamente')
                    #la condicion de que llave sea 0 es para verificar que no se desencadeno
                    #algun mensaje de que no se pudo continuar con la creacion
                if llave==2:
                    print('su contraseña no puede tener los caracteres $, #, %, &, /.')
                    #el unico caso en el que llave es igual a 2 es cuando se detecta alguno de
                    #estos caracteres
#########################################
if Npregunta==6:
    oracion1=input('ingrese la primera oracion\n')
    oracion2=input('ingrese la segunda horacion\n')
    comun=[]
    largo=[]
    comun2=[]
    #primero se revisa cual de las cadenas es mas corta, para poder poder ocupar esa para recorrer
    #la mas larga, sin esto el programa me cortaba la secuencia mas larga
    if len(oracion1)>len(oracion2):
        for x in range(len(oracion2)):
            for y in range(len(oracion1)):
                if oracion2[x:y+1] in oracion1:
                    #deteccion de cadena
                    comun.append(oracion2[x:y+1])
                    #la cadena se agrega a la lista comun
    
    if len(oracion1)<len(oracion2):
        for x in range(len(oracion1)):
            for y in range(len(oracion2)):
                if oracion2[x:y+1] in oracion2:
                    #deteccion de cadena
                    comun.append(oracion1[x:y+1])
                    #la cadena se agrega a la lista comun
                    
    if len(oracion1)==len(oracion2):
        for x in range(len(oracion1)):
            for y in range(len(oracion2)):
                if oracion1[x:y+1] in oracion2:
                    #deteccion de cadena
                    comun.append(oracion1[x:y+1])  
                    #la cadena se agrega a la lista comun
    
    for z in range(len(comun)):
         largo=(len(comun[z]))
         comun2.append(largo)
         #se sacan los largos de cada cadena extraida con anterioridad, y ducho largo se agrega
         #a la lista comun2
    
    print('La secuencia mas larga entre los datos ingresados es : ',comun[comun2.index(max(comun2))])
    #se saca la posicion del valor maximo de la lista comun2, y en base a eso se llama a la primera
    #lista y se selecciona la cadena mas larga
