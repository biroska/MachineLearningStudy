import matplotlib.pyplot as plt

# salario = np.array([1100, 1500, 1300])
# print(salario)
# plt.plot( salario,c='r', ls= '--', marker='s' )
# plt.show()


def gerarGrafico( dataList ):

    print( dataList )

    plt.plot( dataList ,c='r', ls= '--', marker='s' )
    plt.show()