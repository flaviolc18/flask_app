import dataset

db = dataset.connect('sqlite:///worktool.db')
ads_table = db['worktool']