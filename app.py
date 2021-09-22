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


#extract the data from post request
st.title('Store Selection Model')
st.header('Site Location')
Typee = st.selectbox('Type of Area', ('Urban','Suburban and Rural'))
Box_size =st.number_input('Box Size(in sqft)')
Location_type = st.selectbox('Location Type', ('Residence','Local Market','Hospital & Clinic Hub','Transit','Other'))
#st.write('You selected', Location_type)
Store_location = st.selectbox('Store Location',('Main Market (Corner Property)','Middle of the Market','Developing Area','Off Market','Other'))
#st.write('You selected', Store_location)      
Storage = st.selectbox('Storage',('Ground Floor','Ground Floor + Loft','Ground + 1st floor','Ground + Basement','Other'))
#st.write('You selected', Storage)
Income_level = st.selectbox('Income Level', ('HIG','Higher MIG','MIG','Lower MIG','LIG'))
#st.write('You selected', Income_level)
st.write('\n')
st.header('Warehouse Proximity')
Warehouse_proximity = st.number_input('Warehouse Proximity(in km)')
st.write('\n')
st.header('Construction')
Shape = st.selectbox('Shape of the Store', ('Square shape with big facade','Rectangle Box with big facade','Rectangle with less facade','Zig zag box','Other'))
#st.write('You selected', Shape)
Beam_to_bottom = st.number_input('Beam to bottom(in ft)')
Facade = st.number_input('Facade(in ft)')
Staircase = st.selectbox('Staircase to Store', ('No Staircase','A Ramp space and 2 steps','2 to 4 steps','4 to 6 steps','More than 6 steps'))
#st.write('You selected', Staircase)
Parking = st.selectbox('Parking Availability', ('Car + Bike/scooter','Only Bike/scooter','Parking available at some point of time','Pay and park','No parking'))
#st.write('You selected', Parking)
Road_facing = st.selectbox('Road Facing', ('Main Road','Sub/Service Road','Small Lane','One way road','Other'))
#st.write('You selected', Road_facing)
Road_width = st.number_input('Road Width(in ft)')
Facade_blockage = st.selectbox('Facade Blockage', ('No Blockage','Partial Blockage','Complete Blockage'))
st.write('\n')
st.header('Business')
Payback_period = st.number_input('Payback Period')
Rent_to_sales = st.number_input('Rent % to Sales')
Break_even = st.number_input('Break Even Period')
st.write('\n')
st.header('Catchment Analysis')
Household = st.number_input('Household')
Brands = st.number_input('No. Of Brands (Within 1 km)')
Hospital = st.number_input('No. of Hospitals (within 1 km)')
Traffic = st.selectbox('Night time traffic 08:00 to 11:00 pm', ('Well lit with good people movement','Well lit with low people movement','Dimly lit with people movement','Dimly lit with no people movement','Low night traffic'))
Doctor_clinic = st.number_input('No. of Doctors & Clinics (Within 1 km)')
st.write('\n')
st.header('Competetion')
Total_retail_pharmacy = st.number_input('No. of Organized retail pharmacy & 24x7')
Distance_retail_pharmacy = st.number_input('Distance from Organized retail pharmacy(in metres)')
Total_medicals = st.number_input('Number of Local Medical shops')
Distance_medicals = st.number_input('Distance from Local Medical shops(in metres)')
Supermarket_distance = st.number_input('Supermarket Distance(in metres)')
Discounted_pharmacy = st.number_input('Discounted Pharmacy Distance(in metres)')

####
result=st.button('Calculate')
Total_score=500
  #BOX SIZE
