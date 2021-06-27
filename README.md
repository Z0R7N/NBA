# NBA
auto test for portfolio  
python pytest selenium webdriver

#### Test Suit  
test case: 001

file   - test_main_page.py  
method - test_user_can_login_to_account

Open page https://www.nba.com/, click link "Sign in", enter login and password,  
click button "SIGN IN"

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
_________
test case: 002

file   - test_store_page.py  
method - test_guest_can_add_item_to_cart  

Open page https://www.nbastore.eu/, choose group of store, choose item,  
add item to cart, check item price and cart price  

1) Open page - https://www.nbastore.eu/
2) Click button "Continue" in popup window
3) Accept Cookie Consent, if there is
4) Mouse over link - SHOP BY TEAM
5) Click any team
6) Close popup message window
7) Click any item
8) Choose any size
9) Click button - Add to Cart
10) Check price, must be the same for the item and in the cart

Expected result: the price is the same for the item and in the cart  
Actual result: the price is the same for the item and in the cart
_____________
test case: 003  

file   - test_game_page.py
method - test_guest_can_choose_game

Open page https://www.nba.com/, click link "Games", click dropdown menu "month year",  
click any date with game, check text "BOX SCORE" is visible

1) Open page - https://www.nba.com/
2) If url is wrong click link "NBA.COM"
3) Click "Accept" cookie
4) Click link "Games"
5) Close popup window if there is
6) Click dropdown menu "month year"
7) Click any date with game
8) Check link with text "BOX SCORE" is visible

Expected result: Link "BOX SCORE" is visible  
Actual result: Link "BOX SCORE" is visible  
