import pandas as pd
etsy = pd.read_csv(r"C:\Users\holli\Downloads\EtsySoldOrderItems2021-4 newestest.csv")
etsy['color'] = etsy.Variations.str.split(',', expand=True)[0]
etsy['size'] = etsy.Variations.str.split(',', expand=True)[1]

etsy_sale_date = etsy[etsy['Date'].str.match('4/17/2021')]

from collections import Counter
etsy_size_color_date = etsy_sale_date.groupby('color')['size'].agg(Counter)
print(etsy_size_color_date)

