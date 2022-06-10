
import pickle
from flask import Flask,render_template,request
from flask_cors import cross_origin



app=Flask(__name__)
model=pickle.load(open('ipl.pkl','rb'))

@app.route('/')
@cross_origin()
def ipl():
    return render_template('index.html')

@app.route('/redict_Score',methods=['POST','GET'])
@cross_origin()
def predict():
    if request.method=='POST':
        batting_team=request.form.get('batting-team')
        if(batting_team=='Royal Challengers Bangalore'):
             bat_team_Royal_Challengers_Bangalore=1
             bat_team_Kings_XI_Punjab=0
             bat_team_Delhi_Daredevils=0
             bat_team_Kolkata_Knight_Riders=0
             bat_team_Rajasthan_Royals=0
             bat_team_Mumbai_Indians=0
             bat_team_Chennai_Super_Kings=0
             bat_team_Sunrisers_Hyderabad=0
        elif(batting_team=='Kings XI Punjab'):
             bat_team_Royal_Challengers_Bangalore=0
             bat_team_Kings_XI_Punjab=1
             bat_team_Delhi_Daredevils=0
             bat_team_Kolkata_Knight_Riders=0
             bat_team_Rajasthan_Royals=0
             bat_team_Mumbai_Indians=0
             bat_team_Chennai_Super_Kings=0
             bat_team_Sunrisers_Hyderabad=0
        elif(batting_team=='Delhi Daredevils'):
             bat_team_Royal_Challengers_Bangalore=0
             bat_team_Kings_XI_Punjab=0
             bat_team_Delhi_Daredevils=1
             bat_team_Kolkata_Knight_Riders=0
             bat_team_Rajasthan_Royals=0
             bat_team_Mumbai_Indians=0
             bat_team_Chennai_Super_Kings=0
             bat_team_Sunrisers_Hyderabad=0
        elif(batting_team=='Kolkata Knight Riders'):
             bat_team_Royal_Challengers_Bangalore=0
             bat_team_Kings_XI_Punjab=0
             bat_team_Delhi_Daredevils=0
             bat_team_Kolkata_Knight_Riders=1
             bat_team_Rajasthan_Royals=0
             bat_team_Mumbai_Indians=0
             bat_team_Chennai_Super_Kings=0
             bat_team_Sunrisers_Hyderabad=0          
        elif(batting_team=='Rajasthan Royals'):
             bat_team_Royal_Challengers_Bangalore=0
             bat_team_Kings_XI_Punjab=0
             bat_team_Delhi_Daredevils=0
             bat_team_Kolkata_Knight_Riders=0
             bat_team_Rajasthan_Royals=1
             bat_team_Mumbai_Indians=0
             bat_team_Chennai_Super_Kings=0
             bat_team_Sunrisers_Hyderabad=0
        elif(batting_team=='Mumbai Indians'):
             bat_team_Royal_Challengers_Bangalore=0
             bat_team_Kings_XI_Punjab=0
             bat_team_Delhi_Daredevils=0
             bat_team_Kolkata_Knight_Riders=0
             bat_team_Rajasthan_Royals=0
             bat_team_Mumbai_Indians=1
             bat_team_Chennai_Super_Kings=0
             bat_team_Sunrisers_Hyderabad=0
        elif(batting_team=='Chennai Super Kings'):
             bat_team_Royal_Challengers_Bangalore=0
             bat_team_Kings_XI_Punjab=0
             bat_team_Delhi_Daredevils=0
             bat_team_Kolkata_Knight_Riders=0
             bat_team_Rajasthan_Royals=0
             bat_team_Mumbai_Indians=0
             bat_team_Chennai_Super_Kings=1
             bat_team_Sunrisers_Hyderabad=0
        elif(batting_team=='Sunrisers Hyderabad'):
             bat_team_Royal_Challengers_Bangalore=0
             bat_team_Kings_XI_Punjab=0
             bat_team_Delhi_Daredevils=0
             bat_team_Kolkata_Knight_Riders=0
             bat_team_Rajasthan_Royals=0
             bat_team_Mumbai_Indians=0
             bat_team_Chennai_Super_Kings=0
             bat_team_Sunrisers_Hyderabad=1


        bowling_team=request.form.get('bowling-team')
        if(bowling_team=='Royal Challengers Bangalore'):
             bowl_team_Royal_Challengers_Bangalore=1
             bowl_team_Kings_XI_Punjab=0
             bowl_team_Delhi_Daredevils=0
             bowl_team_Kolkata_Knight_Riders=0
             bowl_team_Rajasthan_Royals=0
             bowl_team_Mumbai_Indians=0
             bowl_team_Chennai_Super_Kings=0
             bowl_team_Sunrisers_Hyderabad=0
        elif(bowling_team=='Kings XI Punjab'):
            bowl_team_Royal_Challengers_Bangalore=0
            bowl_team_Kings_XI_Punjab=1
            bowl_team_Delhi_Daredevils=0
            bowl_team_Kolkata_Knight_Riders=0
            bowl_team_Rajasthan_Royals=0
            bowl_team_Mumbai_Indians=0
            bowl_team_Chennai_Super_Kings=0
            bowl_team_Sunrisers_Hyderabad=0
        elif(bowling_team=='Delhi Daredevils'):
             bowl_team_Royal_Challengers_Bangalore=0
             bowl_team_Kings_XI_Punjab=0
             bowl_team_Delhi_Daredevils=1
             bowl_team_Kolkata_Knight_Riders=0
             bowl_team_Rajasthan_Royals=0
             bowl_team_Mumbai_Indians=0
             bowl_team_Chennai_Super_Kings=0
             bowl_team_Sunrisers_Hyderabad=0
        elif(bowling_team=='Kolkata Knight Riders'):
             bowl_team_Royal_Challengers_Bangalore=0
             bowl_team_Kings_XI_Punjab=0
             bowl_team_Delhi_Daredevils=0
             bowl_team_Kolkata_Knight_Riders=1
             bowl_team_Rajasthan_Royals=0
             bowl_team_Mumbai_Indians=0
             bowl_team_Chennai_Super_Kings=0
             bowl_team_Sunrisers_Hyderabad=0          
        elif(bowling_team=='Rajasthan Royals'):
             bowl_team_Royal_Challengers_Bangalore=0
             bowl_team_Kings_XI_Punjab=0
             bowl_team_Delhi_Daredevils=0
             bowl_team_Kolkata_Knight_Riders=0
             bowl_team_Rajasthan_Royals=1
             bowl_team_Mumbai_Indians=0
             bowl_team_Chennai_Super_Kings=0
             bowl_team_Sunrisers_Hyderabad=0
        elif(bowling_team=='Mumbai Indians'):
             bowl_team_Royal_Challengers_Bangalore=0
             bowl_team_Kings_XI_Punjab=0
             bowl_team_Delhi_Daredevils=0
             bowl_team_Kolkata_Knight_Riders=0
             bowl_team_Rajasthan_Royals=0
             bowl_team_Mumbai_Indians=1
             bowl_team_Chennai_Super_Kings=0
             bowl_team_Sunrisers_Hyderabad=0
        elif(bowling_team=='Chennai Super Kings'):
             bowl_team_Royal_Challengers_Bangalore=0
             bowl_team_Kings_XI_Punjab=0
             bowl_team_Delhi_Daredevils=0
             bowl_team_Kolkata_Knight_Riders=0
             bowl_team_Rajasthan_Royals=0
             bowl_team_Mumbai_Indians=0
             bowl_team_Chennai_Super_Kings=1
             bowl_team_Sunrisers_Hyderabad=0
        elif(bowling_team=='Sunrisers Hyderabad'):
             bowl_team_Royal_Challengers_Bangalore=0
             bowl_team_Kings_XI_Punjab=0
             bowl_team_Delhi_Daredevils=0
             bowl_team_Kolkata_Knight_Riders=0
             bowl_team_Rajasthan_Royals=0
             bowl_team_Mumbai_Indians=0
             bowl_team_Chennai_Super_Kings=0
             bowl_team_Sunrisers_Hyderabad=1 

        overs=float(request.form['overs'])    
        runs=float(request.form['runs'])    
        wickets=float(request.form['wickets'])    
        runs_in_prev_5=float(request.form['runs_in_prev_5'])    
        wickets_in_prev_5=float(request.form['wickets_in_prev_5'])    
          
        prediction=model.predict([[
            runs,
            wickets,
            overs,
            runs_in_prev_5,
            wickets_in_prev_5,
            bat_team_Kings_XI_Punjab,
            bat_team_Delhi_Daredevils,
            bat_team_Kolkata_Knight_Riders,
            bat_team_Rajasthan_Royals,
            bat_team_Mumbai_Indians,
            bat_team_Chennai_Super_Kings,
            bat_team_Sunrisers_Hyderabad,
            bowl_team_Kings_XI_Punjab,
            bowl_team_Delhi_Daredevils,
            bowl_team_Kolkata_Knight_Riders,
            bowl_team_Rajasthan_Royals,
            bowl_team_Mumbai_Indians,
            bowl_team_Chennai_Super_Kings,
            bowl_team_Sunrisers_Hyderabad

            


        ]])
        output=round(prediction[0],2)

        return render_template('index.html',prediction_text="IPL score is {}".format(output))

    return render_template('index.html')
        


    
if __name__ == '__main__':
    app.run(debug=True)
    