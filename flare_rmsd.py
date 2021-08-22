# Import all my shenanigans
import mdtraj as md
import glob
import os
import csv
from csv import writer
#import warnings

# Make my function to append stuff
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

# Make CSV file and title rows
with open ('flare_rmsd_05.csv', "w") as f:
	wr = csv.writer(f,dialect= 'excel')
	title_row = ['Ligand_Name','Site_Number', 'With_Or_Without_Water', 'RMSD Value']
	append_list_as_row ('flare_rmsd_05.csv', title_row)
f.close()

# Calculate rmsd and write into csv file
data = []
Ligands = ['Baicalein', 'Baicalin', 'NHC', 'DAR', 'Diammonium', 'Forsythoside', 'Lopinavir' 'VTRRT', 'Wogonin', 'Wogonoside']
Sites = ['Site1', 'Site2', 'Site3d', 'Site3m']
Waters = ['With_Water', 'Without_Water']
#Ligands = ['DAR_DIR', 'Diammonium', 'VTRRT',] # Ligands with no errors
for l in Ligands:
	for s in Sites:
		for w in Waters:
				all_files = glob.glob(l+'/'+s+'/'+w+"/*.pdb")
				print(all_files)
				# selectign a reference for all
				if len(all_files) == 4: #Change to 4 when i have ian's files
					ref = md.load(all_files[0])[0]
					for af in all_files:
						#warnings.filterwarnings("ignore", message="Casting atom_indices dtype=float64 to <class 'int'> ")
						print("Working on file: ",af )
						traj = md.load(af)
						if len(traj.top.select('resname MOL')) != 0:
							lig_MOL = traj.top.select('resname MOL')
							rmsd = md.rmsd(traj[0], ref, atom_indices=lig_MOL)
							# Print data into csv file
							row_contents = [l, s, w, str(rmsd[0])]
							append_list_as_row('flare_rmsd_05.csv', row_contents)
						elif len(traj.top.select('resname UNK')) != 0:		
							lig_UNK = traj.top.select('resname UNK')
							rmsd = md.rmsd(traj[0], ref, atom_indices=lig_UNK)
							# Print data into csv file
							row_contents = [l, s, w, str(rmsd[0])]
							append_list_as_row('flare_rmsd_05.csv', row_contents)
print(data)

# directories = ['Amentoflavone', 'Apigenin', 'Baicalein', 'Baicalin', 'Baricitinib', 'Berchemol', 'Camostat', 'Chrysin', 'Curcumin', 'DAR', 'Diammonium', 'Disulfiram', 'Fisetin', 'Forsythoside_E', 'Hydroxychloroquine', 'Hypericin', 'Hyperoside', 'Ivermectin', 'Lopinavir', 'Myricetin', 'Nelfinavir', 'NHC', 'Oryxylin_A', 'Quercetin', 'Remdesivir', 'Rhein', 'Ritonavir', 'Rutin', 'Scutellarein', 'Theaflavin_digallate', 'Torvoside_H', 'VTRRT', 'Wogonin', 'Wogonoside'] # In the following line you list all the 
