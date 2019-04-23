MANGA UPDATER:

    - For personal practice and use
    - Using python
    - Self-starter project, learning to use API's and python pkg Selenium
    - Using Google Chrome
    - Will use www.mangadex.org as my preferred manga site
    - Program will be connected with Google Drive and Sheets API
    - It will update my sheets file on Google Drive with wanted info after feeding the sheet's data to the script
    - Feeds Manga Name
    - Retrieve Directory URL(respective name), Latest Chapter, and Chapter URL and populates the cells with info.

PLEASE NOTE:
    
    - You will need to have chromedriver downloaded with it's path
    - Install python package: Selenium
    - Will need to make Gmail less secure 
        - DISCLAIMER: DO AT YOUR OWN RISK!
    
What needs to be done(future):

    - Headless automation.
    - Need to learn how to automate a script to run daily to check for new chapters
        - Currently runs fine with head, but not headless
    - In lieu with point above, send e-mail notifications about new chapters

Project Timeline:
    - On a long hold due to copious amounts of schoolwork.
    - 2.15.19
        - Created email_alert.py
            - Connected to GMail servers to send emails when script is finished running
        - Created config.py
            - Holds user's credentials of e-mails
        - Attempt to make headless automation

    - 2.14.19 (Happy Valentine's Day)
        - Created update_mangas.py
            - Incorporated Google Drive and Sheets API
        - Created manga_bot.py
            - Uses selenium package
    
