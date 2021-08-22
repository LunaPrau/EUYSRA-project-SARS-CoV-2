cd ~/autodock_rmsd/trial

# Change all file names so there are no spaces so script changing pdbqt to pdb can work
for rpt in */
do
	cd $rpt
	for lig in */
	do
		cd $lig
		for site1 in S*1/
		do
			if [ -d "$site1" ]
			then
				mv "${site1}" "Site1" || echo 'Could not rename '"$site1"''
    		fi
		done

		for site2 in S*2/
		do
			if [ -d "$site2" ]
			then
				mv "${site2}" "Site2" || echo 'Could not rename '"$site2"''
    		fi
		done

		for site3d in S*3*D*/
		do
			if [ -d "$site3d" ]
			then
				mv "${site3d}" "Site3d" || echo 'Could not rename '"$site3d"''
    		fi
		done

		for site3m in S*3*M*/
		do
			if [ -d "$site3m" ]
			then
				mv "${site3m}" "Site3m" || echo 'Could not rename '"$site3m"''
    		fi
		done

		for site in */
		do
			cd $site
			for wo_water in Witho*/
			do
				if [ -d "$wo_water" ]
				then
					mv "${wo_water}" "Without_Water" || echo 'Could not rename '"$wo_water"''
    			fi
			done

			for w_water in With?W*/
			do
				if [ -d "$w_water" ]
				then
					mv "${w_water}" "With_Water" || echo 'Could not rename '"$w_water"''
    			fi
			done
                
            printf "Changed dir names for $lig."
            printf "\n"

			cd ..
		done
		cd ..
	done
	cd ..
done

cd ~/autodock_rmsd/trial

### DO NOT USE Change pdbqt to pdb - do it in cmd using the code at the bottom
for rpt in Rpt*/
do
	cd $rpt
	for lig in */
	do
		cd $lig
		for site in */
		do
			cd $site
			for water in */
			do
				cd $water
				printf "Opening $lig file."
				printf "\n"
				output.pdbqt
				printf "Finished opening $lig file."
				printf "\n\n"
				cd ..
			done
			cd ..
		done
		cd ..
	done
	cd ..
done

# When converting pdbqt to pdb I tried the following (and they failed giving an index error)
## cut -c-66 file.pdbqt > file.pdb
## cut -c file.pdbqt > file.pdb
## babel -ipdbqt 'filename.pdbqt' -opdb 'filename.pdb' #THIS IS A LINUX COMMAND DON'T TRY AND RUN IN WINDOWS
## pymol pdbqt_to_pdb.pml #Try to execute a pymol script


### AFTER CONVERTING PDBQT TO PDB DO THIS move rpts into the right folder so we can do rmsd

for rpt in *1/
do
	cd $rpt
	for lig in */
	do
		cd $lig
		for site in */
		do
			cd $site
			for water in */
			do
				cd $water
				mv output.pdb Rpt1.pdb
				cd ..
			done
			cd ..
		done
		cd ..
	done
	cd ..
done

for rpt in *2/
do
	cd $rpt
	for lig in */
	do
		cd $lig
		for site in */
		do
			cd $site
			for water in */
			do
				cd $water
				mv output.pdb Rpt2.pdb
				cd ..
			done
			cd ..
		done
		cd ..
	done
	cd ..
done


for rpt in */
do
	cd $rpt
	for lig in */
	do
		cd $lig
		for site in */
		do
			cd $site
			for water in */
			do
				cd $water
				printf "Moving outputs for $lig."
				printf "\n"
				mkdir -p ~/autodock_rmsd/trial/$lig/$site/$water
				cp *.pdb ~/autodock_rmsd/trial/$lig/$site/$water
				printf "Finished moving outputs for $lig."
				printf "\n\n"
				cd ..
			done
			cd ..
		done
		cd ..
	done
	cd ..
done

### DO NOT USE cmd open all output files ##############################################################################################################

for %r in (Rpt1 Rpt2) do (
	for %l in (Beta Bicalein Bicalin DAR_DIR Diammonium Forsythoside_E Lopinavir VTRRT Wogonin Wogonoside) do (
		for %s in (Site1 Site2 Site3d Site3m) do (
			for %w in (With_Water Without_Water) do (
				"%r/%l/%s/%w/output.pdbqt"
			)
		)
	)
)

