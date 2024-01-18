import streamlit as st
import pandas as pd
# pip install plotly
import plotly.express as px
import joblib
import webbrowser


st.set_page_config(layout="wide")

@st.cache_data
def get_data():
    df = pd.read_csv("sample_sales_data.csv") 
    return df

@st.cache_data
def get_data1():
    df_stock = pd.read_csv("sensor_stock_levels.csv")
    return df_stock


@st.cache_data
def get_data2():
    df_temp = pd.read_csv("sensor_storage_temperature.csv")
    return df_temp


column_1, column_2 = st.columns([6, 1], gap="large")
column_1.header(" :green[Gala Groceries Project: Estimation of product stock for a market]")


miuul_url = "https://www.miuul.com/"
eurotech_url = "https://www.eurotech-gmbh.eu/"


# Versuch1:
#import webbrowser

#def open_website(url):
#    webbrowser.open_new_tab(url)

#col1, col2 = column_2.columns(2)

#if col1.button("Miuul"):
#    open_website(miuul_url)

#if col2.button("euroTech GmbH"):
 #   open_website(eurotech_url)



# Versuch2:
#def open_website(url):
#    column_2.markdown(f'<a href="{url}" target="_blank"><button>{url}</button></a>', unsafe_allow_html=True)


#col1, col2 = column_2.columns(2)

#if col1.button("Miuul"):
 #   open_website(miuul_url)

#if col2.button("euroTech GmbH"):
 #   open_website(eurotech_url)




# Versuch3:

#def create_link_button(label, url):
 #   return f'<a href="{url}" target="_blank">{label}</a>'

#col1, col2 = column_2.columns(2)

#col1.markdown(create_link_button("Miuul", miuul_url), unsafe_allow_html=True)
#col2.markdown(create_link_button("euroTech GmbH", eurotech_url), unsafe_allow_html=True)


#Versuch 4:

# JavaScript zum Umleiten
redirect_script = """
<script>
function redirectTo(url) {
    window.open(url, '_blank');
}
</script>
"""

def create_link_button(label, url):
    return f'<button onclick="redirectTo(\'{url}\')">{label}</button>'


col1, col2 = column_2.columns(2)

col1.markdown(redirect_script, unsafe_allow_html=True)
col1.markdown(create_link_button("Miuul", miuul_url), unsafe_allow_html=True)

col2.markdown(redirect_script, unsafe_allow_html=True)
col2.markdown(create_link_button("euroTech GmbH", eurotech_url), unsafe_allow_html=True)









tab_home, tab_data, tab_vis, tab_model, tab_about = st.tabs(["Homepage", "Datasets", "Charts", "Model", "About"])

# Tab home
# column_bir, column_iki = st.columns(2)
# column_bir, column_iki = st.columns([1, 2])
column_bir, column_iki = tab_home.columns(2, gap="large")

column_bir.subheader("Gala Süpermarketleri'nde Stok Yönetimi")
column_bir.markdown("Gala Süpermarketleri olarak, teknoloji odaklı bir market zinciri olarak sürekli gelişen ve\n"
                    "yeniliklere açık bir yaklaşım benimsemekteyiz. Leyla Hanım, Almanya’daki Gala Süpermarketleri\n"
                    " mağazasının şube sorumlusu olarak, müşterilere en kaliteli ve taze ürünleri sunma çabası içinde\n"
                    "olan bir liderdir.")
column_bir.markdown("Veri bilimi ve makine öğrenimiyle desteklenen bir projeyle karşılaştığımızda, Leyla Hanım'ın\n"
                    " tedarik zinciri sorunlarına çözüm üretme konusundaki isteği bizi heyecanlandırdı. Bu proje\n"
                    " kapsamında, satış verileri, sensörlerden gelen stok durumu verileri ve depolardaki sıcaklık\n"
                    " değerleri gibi önemli veri setlerini analiz ederek,\n ürün stoklamayı optimize etme hedefine\n "
                    "odaklandık.")

