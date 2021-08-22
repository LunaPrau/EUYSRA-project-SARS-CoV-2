from cresset import flare

import csv



project = flare.main_window().project

with open('/Users/rosco/OneDrive/Documents/EUYSRA/rDock/rdockout_1.csv', 'w') as score_file:

    wr = csv.writer(score_file, dialect='excel')

    title_row = ['lig_name','SCORE']
    wr.writerow(title_row)

    for l in project.ligands:

        if l.title.endswith('.pdb'):

            name = l.title.strip('.pdb')

            row = []

            row.append(name)

            row.append(l.properties['SCORE'])


            wr.writerow(row)

print(".")


*DELETE ME*

To make the code work for you, you will have to:

1.copy over all of your .flr docking out files into flare, I've done a seperate file per repeat but I don't know if we need to [sorry, this takes a while but the rest should be quick, and it should make things easier with RMSD]
2.make a .csv file [a differnt one for each repeat if you do it the same way as me]
3.change *'/Users/rosco/OneDrive/Documents/EUYSRA/rDock/rdockout_1.csv'* to the file location of your .csv file 
4.ensure all your ligands are named correctly (e.g. Apigenin.pdb), as some of mine were just numbers and the code only works for ligands with same ending.
[if your ligands have a differnt ending to all their names just change it]
5.remove all the code already in the flare python interpreter 
6.Delete all these instructions and paste the rest into the python interpreter