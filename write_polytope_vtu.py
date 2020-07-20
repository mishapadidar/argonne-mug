import numpy as np
from vtkClass import VTK_XML_Serial_Unstructured 
vtk_writer =VTK_XML_Serial_Unstructured()

phi = (1.+np.sqrt(5))/2.0
# create .vtu files of the data
x = np.array([0.,0, 0., 0.,phi,phi, -phi, -phi,1.,-1.,1.,-1.])
y = np.array([1.,-1.,1., -1.,0.,0, 0., 0.,phi,phi, -phi, -phi])
z = np.array([phi,phi, -phi, -phi,1.,-1.,1.,-1.,0.,0, 0., 0.])

#color the particle undergoining 
colors   =np.zeros_like(x)
# colors[0:numForceP:] =1.0	
outFile  = './polytope.vtu'
vtk_writer.snapshot(outFile, x,y,z,[],[],[],[],[],[],[],colors)	#show velocity in vtu 
#	vtk_writer.snapshot(outFile, x,y,z,[],[],[],Fx,Fy,Fz,[],colors)	#show force in vtu	
