import math as mt
import numpy as np
import matplotlib.pyplot as plt
import imagem

class Mohr:
    
#################################
#################################
    sigmaxx = -21
    sigmayy = -11
    sigmaxy = 8
#################################
#################################


    sigma_m = ((sigmaxx + sigmayy) / 2) #Calcula o Sigma médio

    r = mt.sqrt(((sigmaxx - sigmayy) / 2)**2 + ((sigmaxy)**2)) #Calcula o raio

    sigma1 = sigma_m + r
    sigma2 = sigma_m - r

    cu1 = (2 * (sigmaxy))
    cu2 = ((sigmaxx) - (sigmayy))

    cu3 = (cu1/cu2)

    beta1 = 2*(mt.degrees((0.5)*(mt.atan(cu3))))

    r1 = round(r, 2)
    sigma11 = round(sigma1,2)
    sigma22 = round(sigma2,2)

    print('=='*15)
    print('     === Resultados ===  ')
    print ("        Raio : %.2f" % r)
    print ("        sigma M : %.2f" % sigma_m)
    print ("        sigma 1 : %.2f" % sigma1)
    print ("        sigma 2 : %.2f" % sigma2)
    print ("        beta1   : %.2f" % beta1)
    print('=='*15)
    theta = np.linspace(0, 2*np.pi, 360)

    x = sigma_m + r * np.cos(theta)
    y = r * np.sin(theta)

    plt.gca().invert_yaxis()
    plt.plot([sigma_m],[0], marker = 'o', color = 'k')
    plt.plot([sigma1],[0], marker = 'o', color = 'green')
    plt.plot([sigma2],[0], marker = 'o', color = 'green')

    plt.grid()

    'Labels'
    plt.title('Mohrs Circle', fontsize = 18)
    plt.ylabel(r'$\tau$', fontsize = 14)
    plt.xlabel(r'$\sigma$', fontsize = 14)
        
    plt.axhline(color = 'k')
    plt.axvline(color = 'k')
        
    'Adds fill to the circle'
    plt.fill_between(x, y, color = 'b', alpha = 0.1)

    plt.plot([sigma_m-r-10,sigma_m+r+10],[0,0],color='black')
    plt.plot([sigmaxx,sigma_m],[sigmaxy,sigmaxy],linestyle='--',color='k')
    plt.plot([sigma_m,sigma_m],[-r-10,r+10],linestyle='--',color='black')
    plt.plot([sigmaxx,sigma_m],[sigmaxy,0],linestyle='dotted',color='r')
    plt.plot([sigmaxx,sigmaxx],[sigmaxy,0],linestyle='--',color='k')
    plt.plot([sigmaxx],[sigmaxy],marker = 'o',color='k')

    plt.plot([sigma_m],[-r],marker = 'x',color='k') #Plot do R
    plt.plot([sigma_m],[r],marker = 'x',color='k')  #Plot do R

    plt.annotate((sigmaxx,sigmaxy), xy=(sigmaxx, sigmaxy), xytext=(sigmaxx+4, sigmaxy+4), arrowprops=dict(facecolor='black', arrowstyle='->'))

    plt.annotate(r1, xy=(sigma_m,r), xytext=(sigma_m-10,r+10), arrowprops=dict(facecolor='black', arrowstyle='->'))
    plt.annotate(-r1, xy=(sigma_m,-r), xytext=(sigma_m+10,-r-10), arrowprops=dict(facecolor='black', arrowstyle='->'))

    plt.annotate(sigma11, xy=(sigma1,0), xytext=(sigma1+10,sigmaxy), arrowprops=dict(facecolor='black', arrowstyle='->'))
    plt.annotate(sigma22, xy=(sigma2,0), xytext=(sigma2-10,sigmaxy), arrowprops=dict(facecolor='black', arrowstyle='->'))


    plt.plot(x,y)
    plt.xlabel(r'$\sigma$')
    plt.ylabel(r'$\tau$')
    plt.title("Mohr's Circle")
    plt.show()
    
    # import plotly.graph_objs as go

    # fig = go.Figure()

    # # Adds fill to the circle
    # fig.add_trace(go.Scatter(x=x, y=y, line_color='blue', name='Mohr Circle', line=dict(width=3)))
    

    # # Plots the normal stress points
    # fig.add_trace(go.Scatter(x=[sigma_m], y=[0], mode='markers', marker=dict(color='black', symbol='circle', size=8), name='Center'))
    # fig.add_trace(go.Scatter(x=[sigma1, sigma2], y=[0, 0], mode='markers', marker=dict(color='green', symbol='circle', size=8), name='Normal Stresses'))
    # fig.add_trace(go.Scatter(x=[sigma_m], y=[r], mode='markers', marker=dict(color='green', symbol='circle', size=8), name='Raio'))
    # fig.add_trace(go.Scatter(x=[sigma_m], y=[-r], mode='markers', marker=dict(color='green', symbol='circle', size=8), name='Raio'))
    # fig.add_trace(go.Scatter(x=[sigmaxx], y=[sigmaxy], mode='markers', marker=dict(color='green', symbol='circle', size=8)))

    # # Adds horizontal and vertical reference lines
    # fig.add_shape(type='line', x0=200, y0=0, x1=-200, y1=0, line=dict(color='black', width=3))#Eixo X
    # fig.add_shape(type='line', x0=0, y0=-200, x1=0, y1=200, line=dict(color='black', width=3))#Eixo Y

    # fig.add_shape(type='line', x0=sigma_m, y0=-r, x1=sigma_m, y1=r, line=dict(color='black', width=1, dash='dot'))#Eixo Y mostrando r ate -r

    # fig.add_shape(type='line', x0=sigma_m, y0=0, x1=sigmaxx, y1=sigmaxy, line=dict(color='red', width=1))#Diagonal moostrando 0°

    # fig.add_shape(type='line', x0=sigmaxx, y0=0, x1=sigmaxx, y1=sigmaxy, line=dict(color='black', width=1, dash='dot'))#Eixo X mostrando 0°
    # fig.add_shape(type='line', x0=sigma_m, y0=sigmaxy, x1=sigmaxx, y1=sigmaxy, line=dict(color='black', width=1, dash='dot'))#Eixo Y mostrando 0°


    # # Adds the labels and annotations
    # fig.update_layout(
    #     title='Mohr Circle',
    #     xaxis_title=r'$\sigma$',
    #     yaxis_title=r'$\tau$',
    #     xaxis=dict(zeroline=True, mirror=True),
    #     yaxis=dict(zeroline=True, mirror=True, autorange='reversed'),
    #     font=dict(size=12),
    #     annotations=[
    #         dict(x=sigma_m, y=0, xref='x', yref='y', text='Center', showarrow=False),
    #         dict(x=sigma1, y=0, xref='x', yref='y', text=f'σ1: {sigma11:.2f}', showarrow=True, arrowhead=1, ax=50, ay=-sigmaxy),
    #         dict(x=sigma2, y=0, xref='x', yref='y', text=f'σ2: {sigma22:.2f}', showarrow=True, arrowhead=1, ax=-50, ay=-sigmaxy),
    #         dict(x=sigma_m, y=r, xref='x', yref='y', text=f'r: {r1:.2f}', showarrow=True, arrowhead=1, ax=-50, ay=r),
    #         dict(x=sigma_m, y=-r, xref='x', yref='y', text=f'-r: {r1:.2f}', showarrow=True, arrowhead=1, ax=-50, ay=-r),
    #         dict(x=sigmaxx, y=sigmaxy, xref='x', yref='y', text=f'0°: {sigmaxx,sigmaxy}', showarrow=True, arrowhead=1, ax=-50, ay=r+10)
    #     ]
    # )

    #fig.show()



