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

    driver.get(url1)
    listoflinks=[]
    listoflinks=[get_links(driver.find_elements_by_tag_name("header")[i]) for i in range(2,4)]      
    alldetails=[]
    for link in listoflinks:
        driver.get(link)
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
        if length==2:
            break
        else:
            continue

    detnau=[]
    for link in listoflinksn:
        driver.get(link)
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
        if length==2:
            break
        else:
            continue

    detin=[]
    for link in inlinks:
        driver.get(link)
        title=driver.find_element_by_tag_name('h3')
        titlet=title.text
        try:
            company=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div[2]/div').text
        except:
            company=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div[4]/a/div/div/h4').text
                     
             
        tempj={'job_title':titlet,
              'company':company,
              'link for more details':link}
        detin.append(tempj)

    datain=pd.DataFrame(detin)
    



    # In[64]:


  


    tdata=pd.concat([data,datanau,datain])
    return tdata.to_html(header=True)


