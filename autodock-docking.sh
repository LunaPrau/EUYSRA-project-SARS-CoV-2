#!/bin/bash

for dir in */
do
	cd $dir
	lig=${dir%/}
	printf "Start docking for ligand $lig."
	printf "\n"
	/Users/ianyang/Desktop/Autodock_Vina/autodock_vina_1_1_2_mac_catalina_64bit/bin/vina  --receptor Site1_with_water.pdbqt --ligand $lig.pdbqt --config config.txt --log log.txt --out output.pdbqt
	printf "Docking for ligand $lig complete."
	printf "\n\n"
	cd ..
done