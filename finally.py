from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import json

import openai
import os
import streamlit as st
import requests
import pdfplumber

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By



jobs = []

titles = []
names = []
salaries = []
locations = []
discr = []



titles_main =[]
names_main = []
salaries_main = []
locations_main = []
disc_main = []

t = []
n = []
s = []
l = []
d = []



def extract_data(feed):
    data = []
    return None # build more code to return a dataframe 

def jobsfor(job,location):
    jobs = []

    titles = []
    names = []
    salaries = []
    locations = []
    discr = []



    titles_main =[]
    names_main = []
    salaries_main = []
    locations_main = []
    disc_main = []

    t = []
    n = []
    s = []
    l = []
    d = []


    options = Options()
    options.add_argument("--headless")
    options.add_argument("--user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'")


    driver = webdriver.Chrome(options = options)
    d_driver = webdriver.Chrome(options = options)
    search_url = f"https://uk.indeed.com/jobs?q=web developer&l=London&from=searchOnHP"
    search = f"https://uk.indeed.com/jobs?q={job}+£40%2C000&l={location}&vjk=1186702a8e9fb69e"
    driver.get(search)

    job_elements = driver.find_elements(By.ID,"mosaic-provider-jobcards")


    for listing in job_elements:
        jobs.append(listing.find_elements(By.XPATH, "//ul[@class='jobsearch-ResultsList css-0']//li"))



    for job in jobs:
        titles.append(job[0].find_elements(By.XPATH,"//span[@title]"))
        names.append(job[1].find_elements(By.XPATH, '//span[@class="companyName"]'))
        ss= job[2].find_elements(By.XPATH,'//div[@class="metadata salary-snippet-container"]/div[@class="attribute_snippet"]')
        locations.append(job[3].find_elements(By.XPATH, '//div[@class="companyLocation"]'))
        #pdb.set_trace()
        discr.append(job[4].find_elements(By.XPATH,"//*/a[@href]"))
      

        
        if ss is None or len(ss)<3:
            salaries.append("Unknown Salary")
            #print("Unknown Salary")
        else:
            salaries.append(ss)



        #print(job[1].text)
        


    for link in job[4].find_elements(By.XPATH,"//*/a[@href]"):
       
        ll = link.get_attribute("href")
        
        if ll.startswith("https://uk.indeed.com/pagead/clk"):
            disc_main.append(link.get_attribute("href"))
            print(ll)
        else:
            pass




    #print(discr)

    #print(len(titles),len(names),len(salaries),len(locations))

    ##########################
      
    for title in titles:
        titles_main.append(title)


    for name in names:
        #print("name len:", len(name))
        names_main.append(name)  

    for salary in salaries:
        salaries_main.append(salary)
        #print("salary len:", len(salary))

    for location in locations:
        locations_main.append(location)  

    for dis in discr:
        #print(dis.get_attribute("href"))
        #disc_main.append(dis.get_attribute("href"))
        pass

    ############################


    for yep in titles_main:
        #print(yep)
        for y in yep:
            #print(y.text)
            t.append(y.text) 
            pass


    for yep2 in names_main:
        #print("hhh",yep2.text)
        for y in yep2:
            #print(y.text)
            n.append(y.text)
            pass
        



    for yep3 in salaries_main:
        #print("bbb",yep3.text)
        for y in yep3:

            #print(y.text)
            s.append(y.text)
            pass
       



    for yep4 in locations_main:
        #print("kkk",yep4.text)
        for y in yep4:
            #print(y.text)
            l.append(y.text)
            pass
      

    job_type = "web developer"
    place = "London"
    cv_text = "JavaScript"


    #print(len(t),len(n),len(s),len(l))

    #print("saleries:", len(salaries))
    #print("salaries main", len(salaries_main))

    print(len(disc_main))
    #print(len(d))

    if len(disc_main) < len(t):
        missing = len(t) - len(disc_main)
        disc_main += ["https://uk.indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0BGjLRKdjqyImUJI62I12mXxLUuyZdbXOS0MOSu2OUiW33ZaPiKiAJ0lm5exG7tf3TcHSNarqtzTXtssi_Y0u53rDwnOxxqcMq516AdnxS37En3d7MPCmOd7X0wMUDYLRPbQqI_TpUj7omZ_USJbi6TS_K1SMTdI9Lpi2LRXXhxpnh8TH8iZcStECSpzYZkjS5EzfONGFpjMYOtEOJ8o8LoZWlwEilJASGYr0Wp74qtoEX5gUGFgxXsyy75xDWp0H9Wzv-Uelqb1PQhDPXwVqGqoZJMPtftA2Gp8UhORLGAdUXJ87Acwc-AicRNdU8UnLcabrMMKSA494n7BuHjZg9pz955OOQsH1Fx-jjZDanraMD61RjNioSgYhfivu2z9px4QfmXxL1V0BHexb93_BQJ5yKFSMM8LXGDdx6-08Q3OXR9fqHD9p7Cd3_bacY2xw72BB3QvTrUe67mAcn_N__WcDsDnx10g1BDbZRYINKUqYLY_vT-bFjGFdv_2cNTwMpqsxFxhFNnx2N25EKDXYb0inemz88DUgkfI955zliRGUE-9fpHDRIn&xkcb=SoDA-_M3TQWsE0AIkT0LbzkdCdPP&p=12&fvj=1&vjs=3"] * missing



    for lily in disc_main:
        d_driver.get(lily)
        di = driver.find_element(By.ID,"jobDescriptionText")
        d.append(di.text[:50])
        print(di.text)



    if len(s) < len(t):
        missing = len(t) - len(s)
        s += ["Unknown"] * missing

    data = [
        {'title': t[i], 'company': n[i], 'salary': s[i], 'location': l[i], 'Description': d[i]}
        for i in range(len(t))
    ]


    json_data = json.dumps(data, indent=4)
    return json_data

json_data = jobsfor("web developer", "London")


jobs = []
final_job_list = []
job_titles= []
job_companies =[]
job_salaries = []
job_locations = []

# parse the data
parsed_data = json.loads(json.dumps(json_data))


# Set the GPT-3 API key
openai.api_key = "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"

# Read the text of the article from a file
# with open("article.txt", "r") as f:
#     article_text = f.read()





JobField = st.text_area("Enter your Job Field")
JobSpecialisation = st.text_area("Enter your Job Specialisation")
Distance = st.text_area("Enter your commute distance")
Area = st.text_area("Enter your Area")

output_size = st.radio(label = "What kind of output do you want?", 
                    options= ["To-The-Point", "Concise", "Detailed"])

if output_size == "To-The-Point":
    out_token = 50
elif output_size == "Concise":
    out_token = 128
else:
    out_token = 516

uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
if uploaded_file is not None:
    df = extract_data(uploaded_file)

if len(JobField)>1:

    if st.button("Generate Summary",type='primary'):
        

    # Use GPT-3 to generate a summary of the article
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="Please recommend best job in " + JobField+"with specialization in "+JobSpecialisation+"and distance of "+Distance+"km from " + Area+ ": give 5 best job among "+ parsed_data ,
            max_tokens = out_token,
            temperature = 1.0,
        )
        # Print the generated summary
        
        res = response["choices"][0]["text"]
        st.success(res)
        st.download_button('Download result', res)
else:
    st.warning("Not enough words to summarize!")






