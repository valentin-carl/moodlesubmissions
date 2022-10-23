# constants
tndir = 'Teilnehmer'
abdir = 'Abgaben'

# lists of participants, labs, and submissions
tnl = [f for f in os.listdir(teilnehmerdir)]
labs = [x.split('.')[0] for x in tnl]
abgaben = [x for x in os.listdir(abdir) if not re.match(r"\..*", x)]

# list of lists with participants for each lab
tns = []
for l in tnl:
    with open(f'{tndir}/{l}') as lab_participants:
        tns.append(lab_participants.read().splitlines())

# create new dir for current lab
lab_dirs = [d for d in os.listdir() if os.path.isdir(d) and re.fullmatch(r'lab_[0-9]+', d)]
current_lab = f'lab_{len(lab_dirs)+1}'
os.mkdir(current_lab)

# create subdirs for each lab session this week
for lab in labs:
    os.mkdir(f'{current_lab}/{lab}')

# sort each submission into respective lab subdir, delete remaining
for abgabe in abgaben:
    for i in range(len(tns)):
        if any([re.search(tn, abgabe) for tn in tns[i]]):
            shutil.move(f'{abdir}/{abgabe}', f'{current_lab}/{labs[i]}/{abgabe.split("_")[0]}')
            continue
    if os.path.isdir(f'{abdir}/{abgabe}'):
        shutil.rmtree(f'{abdir}/{abgabe}')

