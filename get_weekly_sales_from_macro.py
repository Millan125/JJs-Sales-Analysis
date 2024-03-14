def do_gwsfm():

    #import webdriver
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import Select
    import request_week_range
    from time import sleep 

    #create webdriver object
    driver = webdriver.Chrome()

    #get macromatix
    driver.get("https://jimmyjohns.macromatix.net/MMS_Logon.aspx")

    #get username element
    username_element = driver.find_element(By.ID, "Login_UserName")

    #querey username
    username = input("what's your username?")

    #clear field and input username
    username_element.clear()
    username_element.send_keys(username)

    #get password element
    password_element = driver.find_element(By.ID, "Login_Password")

    #querey password
    password = input("what's your password?")

    #clear field and input password
    password_element.clear()
    password_element.send_keys(password)

    #click login button
    driver.find_element(By.NAME, "Login$Button1").click()

    #click Reports dropdown 
    driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/ul/li[5]/a").click()

    #click Weekly Reports in dropdown
    driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/ul/li[5]/div/ul/li/div/div/ul/li[1]/a").click()


    #click analysis dropdown menu
    drop_analysis = Select(driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div[1]/table/tbody/tr/td/table[2]/tbody/tr[1]/td[2]/select"))

    #select weekly sales
    drop_analysis.select_by_index(9)

    #querey year
    requested_year = input("which year?")

    #select the year from the year dropdown menu
    drop_year = Select(driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div[1]/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/select[2]"))
    drop_year.select_by_value(str(requested_year))

    week_ranger = request_week_range.do_rwr(requested_year)

    #click the send to download center button off
    driver.find_element(By.ID, "ctl00_ph_CheckBoxSendToDownloadManager").click()

    #loop through all selected weeks of the year and send all to excell
    for week in week_ranger:

        driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div[1]/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/a[1]").click()
        drop_week = Select(driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div[1]/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/select[1]"))
        drop_week.select_by_value(str(week))
        driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div[1]/table/tbody/tr/td/div[2]/div/table/tbody/tr/td[4]/span").click()

    sleep(5)

if __name__ == "__main__":
    do_gwsfm()