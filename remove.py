# all imports
import os, shutil, re

# get input parameters, i.e. filepath participants & dirpath assignments
teilnehmerliste = 'teilnehmer.txt'
abgabenordner   = 'Abgaben'

# get list of all lab participants
with open(teilnehmerliste) as tnl:
    teilnehmer = tnl.read().splitlines()

# get list of all assignments (directories) & ignore hidden folders (MacOS)
abgaben = [x for x in os.listdir(abgabenordner) if not re.match(r"\..*", x)]

# if the assigment's name doesn't match any participant's name, delete it
for abgabe in abgaben:
    if not any([re.search(tn, abgabe) for tn in teilnehmer]):
        shutil.rmtree(abgabenordner + '/' + abgabe)
    
