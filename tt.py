import streamlit as st
import matplotlib.pyplot as plt
# import numpy as np

love = [] 
x = []
for i in range(-29,30,7):
    love.append(i)
    x.append(-2*i*i+3*i+5)

a = st.number_input('a의 값을 입력하시오', value=2.0, step=1.0)
b = st.number_input('b의 값을 입력하시오', value=-1.0, step=1.0)
c = st.number_input('c의 값을 입력하시오', value=15.0, step=1.0)
d = st.number_input('d의 값을 입력하시오', value=2000.0, step=100.0)

c1 = st.sidebar.radio('선의 색을 선택하시오',['red','green','blue','orange'])
s1 = st.sidebar.radio('선의 형태를 선택하시오',['-',':','-.','--'])
m1 = st.sidebar.radio('마커의 형태를 선택하시오',['o','^','s','p'])
fig, ax = plt.subplots()

plt.plot(love,x,color=c1, linestyle=s1, marker=m1)
st.pyplot(fig)

import sys
sys.exit()

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

import streamlit as st
import matplotlib.pyplot as plt
# import numpy as np

love = [] 
x = []
for i in range(-29,5,28):
    love.append(i)
    x.append(-2*i*i+3*i+5)

a = st.number_input('a의 값을 입력하시오', value=2.0, step=1.0)
b = st.number_input('b의 값을 입력하시오', value=-1.0, step=1.0)
c = st.number_input('c의 값을 입력하시오', value=15.0, step=1.0)
d = st.number_input('d의 값을 입력하시오', value=2000.0, step=100.0)

c1 = st.sidebar.radio('선의 색을 선택하시오',['red','green','blue','orange'])
s1 = st.sidebar.radio('선의 형태를 선택하시오',['-',':','-.','--'])
m1 = st.sidebar.radio('마커의 형태를 선택하시오',['o','^','s','p'])
fig, ax = plt.subplots()

plt.plot(love,y,color=c1, linestyle=s1, marker=m1)
st.pyplot(fig)

import sys
sys.exit()