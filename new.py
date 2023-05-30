import streamlit as st
import requests
st.write("Hello World")

city = input("Enter Name : ")
key = '67ba64fcbd81ba6c52da7e77b6b1c14a'
url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=' + key

res = requests.get(url).json()

#print(res)


#print('coords :',res['coord'])



st.print('Country:',res['sys']['country'])
st.print('City:',res['name'])
st.print('Longtitude:',res['coord']['lon'])
st.print('Lotitude:',res['coord']['lat'])
st.print('Temperature:',res['main']['temp'],'C')
st.print('Min.Temp:',res['main']['temp'],'C')
st.print('Max.temp:',res['main']['temp'],'C')
st.print('Humidity:',res['main']['temp'])
st.print('Pressure:',res['main']['temp'])





