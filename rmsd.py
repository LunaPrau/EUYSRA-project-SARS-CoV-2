import mdtraj as md
import glob
import os
# Load data

# for d in directories
data = []
directories = ['Ritonavir', 'Rutin', 'Apigenin', 'Scutellarein', 'Disulfiram', 'Hypericin', 'Amentoflavone', 'Torvoside_H', 'Fisetin']
sites = ['Site1', 'Site2']
waters = ['With_Water', 'Without_Water']
for d in directories:
	for s in sites:
		for w in waters:
			all_files = glob.glob(d+'/'+s+'/'+w+"/*.pdb")
			print(all_files)
			# selectign a reference for all
			ref = md.load(all_files[0])[0]
			for f in all_files:
				print("Working on file: ",f )
				traj = md.load(f)
				lig = traj.top.select('resname MOL')
				rmsd = md.rmsd(traj[0], ref, atom_indices=lig)
				data.append(rmsd[0])

print(data)