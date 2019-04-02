# Level3


**URL: http://natas3.natas.labs.overthewire.org/**

#### Creds for level 3

**natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14**

## Solution


by viewing the page source we notice the following comment: 


> <!-- No more information leaks!! Not even Google will find it this time... -->

`Not even Google will find it`, means there something in the robots.txt file 

by going to  [robots.txt](http://natas3.natas.labs.overthewire.org/robots.txt) we can see :  
Disallow: /s3cr3t/

by visiting the folder we can see a users.txt file with the user and password for `level4`.

**natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ**


### About robots.txt file

> Robots.txt is a text file webmasters create to instruct web robots (typically search engine robots) how to crawl pages on their website. The robots.txt file is part of the the robots exclusion protocol (REP), a group of web standards that regulate how robots crawl the web, access and index content, and serve that content up to users. The REP also includes directives like meta robots, as well as page-, subdirectory-, or site-wide instructions for how search engines should treat links (such as “follow” or “nofollow”).In practice, robots.txt files indicate whether certain user agents (web-crawling software) can or cannot crawl parts of a website. These crawl instructions are specified by “disallowing” or “allowing” the behavior of certain (or all) user agents.

### NOTE

robots.txt is a publically available file, which means anyone can see what sections of your server you don't want robots to use.



