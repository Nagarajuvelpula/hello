import streamlit as st
import requests
st.write("Hello World")

city = input("Enter Name : ")
key = '67ba64fcbd81ba6c52da7e77b6b1c14a'
url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=' + key

res = requests.get(url).json()

#print(res)


#print('coords :',res['coord'])



st.write('Country:',res['sys']['country'])
st.write('City:',res['name'])
st.write('Longtitude:',res['coord']['lon'])
st.write('Lotitude:',res['coord']['lat'])
st.write('Temperature:',res['main']['temp'],'C')
st.write('Min.Temp:',res['main']['temp'],'C')
st.write('Max.temp:',res['main']['temp'],'C')
st.write('Humidity:',res['main']['temp'])
st.write('Pressure:',res['main']['temp'])





