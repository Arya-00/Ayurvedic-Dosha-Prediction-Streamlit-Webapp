import streamlit as st
from Doshas_prediction_page_1 import show_predict_page

show_predict_page()
# st.subheader("")
# st.subheader("Project Code")
# code = """
#     heavy = 0
#     medium = 0
#     thin = 0

#     dont_gain_weight_easily = 0
#     dont_lose_weight_easily = 0
#     gain_and_lose_weight_easily = 0

#     inconsistent_appetite = 0
#     appetite_steady_appetite = 0
#     strong_appetite_cant_skip_meal = 0 

#     light_restless_sleep = 0
#     heavy_sleep = 0 
#     moderate_good_sleep =0 

#     neither_or_both = 0
#     weather_prefer_cold = 0
#     weather_prefer_warmth = 0 

#     dry_frizzy_hair = 0
#     fine_thin_hairs = 0
#     thick_and_oily = 0

#     gets_irritated = 0
#     under_stress_is_anxious_and_worried = 0 
#     behaviour_withdrawn = 0

#     dry_and_rough_skin = 0
#     thick_and_oily = 0
#     warm_reddish_and_irritable = 0 

#     cold_hands_and_feet = 0 
#     body_normal = 0 
#     body_warm_body = 0

#     easy_going_and_adaptive = 0
#     workflow_lively_and_enthusiastic = 0 
#     workflow_purposeful_and_intense = 0

#     array_of_features = [thin, medium, heavy, dont_gain_weight_easily, gain_and_lose_weight_easily, dont_lose_weight_easily, inconsistent_appetite, strong_appetite_cant_skip_meal, appetite_steady_appetite, light_restless_sleep, moderate_good_sleep, heavy_sleep, weather_prefer_warmth, weather_prefer_cold, neither_or_both, dry_frizzy_hair, fine_thin_hairs,thick_and_oily, under_stress_is_anxious_and_worried, gets_irritated, behaviour_withdrawn, dry_and_rough_skin, warm_reddish_and_irritable, thick_and_oily, cold_hands_and_feet, body_warm_body, body_normal, workflow_lively_and_enthusiastic, workflow_purposeful_and_intense, easy_going_and_adaptive]
    
#     st.header('**Find your Dosha**:dna:')
#     st.subheader("Fill out your traits")
#     col1, col2, col3 = st.columns(3)
#     col1.subheader("**Weight**:man-lifting-weights:")
#     Body = col1.radio("**Weight**:man-lifting-weights:",["None", "Light Weight","Muscular", "Heavy Weight"],label_visibility="collapsed")

#     col1.subheader("**Weight Gain and Loss**:green_salad:")
#     Weight_Loss = col1.radio("**Weight Gain and Loss**:green_salad:", ["None", "Can't gain weight easily", "Can't loose weight easily", "gain or loose weight easily"],label_visibility="collapsed")

#     col1.subheader("**Appetite**:stuffed_flatbread:")
#     Appetite = col1.radio("**Appetite**:stuffed_flatbread:",["None", "Inconsistent appetite", "Steady appetite", "Strong appetite"],label_visibility="collapsed")
    
#     col2.subheader("**Sleeping Behavior**:sleeping:")
#     Sleeping_behaviour = col2.radio("**Sleeping Behavior**:sleeping:", ["None", "Light Sleeper", "Heavy Sleeper", "Moderate Sleeper"],label_visibility="collapsed")
    
#     col2.subheader("**Favourite Season**:sunny::cloud:")
#     Favourite_Season = col2.radio("**Favourite Season**:sunny::cloud:", ["None", "Like all seasons", "Winter", "Summer"],label_visibility="collapsed")
    
#     col2.subheader("**Type of Hair**:curly_haired_man:")
#     Hair_Type = col2.radio("**Type of Hair**:curly_haired_man:", ["None", "Dry Frizzy Hair", "Fine Thin Hair", "Thick and Oily Hair"],label_visibility="collapsed")
    
#     col3.subheader("**Nature**:innocent:")
#     Nature = col3.radio("**Nature**:innocent:", ["None", "Irritated", "Anxious and Worried", "Withdrawn from Life"],label_visibility="collapsed")
    
