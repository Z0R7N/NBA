# NBA
auto test for portfolio  
 python pytest selenium webdriver

#### Test Suit  
test case: 001

file - test_main_page.py  
method - test_user_can_login_to_account

Click link "Sign in", enter login and password, click button "SIGN IN"

1) Open page - https://www.nba.com/
2) If url is wrong click link - NBA.COM
3) Click "Accept" button in the pop-up window
4) Click link "Sign In"
5) Click link "Sign in to NBA Account"
6) Enter Email in text field - Email Address
7) Enter Password in text field - Password
8) Click button - SIGN IN
9) Check element "My NBA Account" is visible

Expected result: element "My NBA Account" is visible

Actual result: element "My NBA Account" is visible