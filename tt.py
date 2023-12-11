age = 20
if age < 20:
    print('aa')
else:
    print('bb')
'apple' + 'grape'
'apple' * 3

def user_sum(n):
    s = 0
    for i in range(1, n+1):
        s = s + 1
    s

user_sum(100)
user_sum(200)

s = 0
for i in range(10, 21):
    s = s + 1
s
from matplotlib import pyplot as plt
import streamlit as st

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ':rainbow[Comedy]':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")

import streamlit as st
import matplotlib.pyplot as plt
# import numpy as np

c1 = st.sidebar.radio('선의 폭을 선택하시오',['red','green','blue','orange'])
s1 = st.sidebar.radio('선의 형태를 선택하시오',['-',':','-.','--'])
m1 = st.sidebar.radio('마커의 스타일을 선택하시오',['o','^','s','p'])
fig, ax = plt.subplots()

love = []
y = []
for i in range(-20,21,2):
    love.append(i)
    y.append(-2*i*i+3*i+5)

plt.plot(love,y,color=c1, linestyle=s1, marker=m1)
st.pyplot(fig)

import sys
sys.exit()

fig, ax = plt.subplots()


