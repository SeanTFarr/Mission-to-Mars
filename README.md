# Mission-to-Mars
## Overview of Analysis
#### Purpose: A colleague of mine is interested in information about Mars, but she didn't like having to do a costant search across several websites to gather her information. I was asked if it were possible to do this with the click of a button.

#### Resources used:
- Python
- Beautiful Soup
- Splinter
- Flask
- MongoDB
- HTML
- Bootstrap




## Results
After researching which websites we needed to scrape data from, the sites were inspected to determine what data was needed and where to find it inside the HTML code.
<img src=Resources\inspect.png>

Then using Beautiful Soup and Splinter dependecies in Python, we were able to scrape the data that we needed

<img src=Resources\BS_Splinter.png>

Using that framework, a sraping.py file was created to run the functions to scrape the websites. An app.py file was created to call on Flask to execute the code, send the data to a Mongo No SQL DataBase, and update our new page with the latest data.
<img src=Resources\app.png>

The end product, as seen below, was organized using Bootstrap to get the layouts desired for the data we collected.



<img src=Resources\M2M_page.png>
<img src=Resources\M2M_hemis.png>


## Summary
Though there is a lot of initial work to get the information and display it as we have, it is a rewarding process once you can sit back and just click on to the next bit of data instead of spending so much time bouncing from one site to the next every time you would like an update.