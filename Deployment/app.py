 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('bikeanalysis_3.pkl', 'rb')
classifier = pickle.load(pickle_in)
 
st.title('Team: Group 1')
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Year, Season, Weather, Month, Weekday,temp):
 
    # Pre-processing user input    
    if Year == "2018":
        yr = 0
    else:
        yr = 1

    if Season == "Spring":
        season_1 = 1
        season_4 = 0
    elif Season == "Summer":
        season_1 = 0
    elif Season == "Fall":
        season_1 = 0
    else:
        season_4 = 1

    if Weather == "Clear":
        weathersit_1 = 1
        weathersit_2 = 0
        weathersit_3 = 0
        weathersit_4 = 0
    elif Weather == "Mist":
        weathersit_2 = 1
        weathersit_1 = 0
        weathersit_3 = 0
        weathersit_4 = 0
    elif Weather == "Light Snow":
        weathersit_3 = 1
        weathersit_1 = 0
        weathersit_2 = 0
        weathersit_4 = 0
    else:
        weathersit_4 = 1
        weathersit_1 = 0
        weathersit_2 = 0
        weathersit_3 = 0

    if Month == "Sep":
        mnth_9 = 1
    elif Month == "Nov":
        mnth_11 = 1
    elif Month == "Dec":
        mnth_12 = 1
    else:
        mnth_12 = 0
        mnth_9 = 0
        mnth_11 = 0

    if Weekday == "Tuesday":
        weekday_2 = 1
    else:
        weekday_2 = 0
 

# Transform
    from sklearn.preprocessing import PolynomialFeatures
    poly_reg = PolynomialFeatures(degree=2)
    X_poly2 = poly_reg.fit_transform([[yr, season_1,season_4,mnth_9,mnth_11,mnth_12,weekday_2,weathersit_1,weathersit_2,weathersit_3,temp]])
    # Making predictions
    prediction = classifier.predict(X_poly2)
    #prediction = classifier.predict([[yr, season_1, season_4, mnth_9, mnth_11, mnth_12, weekday_2, weathersit_1, weathersit_2, weathersit_3]])
    prediction = prediction * 100
    return prediction
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Bike Rental Analysis ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    yr = st.selectbox('Year',("2018","2019"))
    season = st.selectbox('Season',("Spring","Summer","Fall","Winter"))
    mnth = st.selectbox('Month', ("Jan", "Feb","Mar", "Apr","May", "June","July", "Aug","Sep", "Oct","Nov", "Dec"))
    weekday = st.selectbox('Weekday', ("Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"))
    weathersit = st.selectbox('Weather', ("Clear","Mist","Light Snow","Rainfall"))
    temp = st.number_input("temp")
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(yr,season,mnth,weekday,weathersit,temp)
        st.success('Bike Rental Prediction is {}'.format(result))
     
if __name__=='__main__': 
    main()