## DO THIS cmd open pymol files, one rpt and one site at a time

for %r in (Rpt1) do (
	cd %r
	for %l in (Beta Bicalein Bicalin DAR_DIR Diammonium Forsythoside_E Lopinavir VTRRT Wogonin Wogonoside) do (
		cd %l
		for %s in (Site1) do (
			cd %s
			for %w in (With_Water Without_Water) do (
				cd %w
				"output.pdbqt"
				cd ..
			)
			cd ..
		)
		cd ..
	)
	cd ..
)

# When opened, type the following into pymol terminal:
# save output.pdb, state = 0


for %r in (Rpt1) do (
	cd %r
	for %l in (Beta Bicalein Bicalin DAR_DIR Diammonium Forsythoside_E Lopinavir VTRRT Wogonin Wogonoside) do (
		cd %l
		for %s in (Site2) do (
			cd %s
			for %w in (With_Water Without_Water) do (
				cd %w
				"output.pdbqt"
				cd ..
			)
			cd ..
		)
		cd ..
	)
	cd ..
)

# When opened, type save output.pdb into pymol terminal


for %r in (Rpt1) do (
	cd %r
	for %l in (Beta Bicalein Bicalin DAR_DIR Diammonium Forsythoside_E Lopinavir VTRRT Wogonin Wogonoside) do (
		cd %l
		for %s in (Site3d) do (
			cd %s
			for %w in (With_Water Without_Water) do (
				cd %w
				"output.pdbqt"
				cd ..
			)
			cd ..
		)
		cd ..
	)
	cd ..
)

# When opened, type save output.pdb into pymol terminal


for %r in (Rpt1) do (
	cd %r
	for %l in (Beta Bicalein Bicalin DAR_DIR Diammonium Forsythoside_E Lopinavir VTRRT Wogonin Wogonoside) do (
		cd %l
		for %s in (Site3m) do (
			cd %s
			for %w in (With_Water Without_Water) do (
				cd %w
				"output.pdbqt"
				cd ..
			)
			cd ..
		)
		cd ..
	)
	cd ..
)

# When opened, type save output.pdb into pymol terminal


for %r in (Rpt2) do (
	cd %r
	for %l in (Beta Bicalein Bicalin DAR_DIR Diammonium Forsythoside_E Lopinavir VTRRT Wogonin Wogonoside) do (
		cd %l
		for %s in (Site1) do (
			cd %s
			for %w in (With_Water Without_Water) do (
				cd %w
				"output.pdbqt"
				cd ..
			)
			cd ..
		)
		cd ..
	)
	cd ..
)

# When opened, type save output.pdb into pymol terminal


for %r in (Rpt2) do (
	cd %r
	for %l in (Beta Bicalein Bicalin DAR_DIR Diammonium Forsythoside_E Lopinavir VTRRT Wogonin Wogonoside) do (
		cd %l
		for %s in (Site2) do (
			cd %s
			for %w in (With_Water Without_Water) do (
				cd %w
				"output.pdbqt"
				cd ..
			)
			cd ..
		)
		cd ..
	)
	cd ..
)

# When opened, type save output.pdb into pymol terminal


for %r in (Rpt2) do (
	cd %r
	for %l in (Beta Bicalein Bicalin DAR_DIR Diammonium Forsythoside_E Lopinavir VTRRT Wogonin Wogonoside) do (
		cd %l
		for %s in (Site3d) do (
			cd %s
			for %w in (With_Water Without_Water) do (
				cd %w
				"output.pdbqt"
				cd ..
			)
			cd ..
		)
		cd ..
	)
	cd ..
)

# When opened, type save output.pdb into pymol terminal


for %r in (Rpt2) do (
	cd %r
	for %l in (Beta Bicalein Bicalin DAR_DIR Diammonium Forsythoside_E Lopinavir VTRRT Wogonin Wogonoside) do (
		cd %l
		for %s in (Site3m) do (
			cd %s
			for %w in (With_Water Without_Water) do (
				cd %w
				"output.pdbqt"
				cd ..
			)
			cd ..
		)
		cd ..
	)
	cd ..
)

# When opened, type save output.pdb into pymol terminal