column_bir.subheader("Proje Hedefi")
column_bir.markdown("Tedarikçilerimizden daha akıllıca ürün tedarik edebilmek için saatlik satış verileri ve sensor\n"
                    "verilerine dayanarak ürünlerin en optimum seviyede stoklanmasını sağlamak.")

column_bir.subheader("Veri Seti ve Analiz Süreci")
column_bir.markdown("Bu hedefe ulaşmak için, kasalardaki satış bilgileri, ürün stok miktarı ve sensörler tarafından\n"
                    "ölçülen sıcaklık değerlerini içeren üç ayrı veri setini entegre ettik. Veri hazırlığı ve temizleme\n"
                    "aşamasında, anormallikleri düzelttik ve analize uygun hale getirdik.")

column_bir.subheader("Model Geliştirme ve Test Etme")
column_bir.markdown("Projenin kritik aşamalarından biri, belirlenen faktörlerle stok yönetimi arasındaki ilişkiyi\n"
                    "değerlendirmek için veri bilimi modelleri geliştirmekti. Aykırı değer analizi, standartlaştırma\n"
                    "ve Scikit-learn kütüphanesi kullanılarak regresyon modelleri oluşturduk. En iyi uyan modelleri\n"
                    "belirlemek için Light GBM gibi güçlü algoritmaları kullandık.")


column_iki.markdown("Bu proje, Gala Süpermarketleri'nin tedarik zinciri süreçlerini daha etkili ve verimli bir şekilde\n"
                    "yönetmesine yardımcı olacak. Leyla Hanım'ın liderliğindeki ekip, gelecekteki benzer zorluklara\n"
                    "karşı daha iyi hazırlıklı olacak.")

column_iki.markdown("<br><br>", unsafe_allow_html=True)


column_iki.image("WhatsApp Bild 2024-01-11 um 12.14.47_dd58d66a.jpg", width=820)
column_iki.markdown("https://galasupermarkets.com/")



# Tab Data
column1_bir, column1_iki = tab_data.columns(2, gap="large")
column1_bir.subheader("Columns")
column1_bir.markdown("* transaction_id = this is a unique ID that is assigned to each transaction\n * timestamp = this is the datetime at which the transaction was made\n * product_id = this is an ID that is assigned to the product that was sold. Each product has a unique ID\n * category = this is the category that the product is contained within\n * customer_type = this is the type of customer that made the transaction\n * unit_price = the price that 1 unit of this item sells for\n * quantity = the number of units sold for this product within this transaction\n * total = the total amount payable by the customer\n * payment_type = the payment method used by the customer\n * temperature = time base tempreture informationce from sensors\n * estimated_stock_pct = shows product stock as a percentage, signaling availability or sales using data from sources such as sales and sensors")


df = get_data()
df_stock = get_data1()
df_temp = get_data2()



# for chart 1:
count_df = df.category.value_counts().reset_index()
count_df.columns = ["category", "count"]



def loading_data ():
  sales = df.copy()
  stock = df_stock.copy()
  temp = df_temp.copy()

  return sales , stock, temp

sales, stock, temp =loading_data()

for df in [sales, stock, temp]:

  df.drop("Unnamed: 0", axis=1, inplace=True)
  df["timestamp"] = pd.to_datetime(df["timestamp"], format='%Y-%m-%d %H:%M:%S').dt.floor("H")

  df['month'] = df['timestamp'].dt.month
  df['day'] = df['timestamp'].dt.day
  df['hour'] = df['timestamp'].dt.hour


column1_bir.subheader("Sample_Sales_Data")
column1_bir.dataframe(sales, width=900)

column1_iki.subheader("Sensor_Stock_Levels")
column1_iki.dataframe(stock, width=900)

column1_iki.subheader("Sensor_Storage_Temperature")
column1_iki.dataframe(temp, width=900)



# Tab Vis

tab_vis.subheader("Chart 1")

