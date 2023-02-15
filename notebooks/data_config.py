# set name of most up-to-date data file for notebooks to access
current_sample_sf = "../data/010sample_20230130.pkl"

label_names = {
    0:'COVID-19',
    1:'MSM', 
    2:'Exasperation',
    3:'Case Reports', 
    4:'Cynicism',  
    5:'Vaccination', 
    6:'WHO',
}

# set up common label color map for all notebooks to access
color_map_l = {
    'Exasperation': '#636EFA',
    'Cynicism': '#EF553B',
    'Case Reports': '#00CC96',
    'MSM': '#AB63FA',
    'WHO': '#FFA15A',
    'Vaccination': '#19D3F3',
    'COVID-19': '#FF6692'
}

color_map_lv = {
    'Exasperation True': '#636EFA',
    'Exasperation False': '#66bde5',
    'Cynicism True': '#d42e11',
    'Cynicism False': '#f2715a',
    'Case Reports True': '#00b383',
    'Case Reports False': '#33ffc9',
    'MSM True': '#9639f9',
    'MSM False': '#ca9cfc',
    'WHO True': '#ff6f00',
    'WHO False': '#ffa866',
    'Vaccination Campaigns True': '#0bbbda',
    'Vaccination Campaigns False': '#6ee3f7',
    'COVID-19 True': '#ff336d',
    'COVID-19 False': '#ff80a4'
}

gray = '#BAB0AC'

# # integer color map
# color_map = {
#     0: '#636EFA', 
#     1: '#EF553B', 
#     2: '#00CC96', 
#     3: '#AB63FA', 
#     4: '#FFA15A', 
#     5: '#19D3F3', 
#     6: '#FF6692'
# }