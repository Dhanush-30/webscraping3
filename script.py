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
    ##
    urln='https://www.naukri.com/'+field+'-jobs-in-'+Location+'?k='+field+'&l='+Location+'experience='+Experience
    from selenium import webdriver
    driver.get(urln)
    time.sleep(2)
    detnau=[]
    for i in range(1,4):
        a=driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/section[2]/div[2]/article['+str(i)+']/div[1]/div[1]/a')
        title=a.text
        company=driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/section[2]/div[2]/article['+str(i)+']/div[1]/div[1]/div').text
        link=a.get_property('href')
        tempj={'job_title':title,
               'company':company,
               'link for more details':link}

        detnau.append(tempj)

    datanau=pd.DataFrame(detnau)
    tdata=pd.concat([data,datanau])
    return tdata.to_html(header=True)


