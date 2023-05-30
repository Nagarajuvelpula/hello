import streamlit as st
import requests
st.write("Hello World")

city = input("Enter Name : ")
key = '67ba64fcbd81ba6c52da7e77b6b1c14a'
url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=' + key

res = requests.get(url).json()

#print(res)


#print('coords :',res['coord'])



print('Country:',res['sys']['country'])
print('City:',res['name'])
print('Longtitude:',res['coord']['lon'])
print('Lotitude:',res['coord']['lat'])
print('Temperature:',res['main']['temp'],'C')
print('Min.Temp:',res['main']['temp'],'C')
print('Max.temp:',res['main']['temp'],'C')
print('Humidity:',res['main']['temp'])
print('Pressure:',res['main']['temp'])





