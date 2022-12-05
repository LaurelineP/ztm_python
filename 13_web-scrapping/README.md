# 12 - Web Scrapping
Web Scrapping is the ability to get information from web pages programmatically.
A Website provides a `robots.txt` file expressing what endpoints are scrappable or not.
While doing this automation of getting data from website it is highly recommended to follow
what that file is stating: accessing endpoints allowed


As a developer, we match the User-Agent: * that we can dissociate from others ( Googlebot for instance )


BeautifulSoup: https://pypi.org/project/beautifulsoup4/
Libreary allowing to access the DOM values

Scrappy framework ( more powerfull than BeautifulSoup ): https://scrapy.org/
Great for bigger websites.