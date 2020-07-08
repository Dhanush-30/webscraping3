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
    urls='https://www.shine.com/job-search/'+field+'-jobs-in-'+Location
    driver.get(urls)
    try:
        driver.find_element_by_xpath('//*[@id="push_noti_popup"]/div[1]/span').click()
    except:
        pass
    driver.get(urls)
    driver.find_element_by_xpath('html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]').click()
    fieldar=driver.find_element_by_xpath('//*[@id="id_q"]')
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
            if length==3:
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
    try:
        driver.find_element_by_xpath('//*[@id="main-content"]/div/section/ul/li['+str(i)+']/a').get_property('href')
    except:
        driver.get(urlin)
    for i in range(2,15):
        k=driver.find_element_by_xpath('//*[@id="main-content"]/div/section/ul/li['+str(i)+']/a').get_property('href')
          
        linkin.append(k)
        if len(linkin)==3:
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


    tdata=pd.concat([datash,datalin])
    return tdata.to_html(header=True)
