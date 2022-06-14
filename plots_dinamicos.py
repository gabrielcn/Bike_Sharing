import matplotlib.pyplot as plt
import pandas as pd

plt.ion()

for i in range(1):

    customer_media_chicago = 31
    subscriber_media_chicago = 12.1


    customer_media_ny = 33
    subscriber_media_ny = 13.7

    customer_media_was = 41.7
    subscriber_media_was = 12.5

    df_media_viagem = pd.DataFrame([['Chicago', subscriber_media_chicago, customer_media_chicago], ['NY', subscriber_media_ny, customer_media_ny], ['Was', subscriber_media_was, customer_media_was]], columns=['City', 'Subscribers', 'Customers'])

# Alterando a cor da parte externa e o tamanho do gráfico
    plt.figure(facecolor= '#CBEAFA', figsize=(10,6))

# Alterando a cor de fundo
    ax = plt.axes() 
    ax.set_facecolor("white")

# Cores
    color = ['#73d2de','#218380']

# Inserindo argumento de cor
    plot = df_media_viagem.plot(x='City', kind='bar', color=(color), ax=ax)

# Inserindo labels numéricos nas barras
    for i in plot.patches:
        plot.annotate(i.get_height(), (i.get_x() + i.get_width() / 2, i.get_height()), 
                ha='center', va="baseline", fontsize = 12, color="black", xytext=(0, 1), textcoords='offset points')

# Eixo x
    plt.xlabel("cidade", size = 12, fontweight="bold")
    plt.xticks(rotation=0) # Deixa os valores no eixo x em 0°

# Eixo y
    plt.ylabel("tempo (min)" , size = 12, fontweight="bold") 

# Titulo
    plt.title("Duração média de viagem" , size = 24, fontweight="bold")

    plt.pause(3)

    plt.cla()
    plt.clf()

    sub_chicago = 54982
    sub_ny = 245896
    sub_was = 51753

    cust_chicago = 17149
    cust_ny = 30185
    cust_was = 14573

    df_sub_and_cust = pd.DataFrame([['Chicago', sub_chicago, cust_chicago], ['NY', sub_ny, cust_ny], ['Was', sub_was, cust_was]], columns=['City', 'Subscribers', 'Customers'])

# Alterando a cor da parte externa 
    plt.figure(facecolor= '#f7f2f6')

# Alterando a cor de fundo
    ax = plt.axes() 
    ax.set_facecolor("white") 

# Cores das barras
    color = ['#990066','#a46497']



# Inserindo argumento de cor
    plot2 = df_sub_and_cust.plot(x='City', kind='bar', color=(color), ax=ax, figsize=(10,6))

# Inserindo labels numéricos nas barras
    for i in plot2.patches:
        plot2.annotate(i.get_height(), (i.get_x() + i.get_width() / 2, i.get_height()), 
        ha='center', va="baseline", fontsize = 12, color="black", xytext=(0, 1), textcoords='offset points')

# Eixo x
    plt.xlabel("cidade", size = 15, fontweight = "bold")
    plt.xticks(rotation=0) # Deixa os valores no eixo x em 0°

# Eixo y
    plt.ylabel("n°/usuários" , size = 15, fontweight = "bold") 

# Titulo
    plt.title("Número de usuarios por cidade" , size = 24, fontweight = "bold")

    plt.pause(3)

plt.ioff()
plt.show()