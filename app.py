#importing libraries
#import pandas as pd
#from flask import Flask, render_template, request
import pandas as pd
import streamlit as st
#declare the app
#app = Flask(__name__)

#start the app route which is '/'
#@app.route('/', methods=['GET'])
#declare the main function
#def main():
    
   # return render_template('index.html')
#app.run(debug=True)
#form submission route
#@app.route('/score',methods=['POST'])
if(True):

    #extract the data from post request
    Box_size =st.number_input('Box_size')
    Location_type = st.selectbox('select in the box given', ('Residence','Local Market','Hospital & Clinic Hub','Transit','Other'))
    st.write('you selected', Location_type)
    Store_location = st.selectbox('select in the box given',('Main Market (Corner Property)','Middle of the Market','Developing Area','Off Market','Other'))
    st.write('you selected', Store_location)      
    Storage = st.selectbox('select in the box given',('Ground Floor','Other'))
    st.write('Storage', Storage)
   
    
    ####
    Total_score=500
      #BOX SIZE
        
    if 1001<=Box_size<=1100 or 900<=Box_size<=1000 :
        Box_size_score=5
    elif 1101<=Box_size<=1200 or 800<=Box_size<=899 :
        Box_size_score=4
    elif 1201<=Box_size<=1300 or 700<=Box_size<=799 :
        Box_size_score=3
    elif 1301<=Box_size<=1400 or 500<=Box_size<=699 :
        Box_size_score=2
    elif 1400<=Box_size or Box_size<=500 :
        Box_size_score=1

    #LOCATION TYPE

        

    if Location_type=='Residence':
        Location_type_score=5
    elif Location_type=='Local Market':
        Location_type_score=4
    elif Location_type=='Hospital & Clinic Hub':
        Location_type_score=3
    elif Location_type=='Transit':
        Location_type_score=2
    else :
        Location_type_score=1
    


        

    if Store_location=='Main Market (Corner Property)':
        Store_location_score=5
    elif Store_location=='Middle of the Market':
        Store_location_score=4
    elif Store_location=='Developing Area':
        Store_location_score=4
    elif Store_location=='Off Market':
        Store_location_score=4
    else :
        Store_locatiton_score=1

    #STORAGE


    if Storage=='Ground Floor':
        Storage_score=5
    elif Storage=='Ground Floor + Loft':
        Storage_score=4
    elif Storage=='Ground + 1st floor':
        Storage_score=3
    elif Storage=='Ground + Basement':
        Storage_score=2
    else:
        Storage_score=1
         
    Site_Location_Total_Score=0.15*Total_score
    Box_size_score=(Box_size_score/5)*(0.25*Site_Location_Total_Score)
    Location_type_score=(Location_type_score/5)*(0.25*Site_Location_Total_Score)
    Store_location_score=(Store_location_score/5)*(0.15*Site_Location_Total_Score)
    Storage_score=(Storage_score/5)*(0.10*Site_Location_Total_Score)
    #Income_level_score=(Income_level_score/5)*(0.25*Site_Location_Total_Score)
    Final_Site_Location_Score=Box_size_score+Location_type_score+Store_location_score+Storage_score
    Final_Site_Location_Score

    Final_Score=Final_Site_Location_Score    

        