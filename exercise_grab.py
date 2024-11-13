import pandas as pd
df = pd.read_csv("exerlist2.csv")
def byName(name):
    df_withname = df.loc[df['Name'] == name]
    for i, r in df_withname.iterrows():
        print(f"name: {r["Name"]}\nPrimary Muscles: {r["primary"]}\nSecondary Muscles: {r["secondary"]}")
        #Can't display gifs yet so won't bother printing gif URL
def byMusc(muscle):
    df_muscle = df.loc[df['primary'].str.contains(muscle, na = False)]
    #I used this https://www.geeksforgeeks.org/select-rows-that-contain-specific-text-using-pandas/
    #and this https://stackoverflow.com/questions/66536221/getting-cannot-mask-with-non-boolean-array-containing-na-nan-values-but-the
    #when I was getting errors
    for i, r in df_muscle.iterrows():
        print(f"name: {r["Name"]}\nPrimary Muscles: {r["primary"]}\nSecondary Muscles: {r["secondary"]}")


