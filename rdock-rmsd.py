import mdtraj as md
import glob
import os
import csv
# Load data

# !!!This is for rDock!!!
# for d in directories
data = []
directories = ['Amentoflavone','Baicalein','Amentoflavone','Fisetin','Remdesivir','Apigenin','Forsythoside_E','Rhein', 'Baicalein',	'Hydroxychloroquine','Ritonavir'
'Baicalin',		'Hypericin','Rutin',
'Baricitinib',		'Hyperoside',		'Scutellarein',
'Berchemol',		'Ivermectin',		'Theaflavin_digallate',
'Camostat',		'Lopinavir',		'Torvoside_H',
'Chrysin',			'Myricetin',		'VTRRT',
'Curcumin',		'NHC',			'Wogonin',
'DAR',			'Nelfinavir',		'Wogonoside',
'Diammonium',		'Oryxylin_A', 'Disulfiram','Quercetin']
sites = ['Site1', 'Site2']
waters = ['With_Water', 'Without_Water']

#open csv file for writing
#open csv file for writing
with open ('/root/miniconda3/envs/rdock/share/rxdock-2013.1.1_148c5bd1-0/data/Flare_Trial/rmsd.csv','a') as RMSD:
    wr = csv.writer (RMSD, dialect = 'excel')
    title_row = ['ligand','RMSD_1v2','RMSD_1v3','RMSD_1v4']
    wr.writerow(title_row)

	for d in directories:
		all_files = glob.glob(d+"/*.pdb")
		print(all_files)
		# selecting a reference for all
		ref = md.load(all_files[0])[0]
		for f in all_files:
			print("Working on file: ",f )
			traj = md.load(f)
			lig = traj.top.select('resname MOL')
			rmsd = md.rmsd(traj[0], ref, atom_indices=lig)
			data.append(rmsd[0])
			print (data)

            #writing data
            row = []
            row.append(d+'/'+s+'/'+w)
            if len(data)%3 == 1: 
                row.append(str(data[-1]))
                wr.writerow(row)
            elif len(data)%3 == 2: 
                row.append(str(data[-1]))
                wr.writerow(row)
            elif len(data)%3 == 0:
                row.append(str(data[-1]))
                wr.writerow(row)
RMSD.close()


