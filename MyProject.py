from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, executable_path=".\chromedriver")

#Visit the given URL: https://test.sharebus.co/
driver.get('https://test.sharebus.co/')


def main():
    #driver = webdriver.Chrome('.\chromedriver')
    #driver.get('https://test.sharebus.co/')

    #Navigate to login page by clicking the "Sign in" button
    signin_btn = driver.find_element('xpath', '//li[@class="nav-item text-nowrap"]')
    signin_btn.click()
    time.sleep(10)

    #Login with email("brainstation23@yopmail.com") and password("Pass@1234")
    email_field = driver.find_element('xpath', '//input[@id="email"]')
    email_field.send_keys("brainstation23@yopmail.com")
    time.sleep(10)

    pass_field = driver.find_element('xpath', '//input[@id="password"]')
    pass_field.send_keys("Pass@1234")
    time.sleep(10)

    signin_submit = driver.find_element('xpath', '//button[@class="btn sb-btn-lg sb-btn-primary fw-bold rounded-pill w-100"]')
    signin_submit.click()
    time.sleep(20)

    #Select the user as "Sharelead" from the menu options
    select_user_field = driver.find_element('xpath', '//span[@class="p-dropdown-trigger-icon pi pi-chevron-down"]')
    select_user_field.click()
    time.sleep(10)

    #Sharelead from dropdown
    sharelead_user = driver.find_element('xpath', '//span[text()="Sharelead"]')
    sharelead_user.click()
    time.sleep(10)

    #Continue Button
    continue_button = driver.find_element('xpath', '//button[@class="btn btn-primary btn btn-success text-white align-self-center rounded-pill fw-bolder px-4 my-3 d-flex justify-content-between align-items-center mt-3"]')
    continue_button.click()
    time.sleep(10)

    #Cookies
    cookies_button = driver.find_element('xpath', '//button[@class="btn sb-btn-md sb-btn-primary text-white btn-sm ms-2"]')
    cookies_button.click()
    time.sleep(10)


    #Set Up a ShareBus
    set_up_sharebus_button = driver.find_element('xpath', '//button[@class="btn btn-primary sb-btn-primary sb-btn-lg px-4 py-1 my-2 rounded-pill border-0 fw-400"]')
    set_up_sharebus_button.click()
    time.sleep(10)