if (result):
   
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
        Store_location_score=3
    elif Store_location=='Off Market':
        Store_location_score=2
    elif Store_location=='Other' :
        Store_location_score=1

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
        
    if Income_level=='HIG':
        Income_level_score=5
    elif Income_level=='Higher MIG':
        Income_level_score=4
    elif Income_level=='MIG':
        Income_level_score=3
    elif Income_level=='Lower MIG':
        Income_level_score=2
    elif Income_level=='LIG':
        Income_level_score=1


    if Warehouse_proximity<=50:
        Warehouse_proximity_score=5
    elif 50<Warehouse_proximity<=150:
        Warehouse_proximity_score=4
    elif 150<Warehouse_proximity<=250:
        Warehouse_proximity_score=3
    elif 250<Warehouse_proximity<=400:      
        Warehouse_proximity_score=2
    elif 400<Warehouse_proximity:
        Warehouse_proximity_score=1
    #SHAPE OF THE STORE
        

    if Shape=='Square shape with big facade':
        Shape_score=5
    elif Shape=='Rectangle Box with big facade':
        Shape_score=4
    elif Shape=='Rectangle with less facade':
        Shape_score=3
    elif Shape=='Zig zag box':
        Shape_score=2
    else:
        Shape_score=1
        
    #BEAM TO BOTTOM

        

    if Beam_to_bottom>=12:
        Beam_to_bottom_score=5
    elif Beam_to_bottom==11:
        Beam_to_bottom_score=4
    elif Beam_to_bottom==10:
        Beam_to_bottom_score=3
    elif Beam_to_bottom==9:
        Beam_to_bottom_score=2
    elif Beam_to_bottom<=8:
        Beam_to_bottom_score=1
         
    #FACADE

        

    if Facade>30:
        Facade_score=5
    elif 26<=Facade<=30:
        Facade_score=4
    elif 21<=Facade<=25:
        Facade_score=3
    elif 18<=Facade<=20:
        Facade_score=2
    elif Facade<18:
        Facade_score=1

    #Staircase to Store

        

    if Staircase=='No Staircase':
        Staircase_score=5
    elif Staircase=='A Ramp space and 2 steps':
        Staircase_score=4
    elif Staircase=='2 to 4 steps':
        Staircase_score=3
    elif Staircase=='4 to 6 steps':
        Staircase_score=2
    elif Staircase=='More than 6 steps':
        Staircase_score=1
    # PARKING AVAILABILITY

        

    if Parking=='Car + Bike/scooter':
        Parking_score=5
    elif Parking=='Only Bike/scooter':
        Parking_score=4
    elif Parking=='Parking available at some point of time':
        Parking_score=3
    elif Parking=='Pay and park':
        Parking_score=2
    elif Parking=='No parking':
        Parking_score=1
         
    #ROAD FACING

        

    if Road_facing=='Main Road':
        Road_facing_score=5
    elif Road_facing=='Sub/Service Road':
        Road_facing_score=4
    elif Road_facing=='Small Lane':
        Road_facing_score=3
    elif Road_facing=='One way road':
        Road_facing_score=2
    else:
        Road_facing_score=1
         
    #ROAD WIDTH
       

    if Road_width>50:
        Road_width_score=5
    elif 40<=Road_width<=50:
        Road_width_score=4
    elif 30<=Road_width<=39:
        Road_width_score=3
    elif 20<=Road_width<=29:
        Road_width_score=2
    elif Road_width<20:
        Road_width_score=1

    #FACADE BLOCKAGE

        

    if Facade_blockage=='No Blockage':
        Facade_blockage_score=5
    elif Facade_blockage=='Partial Blockage':
        Facade_blockage_score=4
    elif Facade_blockage=='Complete Blockage':
        Facade_blockage_score=3
          
    #Pay Back Period
        

    if Payback_period<24:
        Payback_period_score=5
    elif 24<=Payback_period<=27:
        Payback_period_score=4
    elif 28<=Payback_period<=31:
        Payback_period_score=3
    elif 32<=Payback_period<=36:
        Payback_period_score=2
    elif Payback_period>36:
        Payback_period_score=1
            
    #Rent % to Sales

        

    if Rent_to_sales<4:
        Rent_to_sales_score=5
    elif 4<=Rent_to_sales<6:
        Rent_to_sales_score=4
    elif 6<=Rent_to_sales<8:
        Rent_to_sales_score=3
    elif 8<=Rent_to_sales<=9:
        Rent_to_sales_score=2
    elif Rent_to_sales>9:
        Rent_to_sales_score=1
            
    #BREAK EVEN PERIOD

        

    if Break_even<4:
        Break_even_score=5
    elif 4<=Break_even<=6:
        Break_even_score=4
    elif 7<=Break_even<=8:
        Break_even_score=3
    elif 9<=Break_even<=10:
        Break_even_score=2
    elif Break_even>10:
        Break_even_score=1
    #Household
       

    if Household>10000:
        Household_score=5
    elif 8000<=Household<=10000:
        Household_score=4
    elif 5000<=Household<=7999:
        Household_score=3
    elif 3000<=Household<=4999:
        Household_score=2
    elif Household<3000:
        Household_score=1
            
    #No. Of Brands (Within 1 km)

        

    if Brands>10:
        Brands_score=5
    elif 7<=Brands<=10:
        Brands_score=4
    elif 5<=Brands<=6:
        Brands_score=3
    elif 3<=Brands<=4:
        Brands_score=2
    elif Brands<3:
        Brands_score=1
            
    #No. of Hospitals (within 1 km)

        

    if Hospital>6:
        Hospital_score=5
    elif 5<=Hospital<=6:
        Hospital_score=4
    elif 3<=Hospital<=4:
        Hospital_score=3
    elif 1<=Hospital<=2:
        Hospital_score=2
    elif Hospital<1:
        Hospital_score=1
            
    #Night time traffic 08:00 to 11:00 pm

        

    if Traffic=='Well lit with good people movement':
        Traffic_score=5
    elif Traffic=='Well lit with low people movement':
        Traffic_score=4
    elif Traffic=='Dimly lit with people movement':
        Traffic_score=3
    elif Traffic=='Dimly lit with no people movement':
        Traffic_score=2
    elif Traffic=='Low night traffic':
        Traffic_score=1
          
        #No. of Doctors & Clinics (Within 1 km)

        

    if Doctor_clinic>10:
        Doctor_clinic_score=5
    elif 7<=Doctor_clinic<=10:
        Doctor_clinic_score=4
    elif 5<=Doctor_clinic<=6:
        Doctor_clinic_score=3
    elif 3<=Doctor_clinic<=4:
        Doctor_clinic_score=2
    elif Doctor_clinic<3:
        Doctor_clinic_score=1
      


    if Typee=='Urban':
        
            
        if Total_retail_pharmacy==0 or Total_retail_pharmacy=='No Competetion':
            Total_retail_pharmacy_score=5
        elif 1<=Total_retail_pharmacy<=2:
            Total_retail_pharmacy_score=4
        elif 3<=Total_retail_pharmacy<4:
            Total_retail_pharmacy_score=3
        elif 4<=Total_retail_pharmacy<=5:
            Total_retail_pharmacy_score=2
        elif Total_retail_pharmacy>5:
            Total_retail_pharmacy_score=1
            
            
            
        if Distance_retail_pharmacy>500 or Distance_retail_pharmacy==0:
            Distance_retail_pharmacy_score=5
        elif 400<=Distance_retail_pharmacy<=500:
            Distance_retail_pharmacy_score=4
        elif 300<=Distance_retail_pharmacy<400:
            Distance_retail_pharmacy_score=3
        elif 200<=Distance_retail_pharmacy<300:
            Distance_retail_pharmacy_score=2
        elif 0<Distance_retail_pharmacy<200:
            Distance_retail_pharmacy_score=1
            
         
            
        if Total_medicals<3:
           Total_medicals_score=5
        elif 3<=Total_medicals<=4:
            Total_medicals_score=4
        elif 5<=Total_medicals<=7:
            Total_medicals_score=3
        elif 8<=Total_medicals<=9:
            Total_medicals_score=2
        elif Total_medicals>9:
            Total_medicals_score=1
          
            
            
        if Distance_medicals>500:
            Distance_medicals_score=5
        elif 401<=Distance_medicals<=500:
            Distance_medicals_score=4
        elif 301<=Distance_medicals<=400:
            Distance_medicals_score=3
        elif 201<=Distance_medicals<=300:
            Distance_medicals_score=2
        elif Distance_medicals<200:
            Distance_medicals_score=1
                
            
            
        if Supermarket_distance>500:
            Supermarket_distance_score=5
        elif 401<=Supermarket_distance<=500:
            Supermarket_distance_score=4
        elif 301<=Supermarket_distance<=400:
            Supermarket_distance_score=3
        elif 201<=Supermarket_distance<=300:
            Supermarket_distance_score=2
        elif Supermarket_distance<200:
            Supermarket_distance_score=1
              
                
            
            
        if Discounted_pharmacy>500:
            Discounted_pharmacy_score=5
        elif 401<=Discounted_pharmacy<=500:
            Discounted_pharmacy_score=4
        elif 301<=Discounted_pharmacy<=400:
            Discounted_pharmacy_score=3
        elif 201<=Discounted_pharmacy<=300:
            Discounted_pharmacy_score=2
        elif Discounted_pharmacy<200:
            Discounted_pharmacy_score=1
        ############################################################################################################        
    elif Typee=='Suburban and Rural':
            
            
        if Total_retail_pharmacy>5:
            Total_retail_pharmacy_score=5
        elif 4<=Total_retail_pharmacy<=5:
            Total_retail_pharmacy_score=4
        elif 3<=Total_retail_pharmacy<4:
            Total_retail_pharmacy_score=3
        elif 1<=Total_retail_pharmacy<=2:
            Total_retail_pharmacy_score=2
        elif Total_retail_pharmacy==0 or Total_retail_pharmacy=='No Competetion':
            Total_retail_pharmacy_score=1
             
            
            
        if 0<Distance_retail_pharmacy<200:
            Distance_retail_pharmacy_score=5
        elif 200<=Distance_retail_pharmacy<300:
            Distance_retail_pharmacy_score=4
        elif 300<=Distance_retail_pharmacy<400:
            Distance_retail_pharmacy_score=3
        elif 400<=Distance_retail_pharmacy<=500:
            Distance_retail_pharmacy_score=2
        elif Distance_retail_pharmacy>500 or Distance_retail_pharmacy==0:
            Distance_retail_pharmacy_score=1
              
            
            
        if Total_medicals>9:
            Total_medicals_score=5
        elif 8<=Total_medicals<=9:
            Total_medicals_score=4
        elif 5<=Total_medicals<=7:
            Total_medicals_score=3
        elif 3<=Total_medicals<=4:
            Total_medicals_score=2
        elif Total_medicals<3:
            Total_medicals_score=1
            
            
            
        if Distance_medicals<200:
            Distance_medicals_score=5
        elif 201<=Distance_medicals<=300:
            Distance_medicals_score=4
        elif 301<=Distance_medicals<=400:
            Distance_medicals_score=3
        elif 401<=Distance_medicals<=500:
            Distance_medicals_score=2
        elif Distance_medicals>500:
            Distance_medicals_score=1
                
            
            
        if Supermarket_distance<200:
            Supermarket_distance_score=5
        elif 201<=Supermarket_distance<=300:
            Supermarket_distance_score=4
        elif 301<=Supermarket_distance<=400:
            Supermarket_distance_score=3
        elif 401<=Supermarket_distance<=500:
            Supermarket_distance_score=2
        elif Supermarket_distance>500:
            Supermarket_distance_score=1
                
                
            
            
        if Discounted_pharmacy<200:
            Discounted_pharmacy_score=5
        elif 201<=Discounted_pharmacy<=300:
            Discounted_pharmacy_score=4
        elif 301<=Discounted_pharmacy<=400:
            Discounted_pharmacy_score=3
        elif 201<=Discounted_pharmacy<=300401<=Discounted_pharmacy<=500:
            Discounted_pharmacy_score=2
        elif Discounted_pharmacy>500:
            Discounted_pharmacy_score=1
            
            
                
            
    Site_Location_Total_Score=0.15*Total_score
    Box_size_score=(Box_size_score/5)*(0.25*Site_Location_Total_Score)
    Location_type_score=(Location_type_score/5)*(0.25*Site_Location_Total_Score)
    Store_location_score=(Store_location_score/5)*(0.15*Site_Location_Total_Score)
    Storage_score=(Storage_score/5)*(0.10*Site_Location_Total_Score)
    Income_level_score=(Income_level_score/5)*(0.25*Site_Location_Total_Score)
    Final_Site_Location_Score=Box_size_score+Location_type_score+Store_location_score+Storage_score+Income_level_score
    #st.write('Site Location Score',Final_Site_Location_Score,'/',Site_Location_Total_Score)
    st.header('Site Location Score')
    Final_Site_Location_Score=int(Final_Site_Location_Score)
    strr=str(Final_Site_Location_Score)+'/'+str(Site_Location_Total_Score)
    st.header(strr)

    Warehouse_proximity_Total_Score=0.05*Total_score
    Final_Warehouse_proximity_score=(Warehouse_proximity_score/5)*Warehouse_proximity_Total_Score
    #st.write('Warehouse Proximity Score',Final_Warehouse_proximity_score,'/',Warehouse_proximity_Total_Score)
    st.header('Warehouse Proximity Score')
    Final_Warehouse_proximity_score=int(Final_Warehouse_proximity_score)
    strr=str(Final_Warehouse_proximity_score)+'/'+str(Warehouse_proximity_Total_Score)
    st.header(strr)    

    Construction_Total_Score=0.1*Total_score
    Shape_score=(Shape_score/5)*(0.4*Construction_Total_Score)
    Beam_to_bottom_score=(Beam_to_bottom_score/5)*(0.3*Construction_Total_Score)
    Facade_score=(Facade_score/5)*(0.15*Construction_Total_Score)
    Staircase_score=(Staircase_score/5)*(0.15*Construction_Total_Score)
    Final_Construction_Score=Shape_score+Beam_to_bottom_score+Facade_score+Staircase_score
    #st.write('Construction Score',Final_Construction_Score,'/',Construction_Total_Score)     
    st.header('Construction Score')
    Final_Construction_Score=int(Final_Construction_Score)
    strr=str(Final_Construction_Score)+'/'+str(Construction_Total_Score)
    st.header(strr)

    Accessibility_Total_Score=0.05*Total_score
    Parking_score=(Parking_score/5)*(0.4*Accessibility_Total_Score)
    Road_facing_score=(Road_facing_score/5)*(0.3*Accessibility_Total_Score)
    Road_width_score=(Road_width_score/5)*(0.2*Accessibility_Total_Score)
    Facade_blockage_score=(Facade_blockage_score/5)*(0.1*Accessibility_Total_Score)
    Final_Accessibility_Score=Parking_score+Road_facing_score+Road_width_score+Facade_blockage_score
    #st.write('Accessibility Score',Final_Accessibility_Score,'/',Accessibility_Total_Score)
    st.header('Accessibility Score')
    Final_Accessibility_Score=int(Final_Accessibility_Score)
    strr=str(Final_Accessibility_Score)+'/'+str(Accessibility_Total_Score)
    st.header(strr)

    Business_Total_Score=0.25*Total_score
    Payback_period_score=(Payback_period_score/5)*(0.4*Business_Total_Score)
    Rent_to_sales_score=(Rent_to_sales_score/5)*(0.3*Business_Total_Score)
    Break_even_score=(Break_even_score/5)*(0.3*Business_Total_Score)
    Final_Business_Score=Payback_period_score+Rent_to_sales_score+Break_even_score
    #st.write('Business Score',Final_Business_Score,'/',Business_Total_Score)    
    st.header('Business Score')
    Final_Business_Score=int(Final_Business_Score)
    strr=str(Final_Business_Score)+'/'+str(Business_Total_Score)
    st.header(strr)


    Catchment_Total_Score=0.2*Total_score
    Household_score=(Household_score/5)*(0.4*Catchment_Total_Score)
    Brands_score=(Brands_score/5)*(0.2*Catchment_Total_Score)
    Hospital_score=(Hospital_score/5)*(0.2*Catchment_Total_Score)
    Traffic_score=(Traffic_score/5)*(0.05*Catchment_Total_Score)
    Doctor_clinic_score=(Doctor_clinic_score/5)*(0.15*Catchment_Total_Score)
    Final_Catchment_Score=Household_score+Brands_score+Hospital_score+Traffic_score+Doctor_clinic_score
    #st.write('Catchment Score',Final_Catchment_Score,'/',Catchment_Total_Score)
    st.header('Catchment Score')
    Final_Catchment_Score=int(Final_Catchment_Score)
    strr=str(Final_Catchment_Score)+'/'+str(Catchment_Total_Score)
    st.header(strr)
        


    Competition_Total_Score=0.2*Total_score
    Total_retail_pharmacy_score=(Total_retail_pharmacy_score/5)*(0.25*Competition_Total_Score)
    Distance_retail_pharmacy_score=(Distance_retail_pharmacy_score/5)*(0.05*Competition_Total_Score)
    Total_medicals_score=(Total_medicals_score/5)*(0.2*Competition_Total_Score)
    Distance_medicals_score=(Distance_medicals_score/5)*(0.05*Competition_Total_Score)
    Supermarket_distance_score=(Supermarket_distance_score/5)*(0.2*Competition_Total_Score)
    Discounted_pharmacy_score=(Discounted_pharmacy_score/5)*(0.25*Competition_Total_Score)
    Final_Competition_Score=Total_retail_pharmacy_score+Distance_retail_pharmacy_score+Total_medicals_score+Distance_medicals_score+Supermarket_distance_score+Discounted_pharmacy_score
    #st.write('Competition Score',Final_Competition_Score,'/',Competition_Total_Score)
    st.header('Competition Score')
    Final_Competition_Score=int(Final_Competition_Score)
    strr=str(Final_Competition_Score)+'/'+str(Competition_Total_Score)
    st.header(strr)

    Final_Score=Final_Site_Location_Score+Final_Warehouse_proximity_score+Final_Construction_Score+Final_Accessibility_Score+Final_Business_Score+Final_Catchment_Score+Final_Competition_Score

    st.header('Total Score')
    Final_Score=int(Final_Score)
    strr=str(Final_Score)+'/'+str(Total_score)
    st.header(strr)

    