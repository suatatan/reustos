# %% 
import pandas as pd
df = pd.read_excel(r"C:\Users\suat.atan\Downloads\walmart_page_list.xlsx")
# %%
def get_product_id_from_walmart_link(url):
    parts = url.split('/')
    last_part = parts[-1]
    return last_part