#  Insert required Trips details and click "Continue" [Please use location address as: From="Oslo, Norway" and To="Kolbotn, Norway"]
    start_point_field1 = driver.find_element('xpath', '//input[@id="startPoint"]')
    start_point_field1.send_keys("Oslo, Norway")
    time.sleep(10)

    #From Oslo, Norway
    start_point_field2 = driver.find_element('xpath', '//span[text()="Oslo, Norway"]')
    start_point_field2.click()
    time.sleep(10)



    #From Kolbotn, Norway
    start_point_field3 = driver.find_element('xpath', '//input[@id="destination"]')
    start_point_field3.send_keys("Norway Resistance Museum")
    time.sleep(10)

    #From Kolbotn, Norway
    start_point_field4 = driver.find_element('xpath', '//span[text()="Norway Resistance Museum"]')
    start_point_field4.click()
    time.sleep(10)

    #Date field
    date1 = driver.find_element('xpath', '//input[@placeholder="Departure Date"]')
    date1.click()
    time.sleep(10)

    #Date pick
    date2 = driver.find_element('xpath', '//span[text()="20"]')
    date2.click()
    time.sleep(10)

    #Time field
    time1 = driver.find_element('xpath', '//input[@placeholder="Time"]')
    time1.click()
    time.sleep(10)

    #Radio button
    radio = driver.find_element('xpath', '//label[@for="returnTripswitch"]')
    radio.click()
    time.sleep(10)



    #Radio cotntinue button
    continue1 = driver.find_element('xpath', '//button[@class="btn sb-btn-primary sb-btn-lg rounded-pill border-0 fw-bold d-flex justify-content-center align-items-center"]')
    continue1.click()
    time.sleep(10)

    #  On the Membership page click "Yes" and select "NTNUI" club and click "Continue"
    yes_button = driver.find_element('xpath', '//button[text()="Yes"]')
    yes_button.click()
    time.sleep(10)


    #yes search
    yes_search_field = driver.find_element('xpath', '//input[@placeholder="Search or select"]')
    yes_search_field.click()
    time.sleep(10)

    yes_search_field.send_keys("NTNUI")
    time.sleep(10)

    #yes continue button
    yes_continue_button = driver.find_element('xpath', '//button[@class="btn sb-btn-lg sb-btn-primary rounded-pill fw-bold d-flex justify-content-center align-items-center"]')
    yes_continue_button.click()
    time.sleep(15)

    #  Need any ticket for himself? click on the "No" button
    no_ticket_himself = driver.find_element('xpath', '//button[@class="btn gray-white-bg ship-gray btn-discount-size rounded-end"]')
    no_ticket_himself.click()
    time.sleep(15)

    #  Activate ticket discounts? click the "No" button
    no_activation = driver.find_element('xpath', '//button[@class="btn gray-white-bg ship-gray btn-discount-size rounded-end"]')
    no_activation.click()
    time.sleep(10)

    #  Click on the "Create ShareBus" button
    create_sharebus = driver.find_element('xpath', '//button[@class="btn sb-btn-lg sb-btn-primary rounded-pill fw-bold d-flex justify-content-center align-items-center"]')
    create_sharebus.click()
    time.sleep(20)    

    #  Click on the "Publish" button
    publish_button = driver.find_element('xpath', '//button[@class="btn sb-btn-primary sb-btn-lg mt-2 rounded-pill fw-bold  d-flex justify-content-center align-items-center"]')
    publish_button.click()
    time.sleep(10)    
    
    #  Insert data on required fields(trip name)
    trip_name = driver.find_element('xpath', '//input[@class="form-control rounded"]')
    trip_name.click()
    time.sleep(10)
    trip_name.send_keys("Sport Trip")
    time.sleep(10)

    #  Insert data on required fields (trip category)
    trip_category = driver.find_element('xpath', '//div[@class="trip-category d-flex justify-content-center align-items-center flex-grow-1 border border-light px-4 rounded me-2 mb-2"]')
    trip_category.click()
    time.sleep(10)

    #  Click on the "Review and publish" button
    review_publish_button = driver.find_element('xpath', '//button[@class="btn sb-btn-primary sb-btn-lg px-4  rounded-pill d-flex align-items-center fw-bold ms-auto"]')
    review_publish_button.click()
    time.sleep(10)

    #  Click on the "Publish" button
    publish_button1 = driver.find_element('xpath', '//button[@class="btn sb-btn-primary sb-btn-lg w-auto rounded-pill lh-1 px-4 fw-bold d-flex justify-content-center align-items-center"]')
    publish_button1.click()
    time.sleep(15)

    #  Click on "my busses" from the navbar
    nav_mubusses = driver.find_element('xpath', '//button[@class="btn sb-btn-sharelead rounded-pill sb-btn-lg text-dark fw-bold"]')
    nav_mubusses.click()
    time.sleep(15)

    #  Verify that the new Trip is displayed on the "My busses" page
    # view sharebus
    sharebus = driver.find_element('xpath', '//button[@class="btn sb-btn-lg sb-btn-primary fw-bold px-2 mb-2"]')
    sharebus.click()
    time.sleep(15)

    #details
    details = driver.find_element('xpath', '//span[@class="rounded-pill border-0 inactive"]')
    details.click()
    time.sleep(15)
    
    busNumber = driver.find_element('xpath', '//p[@class="text-start border border-1 border-light rounded p-2 mb-0"]')
    # busNumber variable will generate bus signage.
    # Then we will check this bus signage with previously created bus signage in sharebus confirmation page.
    
main()