fig = px.bar(count_df, x="category", y="count", color="category",
             labels={"count": "Count"},
             title="Categorical Sales Count",
             text="count",
             width=1000, height=600,
             color_discrete_sequence=px.colors.qualitative.Set3)

fig.update_layout(xaxis_title="Category", yaxis_title="Count", legend_title="Category")

tab_vis.plotly_chart(fig)


tab_vis.subheader("Chart 2")

sales_hour = sales[["hour", "quantity"]]
sales_hour_df = sales_hour.groupby("hour")["quantity"].sum().reset_index()

fig = px.bar(sales_hour_df, x="hour", y="quantity", color="hour",
             labels={"quantity": "Quantity"},
             title="Hourly Sales Quantity",
             text="quantity",
             width=800, height=600,
             color_discrete_sequence=px.colors.qualitative.Set3)

fig.update_layout(xaxis_title="Hour", yaxis_title="Quantity", legend_title="Hour")

tab_vis.plotly_chart(fig)


#tab_vis.subheader("Chart 3")

#sales_hour = sales[["hour", "quantity", "category"]]
#sales_hour_df = sales_hour.groupby(["hour", "category"])["quantity"].sum().reset_index()


#fig = px.line(sales_hour_df, x="hour", y="quantity", color="category",
 #            labels={"quantity": "Quantity"},
  #           title="Hourly Sales Quantity by Category",
   #          text="quantity",
    #         width=1800, height=600,
     #        color_discrete_sequence=px.colors.qualitative.Set3)

#fig.update_layout(xaxis_title="Hour", yaxis_title="Quantity", legend_title="Category")

#tab_vis.plotly_chart(fig)


tab_vis.subheader("Chart 3")

sales_hour = sales[["hour", "quantity", "category"]]
sales_hour_df = sales_hour.groupby(["hour", "category"])["quantity"].sum().reset_index()


fig = px.bar(sales_hour_df, x="hour", y="quantity", color="category",
             labels={"quantity": "Quantity"},
             title="Hourly Sales Quantity by Category",
             text="quantity",
             width=1800, height=600,
             color_discrete_sequence=px.colors.qualitative.Set3)

fig.update_layout(xaxis_title="Hour", yaxis_title="Quantity", legend_title="Category")

tab_vis.plotly_chart(fig)



tab_vis.subheader("Chart 4")


sales_total = sales[["hour", "total"]]
sales_total_df = sales_total.groupby("hour")["total"].sum().reset_index()

fig = px.bar(sales_total_df, x="hour", y="total", color="hour",
             labels={"total": "Total"},
             title="Hourly Sales Total",
             text="total",
             width=800, height=600,
             color_discrete_sequence=px.colors.qualitative.Set3)

fig.update_layout(xaxis_title="Hour", yaxis_title="total", legend_title="Hour")

tab_vis.plotly_chart(fig)


tab_vis.subheader("Chart 5")

cat_total_df =  sales.groupby("category")["total"].sum().reset_index()
cat_total_df.columns = ["category", "total"]

fig = px.bar(cat_total_df, x="category", y="total", color="category",
             labels={"total": "Total"},
             title="Categorical Sales Total",
             text="total",
             width=800, height=600,
             color_discrete_sequence=px.colors.qualitative.Set3)

fig.update_layout(xaxis_title="Category", yaxis_title="Total", legend_title="Category")

tab_vis.plotly_chart(fig)


tab_vis.subheader("Chart 6")

sls = sales[["product_id", "category"]]
stck = stock.merge(sls, on="product_id", how="left")
stck = stck.drop_duplicates()
stck = stck.drop("id", axis=1)


# Hourly Stock estimated_stock_pct by Category

stock_hour = stck[["hour", "estimated_stock_pct", "category"]]
stock_hour_df = stock_hour.groupby(["hour", "category"])["estimated_stock_pct"].mean().reset_index()