#     col3.subheader("**Skin Type**:man:")
#     Skin = col3.radio("**Skin Type**:man:", ["None", "Dry and Rough", "Thick and Oily", "Reddish and Itchy"],label_visibility="collapsed")
    
#     col3.subheader("**Body Temperature**:male-doctor:")
#     Body_Temperature = col3.radio("**Body Temperature**:male-doctor:", ["None", "Cold", "Normal", "Warm"],label_visibility="collapsed")
    
#     col3.subheader("**Workflow**:man-juggling:")
#     Workflow = col3.radio("**Workflow**:man-juggling:", ["None", "Easy going and Adaptive", "Lively and Enthusiastic", "Purposeful and Intense"],label_visibility="collapsed")
    
    
#     if (Workflow or Body_Temperature or Skin or Nature or Hair_Type or Favourite_Season or Sleeping_behaviour or Appetite or Weight_Loss or Body):
#         if Body == "Light Weight": array_of_features[0] = 1
#         elif Body == "Muscular": array_of_features[1] = 1
#         elif Body == "Heavy Weight": array_of_features[2] = 1
        
#         if Weight_Loss == "Can't gain weight easily": array_of_features[3] = 1
#         elif Weight_Loss == "gain or loose weight easily": array_of_features[4] = 1
#         elif Weight_Loss == "Can't loose weight easily": array_of_features[5] = 1
        
#         if Appetite == "Inconsistent appetite": array_of_features[6] = 1
#         elif Appetite == "Steady appetite": array_of_features[7] = 1
#         elif Appetite == "Strong appetite": array_of_features[8] = 1

#         if Sleeping_behaviour == "Light Sleeper": array_of_features[9] = 1
#         elif Sleeping_behaviour == "Moderate Sleeper": array_of_features[10] = 1
#         elif Sleeping_behaviour ==  "Heavy Sleeper": array_of_features[11] = 1
        
#         if Favourite_Season == "Summer": array_of_features[12] = 1
#         elif Favourite_Season == "Winter": array_of_features[13] = 1
#         elif Favourite_Season == "Like all seasons": array_of_features[14] = 1

#         if Hair_Type == "Dry Frizzy Hair" : array_of_features[15] = 1
#         elif Hair_Type == "Fine Thin Hair": array_of_features[16] = 1
#         elif Hair_Type == "Thick and Oily Hair": array_of_features[17] = 1
        
#         if Nature == "Anxious and Worried": array_of_features[18] = 1
#         elif Nature == "Irritated": array_of_features[19] = 1
#         elif Nature == "Withdrawn from Life": array_of_features[20] = 1
        
#         if Skin == "Dry and Rough": array_of_features[21] = 1
#         elif Skin == "Reddish and Itchy": array_of_features[22] = 1
#         elif Skin == "Thick and Oily": array_of_features[23] = 1
        
#         if Body_Temperature == "Cold": array_of_features[24] = 1
#         elif Body_Temperature == "Warm": array_of_features[25] = 1
#         elif Body_Temperature == "Normal": array_of_features[26] = 1
        
#         if Workflow == "Lively and Enthusiastic": array_of_features[27] = 1
#         elif Workflow == "Easy going and Adaptive": array_of_features[29] = 1
#         elif Workflow == "Purposeful and Intense" : array_of_features[28] = 1
        
#         print(array_of_features)
#         if (array_of_features != [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]):
#             array_of_features = pd.DataFrame([array_of_features])
#             a = np.round(vat_model.predict(array_of_features), 2)
#             b = np.round(pit_model.predict(array_of_features), 2)
#             c = np.round(kp_model.predict(array_of_features), 2)
            
#             a_percent = a[0][1]/(a[0][1] + b[0][1] + c[0][1])
#             b_percent = b[0][1]/(a[0][1] + b[0][1] + c[0][1])
#             c_percent = c[0][1]/(a[0][1] + b[0][1] + c[0][1])
#         else:
#             a_percent = 0.05
#             b_percent = 0.05
#             c_percent = 0.05"""
# st.code(code, language="python")