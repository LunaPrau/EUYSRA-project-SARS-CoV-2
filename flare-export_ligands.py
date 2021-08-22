# ***STEP 1 IN FLARE*** 
# Alternatively, you can select and export your desired ligands into one sdf file using the GUI
from cresset import flare
import os

project = flare.main_window().project
ligands = project.ligands

os.chdir('/Users/ianyang/Desktop/University of Edinburgh/Third Year/EUYSRA/Docking Analysis/Flare/Repeat 1 Data')
# Write ALL the ligands into an sdf file
flare.write_file('site1_ligands.sdf',ligands)

# ***The loop does not work***
# for l in ligands: 
# 	if l.title.endswith('_D'):
# 		name = l.title.strip('_D')
# 		flare.write_file(name+'.pdb',l)

# ***STEP 2 in Pymol WITH "site1_ligands.sdf" OPENED***
multifilesave /Users/ianyang/Desktop/University of Edinburgh/Third Year/EUYSRA/Docking Analysis/Flare/Repeat 1 Data/ {}-{title}.pdb, state = 0

# Sometimes, states are saved as untitled. 
# If this happens, simply drag the desired ligand from Flare into Pymol and export as a pdb file

# ***STEP 3 on a command line***
# Move the docked ligands into their folders

cd /Users/ianyang/Desktop/University\of\Edinburgh/Third\Year/EUYSRA/Docking\Analysis/Flare/Repeat \1 \Data/
mv W_*.pdb docked_ligands/

mv W_*.pdb ~/Desktop/RMSD/Flare/Forsythoside_E/Site1/With_Water
mv *.pdb ~/Desktop/RMSD/Flare/Forsythoside_E/Site2/With_Water
mv *.pdb ~/Desktop/RMSD/Flare/Forsythoside_E/Site2/Without_Water
