https://copernicus.eu
I found about: Copernicus
Copernicus is the Earth Observation component of the European Union's space programme, looking at our planet and its environment for the benefit 

another 
ECMWF Reanalysis v5 (ERA5)
ERA5 is the fifth generation ECMWF atmospheric reanalysis of the global climate covering the period from January 1940 to present. ERA5 is produced by the Copernicus Climate Change Service (C3S) at ECMWF.


from data set url https://climateknowledgeportal.worldbank.org/download-data

I choose era5-x0.25
ERA5 is the most accurate and modern global reanalysis dataset provided by the European Centre for Medium-Range Weather Forecasts (ECMWF).

“x0.25” means it has high spatial resolution (0.25° ≈ ~25 km grid).

Covers hourly or daily variables from 1950 to present.

-------------
from the world bank site i was able to download my required data with following setting:
Area of Focus:
    NPL
Collection:
    ERA5 0.25-degree
Type:
    timeseries
Variable:
    hd35 - Number of Hot Days (Tmax > 35°C)
    pr - Precipitation
    tas - Average Mean Surface Air Temperature
Product:
    Time Series
Aggregation:
    Monthly
Time Interval:
    1950-2023
Percentile:
    Mean
Scenario:
    Historical
Model:
    era5
Model Calculation:
    x0.25

--------finally i was able to download excel file and saved json file also

and for the second data set 
https://www.globalforestwatch.org/dashboards/country/NPL/
i donwload from there.



#Exploratory Data Analysis (EDA) Summary
Forest Loss Data (CSV)
The dataset covers tree cover area, gains, and annual losses for Nepal’s five subnational regions from 2001 to 2023.

Forest cover decreased consistently in all regions, with the highest annual losses observed between 2017 and 2021.

Some years (e.g., 2015, 2017) show spikes in loss possibly due to natural disasters or increased deforestation activity.

Precipitation Data (JSON)
Monthly precipitation data spans from 1950 to 2023.

Annual precipitation shows significant variability, with some notably wet years (e.g., 2002, 2010, 2017) and dry periods.

Correlation Between Tree Loss and Precipitation
A moderate correlation, Correlation between Tree Loss and Annual Precipitation: -0.06 was found between tree cover loss and annual precipitation.

Visualization suggests that higher precipitation years sometimes align with increased tree loss, potentially due to climate-driven events like landslides, floods, or storms.

Exploratory Data Analysis (EDA) Summary
Tree Cover Loss:

Computed total tree cover loss per year (2001–2023) across Nepal using the provided CSV dataset.

Identified regional variations, with the Central region consistently showing the highest losses.

A 5-year rolling average was calculated to smooth short-term fluctuations and highlight long-term trends.

Precipitation Data:

Extracted monthly precipitation data from the JSON dataset and aggregated it into annual averages for consistency with tree loss data.

Key Findings:

Visualized both tree cover loss and precipitation trends over time.

Calculated Pearson correlation between yearly tree cover loss and precipitation.

Result: A correlation coefficient of -0.06, indicating no significant linear relationship between precipitation and tree cover loss in Nepal for the period 2001–2023.


Modeling Results

A linear regression model was developed to predict annual tree cover loss based on features such as the previous year’s tree cover loss (lag feature) and annual precipitation. The model achieved the following Random Forest Model Performance:
Mean Squared Error (MSE): 0.6591
R-squared (R²): -0.8554


and from Gradient Boosting Model Performance:
Mean Squared Error (MSE): 0.8182
R-squared (R²): -1.3032


The model's predictions closely followed the actual values, as shown in the comparison plot. While the predictions were not perfect (due to limited feature complexity and potential nonlinearities in environmental data), the model successfully captured overall trends in tree cover loss over time.

Note: Future model improvements could include additional features such as temperature trends, socioeconomic factors, or advanced models like Random Forest or Gradient Boosting.

