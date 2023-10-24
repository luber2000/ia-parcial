#################################
# Segmentacion de imagen a la "Grab Cut" simplificado
#################################


import numpy as np

import maxflow
import matplotlib.pyplot as plt
import codigo.select_pixels as sel
import cv2

imgName='horse.jpg'

imgbgr = cv2.imread(imgName)
img = cv2.cvtColor(imgbgr, cv2.COLOR_RGB2BGR)

# Marco algunos pixeles que pertenecen el objeto y el fondo
markedImg = sel.select_fg_bg(img)

# creando el grafo
g = maxflow.Graph[float]()

#Añade los nodos. nodeids tiene los identificadores de los nodos en el grid
nodeids = g.add_grid_nodes(img.shape[:2])

# Calcula los costes de los nodos no terminales del grafo

# Estos son los costes de los vecinos horizontales
exp_aff_h=
# Estos son los costes de los vecinos verticales
exp_aff_v=

# Construyo el grafo 
# Para construir el grafo relleno las estructuras
hor_struc=np.array([[0, 0, 0],[1, 0, 0],[0, 0, 0]])
ver_struc=np.array([[0, 1, 0],[0, 0, 0],[0, 0, 0]])
# Construyo el grafo 
g.add_grid_edges(nodeids, exp_aff_h, hor_struc,symmetric=True)
g.add_grid_edges(nodeids, exp_aff_v, ver_struc,symmetric=True)

# Leo los pixeles etiquetados
# Los marcados en rojo representan el objeto
pts_fg = np.transpose(np.where(np.all(np.equal(markedImg,(255,0,0)),2)))
# Los marcados en verde representan el fondo
pts_bg = np.transpose(np.where(np.all(np.equal(markedImg,(0,255,0)),2)))

# Incluyo las conexiones a los nodos terminales
# Pesos de los nodos terminales
g.add_grid_tedges(nodeids[pts_fg[:,0],pts_fg[:,1]], ...)
g.add_grid_tedges(nodeids[pts_bg[:,0],pts_bg[:,1]], ...)

# Encuentra el flujo maximo
g.maxflow()
# obtiene los segmentos de los nodos en el grid.
sgm = g.get_grid_segments(nodeids)

# Muestro el resultado de la segmentacion
plt.figure()
plt.imshow(np.uint8(np.logical_not(sgm)),cmap='gray')
plt.show()

# Lo muestro junto con la imagen para ver el resultado
plt.figure()
wgs=(np.float_(np.logical_not(sgm))+0.3)/1.3

# Replico los pesos para cada canal y ordeno los indices
wgs=np.rollaxis(np.tile(wgs,(3,1,1)),0,3)
plt.imshow(np.uint8(np.multiply(img,wgs)))
plt.show()
