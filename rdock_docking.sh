#!/bin/bash

for dir in */
do
	cd $dir
	lig=${dir%/}
	printf "Start docking for ligand $lig."
	printf "\n"
	rbdock -r def_dock.prm -p dock.prm -n 10 -i $lig.sdf -o docking_out_1 > docking_out_1.log
	printf "Docking for ligand $lig complete."
	printf "\n\n"
	cd ..
done
