import py3Dmol 

# coronavirus nucleocapsid dimerisation domain 
view = py3Dmol.view(query='pdb:6wzo') 
view.setStyle({'cartoon':{'color':'spectrum'}}) 
view.show()

#SARS-CoV-2 bound to ACE-2 receptor 
see=py3Dmol.view(query='pdb:6M0J') 
see.setStyle({'cartoon':{'color':'spectrum'}}) 
see.show() 
