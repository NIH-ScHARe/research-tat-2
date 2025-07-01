import stl_reader as stl 

verticies,indices = stl.read('data/2016_survival_months.slm')

print(indices)

# data = pd.read_csv('data/2016_survival_months.slm')

# print(data.head(10))