fig = px.bar(stock_hour_df, x="hour", y="estimated_stock_pct", color="category",
             labels={"estimated_stock_pct": "estimated_stock_pct"},
             title="Hourly Stock estimated_stock_pct by Category",
             text="estimated_stock_pct",
             width=1000, height=600,
             color_discrete_sequence=px.colors.qualitative.Set3)
fig.update_traces(texttemplate='%{text:.3f}', textposition='inside')
fig.update_layout(xaxis_title="Hour", yaxis_title="Estimated_stock_pct", legend_title="Category")

tab_vis.plotly_chart(fig)


#tab_vis.subheader("Chart 8")

# Hourly Stock Estimated Stock Percentage by Category

#stock_hour = stck[["hour", "estimated_stock_pct", "category"]]
#stock_hour_df = stock_hour.groupby(["hour", "category"])["estimated_stock_pct"].mean().reset_index()


#fig = px.line(stock_hour_df, x="hour", y="estimated_stock_pct", color="category",
 #             labels={"estimated_stock_pct": "Estimated Stock Percentage"},
 #             title="Hourly Stock Estimated Stock Percentage by Category",
  #            width=1800, height=600,
  #            color_discrete_sequence=px.colors.qualitative.Set2)


#fig.update_layout(
 #   xaxis_title="Hour",
 #   yaxis_title="Estimated Stock Percentage",
 #   legend_title="Category",
#)

# tab_vis.plotly_chart(fig)



#tab_vis.subheader("Chart 9")

# Hourly Stock Estimated Stock Percentage

#stock_hour2 = stck[["hour", "estimated_stock_pct"]]
#stock_hour2_df = stock_hour2.groupby(["hour"])["estimated_stock_pct"].mean().reset_index()


#fig = px.bar(stock_hour2_df, x="hour", y="estimated_stock_pct",
      #         title="Hourly Stock Estimated Stock Percentage ",
       #       text ="estimated_stock_pct",
       #       width=1800, height=600,
        #      color_discrete_sequence=px.colors.qualitative.Set3)

#fig.update_traces(texttemplate='%{text:.3f}', textposition='inside')
#fig.update_layout(
   # xaxis_title="Hour",
   # yaxis_title="Estimated Stock Percentage")

#tab_vis.plotly_chart(fig)


tab_vis.subheader("Chart 7")
# Hourly Stock Estimated Stock Percentage

stock_hour2 = stck[["hour", "estimated_stock_pct"]]
stock_hour2_df = stock_hour2.groupby(["hour"])["estimated_stock_pct"].mean().reset_index()


fig = px.line(stock_hour2_df, x="hour", y="estimated_stock_pct",
              labels={"estimated_stock_pct": "Estimated Stock Percentage"},
              title="Hourly Stock Estimated Stock Percentage ",
              text ="estimated_stock_pct",
              width=1800, height=600,
              color_discrete_sequence=px.colors.qualitative.Set2)

fig.update_traces(texttemplate='%{text:.3f}')
fig.update_layout(
    xaxis_title="Hour",
    yaxis_title="Estimated Stock Percentage")

tab_vis.plotly_chart(fig)



tab_vis.subheader("Chart 8")

tmp = temp.drop("id", axis=1)

tmp['temp_category'] = pd.cut(x=temp['temperature'], bins=[-36, -16, 0, 15, 19, 36],labels=["A", "B", "C", "D", "E"])

# Categorical temperature
cat_temp = tmp.groupby(["temp_category", "hour"])["temperature"].mean().reset_index()

fig = px.line(cat_temp, x="hour", y="temperature", color="temp_category",
             labels={"temperature": "Temperature"},
             title="Categorical temperature",
             text="temperature",
             width=1000, height=600,
             color_discrete_sequence=px.colors.qualitative.Set3)
fig.update_traces(texttemplate='%{text:.3f}',) #textposition='inside')
fig.update_layout(xaxis_title="Category", yaxis_title="Temperature", legend_title="Category")

tab_vis.plotly_chart(fig)



