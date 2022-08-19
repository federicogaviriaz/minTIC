def CDT(nombre, monto, meses):
    totalMasIntereses = 0
    if meses <= 2:
        interes = 0.02
        interesesCalculados = monto*interes
        totalMasIntereses = monto - interesesCalculados
    else:
        interes = 0.03
        interesesCalculados = (monto*interes*meses)/12
        totalMasIntereses = monto+interesesCalculados
    return "Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}".format(
        nombre, monto, meses, totalMasIntereses)


print(CDT("Federico", 650000, 2))


# class cdtInfo:
#     nombreUsuario = " "
#     interesesUsuario = 0.02
#     montoUsuario = 0
#     mesesUsuario = 0

#     def __init__(self, nombre, capital, tiempo):
#         self.nombreUsuario = nombre
#         self.montoUsuario = capital
#         self.mesesUsuario = tiempo


# objCDT = cdtInfo(input("Por favor ingrese el nombre del usuario: \n "), int(input(
# #     "Ingrese el capital sin puntos: \n ")), int(input("Ingrese el tiempo en meses: \n ")))
# if objCDT.mesesUsuario < 2:
#     objCDT.interesesUsuario = 0.02
#     print("Para el usuario", objCDT.nombreUsuario, "La cantidad de dinero a recibir, según el monto inicial", objCDT.montoUsuario,
#           "para un tiempo de", objCDT.mesesUsuario, "meses es: ", float(cdtCalc(objCDT.montoUsuario, objCDT.interesesUsuario, objCDT.mesesUsuario))+objCDT.montoUsuario)
# else:
#     objCDT.interesesUsuario = 0.03
#     print("Para el usuario", objCDT.nombreUsuario, "La cantidad de dinero a recibir, según el monto inicial", objCDT.montoUsuario,
#           "para un tiempo de", objCDT.mesesUsuario, "meses es: ", float(
#               cdtCalc(objCDT.montoUsuario, objCDT.interesesUsuario, objCDT.mesesUsuario)))
