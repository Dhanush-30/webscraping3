import numpy as np
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
def scrap(field,Location,Experience):
    import time
    import selenium
    import os
    from selenium import webdriver
    import pandas as pd
        
    
    chrome_options = webdriver.ChromeOptions()
    
    chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('headless')
    
    driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)
    url1='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords='+field+'&txtLocation='+Location+'&cboWorkExp1='+str(Experience)

    from selenium import webdriver

    def get_links(n): 
        na=n.find_elements_by_tag_name('h2')[0]
        mae=na.find_elements_by_tag_name('a')[0]
        link=mae.get_property('href')
        return link

    driver = webdriver.Chrome(path)
    driver.get(url1)
    listoflinks=[]
    for i in range(2,27):
        n=driver.find_elements_by_tag_name("header")[i]
        a=get_links(n)
        listoflinks.append(a)
        l=len(listoflinks)
        if l==10:
            break
        else:
            continue
            

    alldetails=[]
    for link in listoflinks:
        driver.get(link)
        time.sleep(3)
        title=driver.find_element_by_xpath('//*[@id="job-detail-main-container"]/div[1]/div[2]/h1').text
        comp=driver.find_element_by_xpath('//*[@id="job-detail-main-container"]/div[1]/div[2]/h2').text
        
        tempj={'job_title':title,
               'company':comp,
          'link for more details':link}
         
        
        alldetails.append(tempj)

    data=pd.DataFrame(alldetails)


    urln='https://www.naukri.com/'+field+'-jobs-in-'+Location+'?k='+field+'&l='+Location+'experience='+str(Experience)
    from selenium import webdriver
    driver.get(urln)
    listoflinksn=[]
    l=driver.find_elements_by_class_name("jobTupleHeader")
    for i in range(len(l)):    
        m=driver.find_elements_by_class_name("jobTupleHeader")[i]
        ma=m.find_elements_by_tag_name("a")[0]
        lik=ma.get_property('href')
        listoflinksn.append(lik)
        length=len(listoflinksn)
        if length==10:
            break
        else:
            continue

    detnau=[]
    for link in listoflinksn:
        driver.get(link)
        time.sleep(5)
        title=driver.find_element_by_tag_name('h1').text
        try:
            comp=driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div[2]/section[1]/div[1]/div[1]/div/a[1]').text
        except:
            pass
        
        tempj={'job_title':title,
               'company':comp,
               'link for more details':link}
         
        detnau.append(tempj)


 

    datanau=pd.DataFrame(detnau)
  


    # In[7]:


    # monster


    urlm='https://www.monsterindia.com/srp/results?query='+field+'&locations='+Location+'&experienceRanges='+str(Experience)+'~'+str(Experience)+'&experience='+str(Experience)+'&searchId=81e909fa-3756-40af-be64-538c1eade7e1'


    driver.get(urlm)

    listoflinksm=[]
    k=driver.find_elements_by_tag_name('h3')
    for i in k:
        try:
            m=i.find_element_by_tag_name('a')
            ma=m.get_property('href')        
            listoflinksm.append(ma)
            length=len(listoflinksm)
            if length==10:
                break
            else:
                continue
        except:
            pass
        

    det=[]
    for link in listoflinksm:
        driver.get(link)
        time.sleep(3)
        
        try:
            title=driver.find_element_by_xpath('//*[@id="jobDetailHolder"]/div/div/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div/div/h1').text
            company=driver.find_element_by_xpath('//*[@id="jobDetailHolder"]/div/div/div[1]/div[2]/div[1]/div[1]/div/div[1]/div/div/div/span/a').text
            tempj={'job_title':title,
               'company':company,
               'link for more details':link}
            det.append(tempj)
        except:
            pass
        

    data1=pd.DataFrame(det)
    


    # In[8]:


    # indeed

    urli='https://www.indeed.co.in/jobs?q='+field+'&l='+Location

    driver.get(urli)

    ik=driver.find_elements_by_tag_name('h2')
    inlinks=[]
    for i in range(len(ik)):
        link=ik[i].find_element_by_tag_name('a').get_property('href')
        inlinks.append(link)
        length=len(inlinks)
        if length==10:
            break
        else:
            continue

    detin=[]
    for link in inlinks:
        driver.get(link)
        title=driver.find_element_by_tag_name('h3')
        titlet=title.text
        try:
            company=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div').text
        except:
            company=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div[4]/a/div/div/h4').text    
        tempj={'job_title':titlet,
              'company':company,
              'link for more details':link}
        detin.append(tempj)

    datain=pd.DataFrame(detin)
    


    # # shine

    # In[64]:


    urls='https://www.shine.com/job-search/'+field+'-jobs-in-'+Location
    driver.get(urls)
    fieldar=driver.find_element_by_xpath('//*[@id="id_q"]')
    driver.find_element_by_xpath('html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]').click()
    fieldar.send_keys(field)
    fieldar.submit()

    k=driver.find_elements_by_tag_name('h3')
    shlinks=[]
    for i in range(1,20):
        try:
            k=driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[1]/div/div[1]/div/div/div[1]/ul/li['+str(i)+']/div[2]/ul[1]/li/h3')
            link=k.find_element_by_tag_name('a').get_property('href')
            shlinks.append(link)
            length=len(shlinks)
            if length==10:
                break
            else:
                continue
        except:
            pass


    shdet=[]
    for link in shlinks:
        driver.get(link)
        comp=driver.find_element_by_xpath('//*[@id="id_search_head"]/div/div[1]/a/span/span/h2').text
        title=driver.find_element_by_xpath('//*[@id="id_search_head"]/div/div[1]/strong/span[1]/h1').text
        tempj={'job_title':title,
              'company':comp,
              'link for more details':link}
        shdet.append(tempj)

    datash=pd.DataFrame(shdet)


    # In[14]:


    # linkedin

    urlin='https://www.linkedin.com/jobs/search?keywords='+field+'&location='+Location+'&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0'


    driver.get(urlin)
    linkin=[]
    for i in range(1,11):
        k=driver.find_element_by_xpath('//*[@id="main-content"]/div/section/ul/li['+str(i)+']/a').get_property('href')
        linkin.append(k)
        if len(linkin)==10:
            break
        else:
            continue

    detlin=[]
    for link in linkin:
        driver.get(link)
        title=driver.find_element_by_xpath('/html/body/main/section[1]/section[2]/div[1]/div[1]/h1').text
        try:
            company=driver.find_element_by_xpath('/html/body/main/section[1]/section[2]/div[1]/div[1]/h3[1]/span[1]/a').text
        except:
            company=driver.find_element_by_xpath('/html/body/main/section[1]/section[2]/div[1]/div[1]/h3[1]/span[1]').text

        tempj={'job_title':title,
              'company':company,
              'link for more details':link}
        detlin.append(tempj)


    datalin=pd.DataFrame(detlin)
    


    # # total data

    # In[90]:


    tdata=pd.concat([data,datanau,data1,datain,datash,datalin])
    

    return tdata

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit',methods=['GET','POST'])
def submit():

    field=request.form['Field']
    experience=request.form['Experience']
    location=request.form['Location']
    output=scrap(field=field,Experience=experience,Location=location)
    
    return render_template('index.html',prediction_text=output)
if __name__ == "__main__":
    app.run(debug=True)
