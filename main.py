import streamlit as st
import pandas as pd
# pip install plotly
import plotly.express as px
import joblib


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


column_1, column_2 = st.columns([2, 1], gap="large")
column_1.header(" :rainbow[Gala Groceries Project: Estimation of product stock for a market]")



col1, col2, col3, col4, col5  = column_2.columns(5)

with col1:
   st.link_button("Miuul", "https://www.miuul.com/")

with col2:
  st.link_button("euroTech", "https://www.eurotechstudy.com/public/de")

with col3:
   st.metric(":thermometer: Temp", "-2 °C", "1.2 °C")

with col4:
   st.metric(":wind_blowing_face: Wind", "9 mph", "-8%")

with col5:
   st.metric(":droplet: Humidity", "86%", "4%")



tab_home, tab_data, tab_vis, tab_model, tab_about = st.tabs(["🏠 Homepage", "📂 Datasets", "📈 Charts", "🤖 Model", "📄 About"])

# Tab home
# column_bir, column_iki = st.columns(2)
# column_bir, column_iki = st.columns([1, 2])
column_bir, column_iki = tab_home.columns(2, gap="large")

column_bir.subheader("Inventory management at Gala supermarkets", divider="rainbow")
column_bir.markdown("Gala Supermarkets, as a technology-driven grocery store chain, embraces a strategy of continuous\n"
                    "evolution and a commitment to innovation. Leyla Hanım, serving as the branch manager of Gala\n"
                    "Supermarket in Germany, stands out as a dedicated leader with a focus on consistently providing\n"
                    "customers with the highest quality and freshest products.") 

column_bir.markdown("Encountering a project-oriented approach, supported by data science and machine learning, has\n"
                    "captured our interest. Leyla Hanım's notable willingness to devise innovative solutions for\n"
                    "challenges in the supply chain has left a lasting impression. Throughout this project, our focus\n"
                    "has been on analyzing pertinent datasets, including sales data, sensor-derived inventory information,\n"
                    "and temperature values within storage areas. This effort is directed towards achieving the objective\n"
                    "of optimizing product storage.")

column_bir.subheader("Project goal", divider="rainbow")
column_bir.markdown("The goal of our project is to enable efficient sourcing from our suppliers by analyzing hourly sales data\n"
                    "and sensor signals. This ensures that products are maintained at an optimal level in our inventory.")

column_bir.subheader("Dataset and Analysis Process", divider="rainbow")
column_bir.markdown("To attain this objective, we amalgamated three distinct datasets encompassing details on cash transactions,\n"
                    "product inventories, and temperature values measured by sensors. During the data preparation and cleaning phase,\n"
                    "we rectified anomalies, ensuring the data was meticulously primed for analysis.")

column_bir.subheader("Development and Testing of the Model", divider="rainbow")
column_bir.markdown("An essential phase of the project entailed crafting data science models to evaluate the connection between identified")
                    


column_iki.markdown("factors and inventory management. This involved creating regression models through outlier analysis, standardization,\n"
                    "and utilization of the Scikit-learn library. Robust algorithms such as BayesianRidge were employed for optimal model selection."
                    "The project significantly enhances the efficiency of Gala Supermarkets' supply chain processes under the guidance of Leyla Hanım.\n"
                    "This ensures the team is well-prepared for forthcoming challenges.")

column_iki.markdown("<br><br>", unsafe_allow_html=True)


column_iki.image("WhatsApp Bild 2024-01-11 um 12.14.47_dd58d66a.jpg", width=820)
column_iki.markdown("https://galasupermarkets.com/")



# Tab Data
column1_bir, column1_iki = tab_data.columns(2, gap="large")
column1_bir.subheader("Columns", divider="rainbow")
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


column1_bir.subheader("Sample_Sales_Data", divider="rainbow")
column1_bir.dataframe(sales, width=900)

column1_iki.subheader("Sensor_Stock_Levels", divider="rainbow")
column1_iki.dataframe(stock, width=900)

column1_iki.subheader("Sensor_Storage_Temperature", divider="rainbow")
column1_iki.dataframe(temp, width=900)



# Tab Vis

tab_vis.subheader("Chart 1", divider="rainbow")

fig = px.bar(count_df, x="category", y="count", color="category",
             labels={"count": "Count"},
             title="Categorical Sales Count",
             text="count",
             width=1000, height=600,
             color_discrete_sequence=px.colors.qualitative.Set3)

fig.update_layout(xaxis_title="Category", yaxis_title="Count", legend_title="Category")

tab_vis.plotly_chart(fig)


tab_vis.subheader("Chart 2", divider="rainbow")

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


#tab_vis.subheader("Chart 3", divider="rainbow")

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


tab_vis.subheader("Chart 3", divider="rainbow")

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



tab_vis.subheader("Chart 4", divider="rainbow")


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


tab_vis.subheader("Chart 5", divider="rainbow")

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


tab_vis.subheader("Chart 6", divider="rainbow")

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


#tab_vis.subheader("Chart 8", divider="rainbow")

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



#tab_vis.subheader("Chart 9", divider="rainbow")

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


tab_vis.subheader("Chart 7", divider="rainbow")
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



tab_vis.subheader("Chart 8", divider="rainbow")

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

tab_about.subheader(" :rainbow[HAKKIMIZDA]")
tab_about.markdown("euroTech Study & Miuul Data Science and Machine Learning Bootcamp katılımcıları olarak, veri bilimi\n"
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


co1, co2, co3, co4, co5  = tab_about.columns(5)

with co1:
   st.image("Betül Karagöz.jpg", "Betül Karagöz", width=130)
   st.link_button("Linkedin", "https://www.linkedin.com/in/betül-karagöz/")

with co2:
  st.image("Bilal Özdemir.jpg", "Bilal Özdemir", width=150)
  st.link_button("Linkedin", "https://www.linkedin.com/in/bilal-%C3%B6zdemir-0a5b58287?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")

with co3:
   st.image("Cemil Öksüz.jpg", "Cemil Öksüz", width=120)
   st.link_button("Linkedin", "https://www.linkedin.com/in/cemil-oksuz/")

with co4:
   st.image("Ercan Tayfun.jpg", "Ercan Tayfun", width=150)
   st.link_button("Linkedin", "https://www.linkedin.com/in/e-tayfun/")

with co5:
   st.image("Naime Diler.jpg", "Naime Diler", width=150)
   st.link_button("Linkedin", "https://www.linkedin.com/in/naime-diler/")
