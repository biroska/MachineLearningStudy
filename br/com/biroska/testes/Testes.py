import numpy as np
from br.com.biroska.pharmaceutical.file import Reader as reader
from br.com.biroska.pharmaceutical.view import Graphs  as graph

# salario = np.array([1100, 1500, 1300])
# print(salario)
# plt.plot( salario,c='r', ls= '--', marker='s' )
# plt.show()


dados = reader.getDataFromFile()

print(type(dados))


locations = []
year = []
pcHealth = []
PIB = []
cap = []
totalSpend = []

for d in dados:
    locations.append(d.location)
    year.append(d.year)
    pcHealth.append(d.percHealthExp)
    PIB.append(d.percPIB)
    cap.append(d.usdPerCapita)
    totalSpend.append(d.totalSpend)

dataMatrix = [ locations, year, pcHealth, PIB, cap, totalSpend ]


print( ' aad ' +dataMatrix[5][0] )

npMatrix = np.array( [ locations, year, pcHealth, PIB, cap, totalSpend ] )

print( npMatrix.shape )
print('--------------------')



print(npMatrix[5][0])
print(npMatrix[5])