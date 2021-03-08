# Museum Exhibit 
**Summary**: Our website is a museum exhibit that encompasses the aspects of art/culture/history. Within the website, depending on the user’s interests (figured out through a form), the user will be able to visit a variety of exhibits like photography, international culture, music and more. They also have access to a gift shop where they can buy items that interest them. 

**Authors**: Sriya Chilla, Crystal Widjaja, Maggie Killada, and Ridhima Inukurti

IMPORTANT: TO ACCESS THE WEBSITE YOU MUST BE SIGNED IN. Click "Already have an account? Sign In" and sign in with the given username and password.

 - Username: test
 - Password: test

# Finals Week (Technicals Overview)
 - [Planetarium Exhibit](https://github.com/crystalwidjaja/lobster/projects/2#card-55321632) by Sriya and Maggie
   - A. The planetarium exhibit includes a panorama of the solar system. It will also have [“infospots” (located on top of each Jupiter, for example)](https://github.com/crystalwidjaja/lobster/blob/main/templates/planetarium.html#L113-#L153) that the user can click on. Clicking on “info spots” will show information about each of the planets.
   - B. Code link: see [planetarium.html](templates/planetarium.html)
     - Sriya:
       - I used an image map with coordinates to allow the user to click infospot on each planet. For example, Mercury used ```  <area shape="rect" coords="100,250,125,300" alt="Mercury"> ```
       - I used a JS event to figure out which planet is being clicked, then display text on information about the planet.
         - ``` function showPlanetInfo(e){ let planet = e.target.getAttribute('alt') let showModal = true; ```
         - ``` case 'Mercury': msg = 'Mercury is the closest planet to the Sun...'; break; ```
       - There is also a close button to close the modal.
         - ``` document.querySelector('.popupCloseButton').addEventListener('click', function(){ modal.style.display = 'none'; ```
   - C. Runtime link: http://lobstersmuseum.cf/planetarium
 - [Music Exhibit](https://github.com/crystalwidjaja/lobster/projects/2#card-53148483) by Crystal
   - A. The music exhibit is split into different eras with a symbol for each decade (jukebox, phonograph, radio, etc). The images will be buttons that can play various decade themed playlists. The code will primarily use HTML and CSS.
   - B. Code link: see [song.csv](song.csv), [song.py](song.py), [music.css](templates/music.css), and [music.html](templates/music.html)
   - C. Runtime link: http://lobstersmuseum.cf/music
- [Art Exhibit](https://github.com/crystalwidjaja/lobster/projects/2#card-53148527) by Sriya and Ridhima
   - A. The Art Exhibit displays art from various different time periods. The user can view these images by scrolling sideways, a feature that mimics walking in a museum. Also, the user can hover over the art images to learn more information. This code primarily uses backend python. 
   - B. Code link: see [artpiece.py](artpiece.py), [photography.html](photography.html)
   - C. Runtime Link: http://lobstersmuseum.cf/art
- [Login](https://github.com/crystalwidjaja/lobster/projects/2#card-55341819) by Maggie and Ridhima
   - A. The user must create an account with a username and passowrd to access the website. The user must also provide information such as age, gender, email, and favorites (see next bullet). If the user has already created an account, they can use the "Sign In" option and input their username and password. The login page frontend uses CSS to match with the theme colors, font, and layout of the museum webpage.
   - B. Code link: see [login.html](templates/login.html) and [landing_page.html](templates/landing_page.html)
   - C. Runtime link: http://lobstersmuseum.cf/login OR http://104.63.255.249:8081/
 - [Favorites Page](https://github.com/crystalwidjaja/lobster/projects/2#card-51242483) by Crystal and Maggie
   - A. The user is able to select a few exhibits that may interest them. When they first create an account on the website, they can choose from Botany, History, Photography, Music, and Space. The topics they choose will appear in the "My Favorites" page when the user logs in to the website.
   - B. Code link: see [favorites.html](templates/favorites.html) and [landing_page.html](templates/landing_page.html)
   - C. Runtime link: http://104.63.255.249:8081/favorites
 - [Search Bar](https://github.com/crystalwidjaja/lobster/projects/2#card-51316886) by Maggie and Crystal
   - A. The search bar feature in the top right corner of the nav bar allows users to find information from anywhere on the website.
   - B. Code link: see [searchresults.html](searchresults.html)
   - C. Runtime link: http://lobstersmuseum.cf/home
 - [About Us Page](https://github.com/crystalwidjaja/lobster/projects/2#card-52328560) by Crystal
   - A The user can learn about the creators of the website through the About Us page. This page uses Python variables to list a picture of us, our name, birthday, star sign, and a fun fact.
   - B. Code link: see [about.py](about.py) and [about_us.html](templates/about_us.html)
   - C. Runtime link: http://104.63.255.249:8081/about_us

- COLLEGE BOARD REQUIREMENTS
  - INPUTS: Our project has inputs, specifically for the making of a user account. There is a form for new users and a form for returning users. These involve “GET” and “POST.” The type of input we are using is a html form for the user to input their information. We also use checkboxes for choosing favorites and a dropdown menu to specific gender. Evidence in [landing_page.html](https://github.com/crystalwidjaja/lobster/blob/main/templates/landing_page.html#L114-#L155) and [login.html](https://github.com/crystalwidjaja/lobster/blob/main/templates/login.html#L90-#L100)
  - LISTS: One way we use lists is through extracting the data from a source through a REST API. Evidence in [botany.py](https://github.com/crystalwidjaja/lobster/blob/ca0465e152014101665ebd9d518ad86ec8d514f6/botany.py#L25-#L52)
  - PROCEDURES: We are using these procedures mainly through our main.py which contains most of the routes to our websites. Evidence in [main.py](https://github.com/crystalwidjaja/lobster/blob/ca0465e152014101665ebd9d518ad86ec8d514f6/main.py#L122-#L211)
  - ALGORITHMS: We use algorithms to create user accounts and sessions. Additionally, the algorithms are used to direct the user throughout the pages via conditional statements. Evidence in [main.py](https://github.com/crystalwidjaja/lobster/blob/ca0465e152014101665ebd9d518ad86ec8d514f6/main.py#L78-#L118)
  - OUTPUTS: Our Favorites page creates a customized page of exhibits based on the user input. For example, if the user chooses the art and planetarium exhibits when they make an account, their Favorites page will display these 2 exhibits. Evidence in [favorites.html](https://github.com/crystalwidjaja/lobster/blob/ca0465e152014101665ebd9d518ad86ec8d514f6/templates/favorites.html#L107-#L139)

# Completed Tickets/Goals for Team (Week 2/15/2021)
### CODE REVIEW IS INCORPORATED IN THE FOLLOWING TICKET OVERVIEWS
 - [Planetarium 3D Panorama (Frontend)](https://github.com/crystalwidjaja/lobster/projects/2#card-55321632) by Sriya
   - A. The planetarium exhibit will include a panorama of solar system. It will also have [“infospots” (located on top of each Jupiter, for example)](https://github.com/crystalwidjaja/lobster/blob/main/templates/planetarium.html#L113-#L153) that the user can click on. Clicking on “info spots” will also shows information from database about planets.
    - NOTE: The infospot feature is still in progress. Currently, Jupiter is the only working infospot and will give an alert when clicked on, but still needs a link to the database. My goal is to complete all infospots for next week.
   - B. Code link: see [planetarium.html](templates/planetarium.html)
   - C. Runtime link: http://lobstersmuseum.cf/planetarium
 - [Music Exhibit (Backend)](https://github.com/crystalwidjaja/lobster/projects/2#card-53148483) by Crystal
   - A. The music exhibit will be split into different eras with a symbol for each decade (jukebox, phonograph, radio, etc). The code will primarily use HTML and CSS. The images will be buttons that can play various decade themed playlists
   - B. Code link: see [song.csv](song.csv), [song.py](song.py), [music.css](templates/music.css), and [music.html](templates/music.html)
   - C. Runtime link: http://lobstersmuseum.cf/music
- [Art Exhibit Backend](https://github.com/crystalwidjaja/lobster/projects/2#card-53148527) by Ridhima
   - A. The art exhibit presents the information for each of the art pieces and is immediately available when you hover over the art piece. This code primarily uses backend python. 
   - B. Code link: see [artpiece.py](artpiece.py), [photography.html](photography.html)
   - C. Runtime Link: http://lobstersmuseum.cf/art
- [Login (Frontend)](https://github.com/crystalwidjaja/lobster/projects/2#card-55341819) by Maggie
   - A. The login page frontend now matches with the theme colors and layout of the museum webpage. Now, the css is revised and has different colors and font.
   - NOTE: The search bar feature is still in progress. Currently, the css is finished for the search bar, but I will continue to work on it to perform a search successfully by next week.
   - B. Code link: see [login.html](templates/login.html) and [login.html](login.html)
   - C. Runtime link: http://lobstersmuseum.cf/login

- CrossOver Suggestions from other team (Sushi): 
  - 1) For the landing page, make sure not to display the output information on that same page. Make sure you hide that information once it is stored within the database. 
  - 2) Make sure the frontend for the login and sign in page have the same theme style that as the museum exhibit colors because they are very different. (presentation wise)
- Crossover Revisions: 
  - 1) For the login page the color scheme is now corrected and fits in with the museum scheme colors. 
  - 2) For the landing page, there is no longer any information outputed within the same information. All the information is stored within the database and hidden from the users. 

- COLLEGE BOARD REQUIREMENTS
  - INPUTS: Our project has inputs, specifically for the making of a user account. There is a form for new users and a form for returning users. These involve “GET” and “POST.” The type of input we are using is a html form for the user to input their information. We also use checkboxes for choosing favorites and a dropdown menu to specific gender. Evidence in [landing_page.html](https://github.com/crystalwidjaja/lobster/blob/main/templates/landing_page.html#L114-#L155) and [login.html](https://github.com/crystalwidjaja/lobster/blob/main/templates/login.html#L90-#L100)
  - LISTS: One way we use lists is through extracting the data from a source through a REST API. Evidence in [botany.py](https://github.com/crystalwidjaja/lobster/blob/ca0465e152014101665ebd9d518ad86ec8d514f6/botany.py#L25-#L52)
  - PROCEDURES: We are using these procedures mainly through our main.py which contains most of the routes to our websites. Evidence in [main.py](https://github.com/crystalwidjaja/lobster/blob/ca0465e152014101665ebd9d518ad86ec8d514f6/main.py#L122-#L211)
  - ALGORITHMS: We use algorithms to create user accounts and sessions. Additionally, the algorithms are used to direct the user throughout the pages via conditional statements. Evidence in [main.py](https://github.com/crystalwidjaja/lobster/blob/ca0465e152014101665ebd9d518ad86ec8d514f6/main.py#L78-#L118)
  - OUTPUTS: Our Favorites page creates a customized page of exhibits based on the user input. For example, if the user chooses the art and planetarium exhibits when they make an account, their Favorites page will display these 2 exhibits. Evidence in [favorites.html](https://github.com/crystalwidjaja/lobster/blob/ca0465e152014101665ebd9d518ad86ec8d514f6/templates/favorites.html#L107-#L139)

# Completed Tickets/Goals for Team (Week 2/1/2021)
 - [Planetarium 3D Panorama (Frontend)](https://github.com/crystalwidjaja/lobster/projects/2#card-53783120)
   - A. The planetarium exhibit will include a 3D panorama of solar system that has interactive to drag around and explore. It will also have “infospots” that the user can click on to bring a certain planet to the center of attention. Clicking on “info spots” will also shows information from database about planets.
   - B. Code link: see [planetarium.html](templates/planetarium.html)
   - C. Runtime link: http://104.63.255.249:8081/planetarium
 - [Music Exhibit (Backend)](https://github.com/crystalwidjaja/lobster/projects/2#card-53148483)
   - A. The music exhibit will be split into different eras with a symbol for each decade (jukebox, phonograph, radio, etc). The code will primarily use HTML and CSS. The images will be buttons that can play various decade themed playlists
   - B. Code link: see [song.csv](song.csv), [song.py](song.py), [music.css](templates/music.css), and [music.html](templates/music.html)
   - C. Runtime link: http://104.63.255.249:8081/music
 - [Carousel](https://github.com/crystalwidjaja/lobster/projects/2#card-53783149)
   - A. The carousel will be an image slider for the botany exhibit (using plants for images). The code will use mainly HTML and CSS with a little bit of JS for the radio button. The carousel is clickable to allow the user to move to the next image.
   - B. Code link: see [botany.py](botany.py) and [botany.html](templates/botany.html)
   - C. Runtime link: http://104.63.255.249:8081/
 - [Planetarium (Backend)](https://github.com/crystalwidjaja/lobster/projects/2#card-53783136)
   - A. The planetarium backend will be include an API from the web to get content for the page. This content will include information about planets. The backend will utilize python and will link to the frontend through the planetarium exhibit.
   - B. Code link: see [planetarium.html](templates/planetarium.html) and [planetarium.py](planetarium.py)
   - C. Runtime link: http://104.63.255.249:8081/planetarium

# Completed Tickets/Goals for Team (Week 1/11/2021)
 - [Log in](https://github.com/crystalwidjaja/lobster/projects/2#card-51525126)
   - A. The user must create an account with a username and passowrd to access the website. The user must also provide information such as age, gender, email, and favorites (see next bullet). If the user has already created an account, they can use the "Sign In" option and input their username and password.
   - B. Code link: see [landing_page.html](templates/landing_page.html) and [login.html](templates/login.html)
   - C. Runtime link: http://104.63.255.249:8081/
 - [Favorites Page](https://github.com/crystalwidjaja/lobster/projects/2#card-51242483)
   - A. The user is able to select a few exhibits that may interest them. When they first create an account on the website, they can choose from Botany, History, Photography, Music, and Space. The topics they choose will appear in the "My Favorites" page when the user logs in to the website.
   - B. Code link: see [favorites.html](templates/favorites.html) and [landing_page.html](templates/landing_page.html)
   - C. Runtime link: http://104.63.255.249:8081/favorites
 - [About Us Page](https://github.com/crystalwidjaja/lobster/projects/2#card-52328560)
   - A The user can learn about the creators of the website through the About Us page. This page uses Python variables to list a picture of us, our name, birthday, star sign, and a fun fact.
   - B. Code link: see [about.py](about.py) and [about_us.html](templates/about_us.html)
   - C. Runtime link: http://104.63.255.249:8081/about_us
 - [Art Exhibit (frontend)](https://github.com/crystalwidjaja/lobster/projects/2#card-51316952)
   - A. The Art Exhibit displays art from various different time periods. The user can view these images by scrolling sideways, a feature that mimics walking in a museum. Also, the user can hover over the art images to learn more information.
   - B. see [photography.html](templates/photography.html) and [artpiece.py](artpiece.py)
   - C. Runtime link: http://104.63.255.249:8081/photography
   

# Key Features 
 - Exhibits
 

Carousel for photographs
User makes an account to save data -- login (force them to create an account)
  - They can pick favorite subjects, genres of music (like NoRedInk)
  - They choose favorites when they are making their account
Prioritize favorites & recent searches at the top of the page
Planetarium/Botany
  - Google Maps movement kinda
  - Clicking on the plants gives u more info about it
Gift Shops
  - Add to Cart/Bookmarking Items
Search bar in the history section
  - Search history
 # Delivery Plan Week 1 Goals:
Week 1 Goals: 
  - Create IntelliJ and GitHub collaborative centers
  - Create pair shares and documents (project plan and journals)

Week 2 Goals:
  - Start adding content to ReadMe and Journals
  - Flesh out overall goals and plans for the website
  - Start storyboarding the website

Week 3 Goals:
  - Create homepage on IntelliJ with navigation bar
  - Start to create login with username and password

Week 4 Goals:
  - Begin creating exhibit 1 using previous data (no databasing)
  - Explore data base collecting process
  - Start interest page

Week 5 Goals:
  - Create second exhibit with databasing
  - Continue the interest page

Midterm Goal: 
  - Finish login and account configurations
  - Create interest board with recommendations
  - Have a functioning home page
  - Have at least two exhibits
Week 7 Goals:
  - Begin work on gift shop
  - Add another exhibit or two

Week 8 Goals:
  - Add shop feature of gift shop
  - Add another exhibit or two

Week 9 Goals:
  - Experiment with planetarium and botany
  - Testing to make sure everything works

Week 10 Goals:
  - Add cosmetics to exhibits
  - Work on search bars
  - Week 11 Goals:
  - Add cosmetics to homepage and login area

Final/N@tM Goal:
  - Add more exhibits
  - Have better cosmetics
  - Create carousel and gift shop
  - Add search bar
# Authors & Github IDs
NAME             | GITHUB ID |
-------------    | --------------- |
Crystal Widjaja  | crystalwidjaja  |
Ridhima Inukurti | ridhimainukurti |
Maggie Killada   | maggie3000 |
Sriya Chilla     | sriyachilla |

# Links
Project Plan: https://docs.google.com/document/d/1oF9n5UcXqyrZDL_TEkaHepAqPodVf1hqFacXWsT9auY/edit?usp=sharing 

Storyboard: https://docs.google.com/presentation/d/1s8BYup586gtJS0jcmAaMi93Vr8C7_bnCXn_vSK02BRc/edit?usp=sharing 

Easter Egg: http://104.63.255.249:8081/easteregg

