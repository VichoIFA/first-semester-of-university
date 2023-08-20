def rotar_RD(rotor):
    variable=rotor[0]
    del rotor[0]
    rotor.append(variable)
    #funcion de rotacion del rotor derecho, elimina el valor 0 de la lista y lo agrega al
    #final con la funcion append

def rotar_RM(rotor_d,rotor_m):
    if rotor_d[0][0]=='V':
        variable2=rotor_m[0]
        del rotor_m[0]
        rotor_m.append(variable2)
        #funcion de toracion del rotor medio, verifica si la v esta en la parte superior del
        #rotor medio, y en caso de szer asi, se ejecuta la rotacion

def rotar_RI(rotor_d,rotor_m,rotor_i):
    if rotor_m[0][0]=='Q' and rotor_d[0][0]=='V':
        variable3=rotor_i[0]
        del rotor_i[0]
        rotor_i.append(variable3)
        #funcion de rotacion del rotor izquierdo, verifica las primeras letras del rotor medio
        #y derecho, y en caso de cumplirse las conidiciones, este rotara
        
def configurar_rotores(rotor_d,rotor_m,rotor_i,l1,l2,l3):
    while rotor_d[0][0]!=l1:
        variable=rotor_d[0]
        del rotor_d[0]
        rotor_d.append(variable)
    while rotor_m[0][0]!=l2:
        variable=rotor_m[0]
        del rotor_m[0]
        rotor_m.append(variable)
    while rotor_i[0][0]!=l3:
        variable=rotor_i[0]
        del rotor_i[0]
        rotor_i.append(variable)
        #funcion de configuracion de la posicion inicail de los rotores, para cada caso verifica
        #la letra inicial de cada rotor, y si no se cumple la condicion, se mantendra girando 
        #hasta completar la configuracion
        
def maquina_enigma(palabra,clave):
    lista_cifrado=[]
    lista_p=[x.upper() for x in palabra]
    #sepraracion de letras en la palabra
    
    abecedario=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U'
                ,'V','W','X','Y','Z']
    
    rotor_derecho=['AB','BD','CF','DH','EJ','FL','GC','HP','IR','JT','KX','LV','MZ','NN','OY','PE',
                   'QI','RW','SG','TA','UK','VM','WU','XS','YQ','ZO']
    
    rotor_medio=['AA','BJ','CD','DK','ES','FI','GR','HU','IX','JB','KL','LH','MW','NT','OM','PC',
                 'QQ','RG','SZ','TN','UP','VY','WF','XV','YO','ZE']
    
    rotor_izquierdo=['AE','BK','CM','DF','EL','FG','GD','HQ','IV','JZ','KN','LT','MO','NW','OY','PH'
                     ,'QX','RU','SS','TP','UA','VI','WB','XR','YC','ZJ']
    
    reflector=['A','B','C','D','E','F','G','D','I','J','K','G','M','K','M','I','E','B','F','T','C',
               'V','V','J','A','T']     
       
    letras_clave=[x.upper() for x in clave]
    #separacion de las letras de la clave
    configurar_rotores(rotor_derecho, rotor_medio, rotor_izquierdo, letras_clave[2], letras_clave[1], letras_clave[0])
    rotor_d1=rotor_d2=rotor_m1=rotor_m2=rotor_i1=rotor_i2=[]
    #configuracion inicial de la maquina para comenzar su funcionamiento
    
    for x in (lista_p):
        rotar_RM(rotor_derecho,rotor_medio)
        rotar_RI(rotor_derecho,rotor_medio,rotor_izquierdo)
        rotar_RD(rotor_derecho)
        #se verifica la condicion para ejecutar la rotacion en cada rotor en funcion de las letras
        #superiores
        ubicacion_reflector=[]
        rotor_d1=rotor_d2=rotor_m1=rotor_m2=rotor_i1=rotor_i2.clear()
        #se limpian las listas, ya que al estar en cambio no se pueden ocupar listas iguales
        #en diferentes momentos
        rotor_d1=[x[0] for x in rotor_derecho]
        rotor_d2=[x[1] for x in rotor_derecho]
        rotor_m1=[x[0] for x in rotor_medio]
        rotor_m2=[x[1] for x in rotor_medio]
        rotor_i1=[x[0] for x in rotor_izquierdo]
        rotor_i2=[x[1] for x in rotor_izquierdo]
        #separacion de los valores [0] y [1] de cada rotor en cada lista para ser manipulados
        #de manera mas comoda
        if x==' ':
            lista_cifrado.append(x)
            configurar_rotores(rotor_derecho, rotor_medio, rotor_izquierdo, letras_clave[2], letras_clave[1], letras_clave[0])
            #si la letra es un espacio, este se agrega a la lista y se reiniciaran los rotores
            #a la calve establecida
        else:
            cifrado1=rotor_d2[abecedario.index(x)]
            cifrado2=rotor_m2[rotor_d1.index(cifrado1)]
            cifrado3=rotor_i2[rotor_m1.index(cifrado2)]
            cambio_no_final_reflector=reflector[rotor_i1.index(cifrado3)]
            #si la letra no es un espacio, se sigue con el cifrado desde el rotor derecho
            #hasta el reflector
                
            for y in range(len(reflector)):
                if reflector[y]==cambio_no_final_reflector:
                    ubicacion_reflector.append(y)
                
            for z in ubicacion_reflector:
                if z!=rotor_i1.index(cifrado3):
                    ubicacion_reflector=z
                    #se verifica el index en el reflector y se compara con la funcion for
                    #para que no se refleje en la misma posicion
                
            cifrado4=rotor_i1[ubicacion_reflector]
            cifrado5=rotor_m1[rotor_i2.index(cifrado4)]
            cifrado6=rotor_d1[rotor_m2.index(cifrado5)]
            cifrado7=abecedario[rotor_d2.index(cifrado6)]
            #segundo cifrado desde el reflector hasta el rotor derecho
                
            lista_cifrado.append(cifrado7)
            #se agrega la letra cifrada a la lista llamada lista_cifrado
    resultado=''.join(lista_cifrado)
    #se transforma la lista a un str
    return(resultado)
    #se retorna la palabra cifrada
    
print('||||||||||||||||||||||||||||||||||||||||||||||')
print('||||||||||||||                  ||||||||||||||')
print('||||||||||||||  MAQUINA ENIGMA  ||||||||||||||')
print('||||||||||||||                  ||||||||||||||')
print('||||||||||||||||||||||||||||||||||||||||||||||')

palabra=input('ingrese la palabra que desea encriptar o desencriptar, solo debe poseer letras\n')
clave=input('ingrese la clave que desea ocupar para encriptarla, solo debe poseer tres letras')

try:
    print(f'la palabra encriptada encriptada o desencriptada es la siguiente: {maquina_enigma(palabra,clave)}')
except:
    print('los valores dados no son validos, intentelo nuevamente')