# Tab Model
def get_model():
    model = joblib.load("final_model_bys.joblib")
    return model

model = get_model()

quantity_original = tab_model.number_input("Enter Quantity", min_value = 1, max_value = 4, step=1 ,value = 1)
temp_category = tab_model.number_input("Enter Category :  1: (-36°C to -16°C) # 2: (-16°C to 0°C) # 3: (0°C to 15°C) # 4: (15°C to 19°C) # 5: (19°C to 36°C)", min_value = 1, max_value = 5, step=1 ,value = 1)
temperature = tab_model.number_input("Enter Temperature : Attention: Enter the temperature suitable for the category you selected!", min_value = -36, max_value = 36, step=1 ,value = 0)
unit_price = tab_model.number_input("Enter Unit Price", min_value = 0.0, max_value = 24.0, step=0.01 ,value = 0.0)
day = tab_model.number_input("Enter Day: (0: Tuesday) # (1: Wednesday) # (2: Thursday) # (3: Friday) # (4: Saturday) # (5: Sunday) # (6: Monday)", min_value = 0, max_value = 6, step=1, value = 0)
hour = tab_model.number_input("Enter Hour", min_value = 9, max_value = 19, step=1 ,value = 9)
quantity_total = tab_model.number_input("Enter Weekly Total Quantity", min_value = 0, max_value = 288, step=1 ,value = 0)

user_input = pd.DataFrame({"quantity_original": quantity_original, "temperature": temperature, "temp_category": temp_category, "unit_price": unit_price, "day": day, "hour": hour, "quantity_total": quantity_total}, index=[0])

if tab_model.button("Predict!"):
    prediction = model.predict(user_input)
    tab_model.success(f"Estimated Stock Status : {prediction[0]}")
    tab_model.balloons()


# Tab About:

tab_about.subheader("HAKKIMIZDA")
tab_about.markdown("euroTech Study &Miuul Data Science and Machine Learning Bootcamp katılımcıları olarak, veri bilimi\n"
                   "ve makine öğrenimi dünyasına adım atmak amacıyla bir araya geldik. Eğitim süresince gerçek dünya\n"
                   "projeleri üzerinde çalışarak edindiğimiz bilgileri pekiştirdik. Bootcamp programının sonunda\n"
                   "sunduğumuz bu proje ile bu önemli süreci tamamlıyoruz. Kazandığımız bilgi ve deneyimle, geleceğin\n"
                   "veri bilimcileri olarak, bu alanda başarılı bir kariyere adım atmak için hazırız.")

tab_about.markdown("<br>", unsafe_allow_html=True)

tab_about.markdown("Bu seyahatte bizlere rehberlik eden ve destek sağlayan tüm eğitmenlere, mentörlere ve euroTech\n"
                   "Study & Miuul ailesine içten teşekkürlerimizi sunuyoruz. Veri bilimi ve makine öğrenimi tutkunları\n"
                   "olarak, elde ettiğimiz bu değerli bilgi ve becerileri, gelecekteki projelerde etkili bir şekilde\n"
                   "kullanmak için sabırsızlıkla bekliyoruz.")



tab_about.markdown("<br><br><br><br><br><br><br>", unsafe_allow_html=True)

def create_linked_profiles(profiles):
    columns = tab_about.columns(len(profiles))

    for column, (name, linkedin_url) in zip(columns, profiles):
        column.markdown(f'[**{name}**]({linkedin_url})')


profiles = [("Betül Karagöz", "https://www.linkedin.com/in/betül-karagöz/"),
            ("Bilal Özdemir", "https://www.linkedin.com/in/bilal-%C3%B6zdemir-0a5b58287?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"),
            ("Cemil Öksüz", "https://www.linkedin.com/in/cemil-oksuz/"),
            ("Ercan Tayfun", "https://www.linkedin.com/in/e-tayfun/"),
            ("Naime Diler", "https://www.linkedin.com/in/naime-diler/")]

create_linked_profiles(profiles)
