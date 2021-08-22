from cresset import flare
import csv

project = flare.main_window().project
with open('/Users/Marta/Documents/university (Edinburgh)/year 3/project/docking_rdock/score.csv', 'w') as score_file:
    wr = csv.writer(score_file, dialect='excel')
    title_row = ['pose', 'score']
    wr.writerow(title_row)
    for l in project.ligands:
        name = l.title
        row = []
        row.append(name)
        row.append(l.properties['SCORE'])
        wr.writerow(row)
        print(".")

