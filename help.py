"""
Includes the help page of the program having information about the different flags and options.
Most importantly includes examples of how the different flags are going to be used.  This page
is going to be implemented iteratively i.e when a new feature is implemented this page is updated
to include info about it.
"""


# Prints help into screen.
def help():
    print("""
Please refer to 'Issues' section in GitHub for any problems you may have.
           
-- [ Options for Help & Symbols Explained ] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =============================================
help                | Prints help on screen                             | Intel-One >> help              
'|' symbol          | Means 'or'                                        | Intel-One >> click 1 | 2 means click 1 or 2  
'-' symbol          | Used for the short flag                           | Intel-One >> john smith -g                   
'--' symbol         | Used for the long flag                            | Intel-One >> john smith --google             
           
           
-- [ ALL in ONE Options ] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =============================================
-c, --company       | Executes all available searches for companies     | Intel-One >> glovdi -c | --company       
-d, --domain        | Executes all available searches for domains       | Intel-One >> glovdi.com -d | --domain
-i, --individual    | Executes all available searches for individuals   | Intel-One >> john smith -i | --individual
-i and -l           | As above including location of an individual      | Intel-One >> john smith -i madrid -l
-e, --email         | Performs all possible searches using an email     | Intel-One >> jsmith@email.com -e | --email

-- Note: The 2 following flags below are executed whenever the above ALL in ONE flags are executed. --  
-sm, --socialMedia  | Executes all available searches in social media   | Intel-One >> john smith -sm | --socialMedia
-s, --search        | Executes all available searches in search engines | Intel-One >> glovdi -s | --search

           
-- [ Options for Social Media ] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =============================================
-rts, --rtsearch    | Returns real time social media search results     | Intel-One >> john smith -rts | --rtsearch  
-fb, --facebook     | Performs facebook search through google           | Intel-One >> john smith -fb | --facebook     
-ln, --linkedin     | Performs linkedin search through google           | Intel-One >> john smith -ln | --linkedin     
-tw, --twitter      | Twitter search plus retrieves tweets and analytics| Intel-One >> john smith -tw | --twitter      
-in, --instagram    | Performs instagram search, posts and analytics    | Intel-One >> john smith -in | --instagram
-pn, --pinterest    | Performs pinterest search through google          | Intel-One >> john smith -pn | --pinterest
-yt, --youtube      | Performs search in youtube for username           | Intel-One >> john smith -yt | --youtube
-evs, --extraVid    | Perfroms further search in multiple video engines | Intel-One >> john smith -evs | --extraVid
-tb, --tumblr       | Performs tumblr search through google             | Intel-One >> john smith -tb | --tumblr    
-re, --redit        | Performs reddit search and posts search           | Intel-One >> john smith -re | --reddit
-ure, --userReddit  | Provides insights and statistics on reddit user   | Intel-One >> john smith -ure | --userReddit
-bl, --blogs        | Searches in blogs about target keyword            | Intel-One >> john smith -bl | --blogs  
-cd ,--code         | Performs github & 'nerdy data' search on repos    | Intel-One >> setoolkit -cd | --code
           
           
-- [ Options for Search Engines ] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =============================================
-g, --google        | Performs normal google search                     | Intel-One >> john smith -g | --google      
-ddg, --ddGo        | Performs search in duck duck go search engine     | Intel-One >> john smith -ddg | --ddGo
-bd, --baidu        | Performs search in chinese engine baidu           | Intel-One >> john smith -bd | --baidu
-bg, --bing         | Performs search in bing search engine             | Intel-One >> john smith -bg | --bing
-qw, --qwant        | Performs search in qwant search engine            | Intel-One >> john smith -qw | --qwant
-km, --keyword      | Performs keyword matching search on given keyword | Intel-One >> john smith -km | --keyword
-cl, --cluster      | Performs clustering search for query              | Intel-One >> john smith -cl | --cluster 
-ex, --exciteNews   | Performs search about recent news on search engine| Intel-One >> john smith -ex | --exciteNews
-oa, --oldArticles  | Performs search about very old posts about query  | Intel-One >> john smith -oa | --oldArticles
-ev, --emailValid   | Performs email validity search for target mail    | Intel-One >> jsmith@email.com -ev | --emailValid
-rss, --rssFeeds    | Performs RSS search in feeds on target keyword    | Intel-One >> john smith -rss | --rssFeeds


-- [ Options for People Search Engines ] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =============================================      
-p, --people        | Provides links on multiple people search engines  | Intel-One >> john smith -p | --people          
-p and -l           | Performs specific pipl using with location        | Intel-One >> john smith -p madrid -l         
           
           
-- [ Options for Companies ] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =============================================       
-cs, --compSearch   | Performs search in multiple companies websites    | Intel-One >> glovdi -cs | compSearch             
-are, --reports     | Provides 2 links with annual reports of companies | Intel-One >> glovdi -are | --reports
-cef, --emailFormat | Returns the email format of the company searched  | Intel-One >> glovdi -cef | --emailFormat
           
                      
-- [ Options for Domains ] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =============================================
-wh, --whois        | Performs whois search in the target domain        | Intel-One >> glovdi.com -wh | --whois
-dns, --dnsLookup   | Performs a DNS lookup about target domain         | Intel-One >> glovdi.com -dns | --dnsLookup     
-sc, --scan         | Performs a vulnerability scan using asafaweb site | Intel-One >> glovdi.com -sc | --scan
-ar, --archive      | Performs search for past versions of website      | Intel-One >> glovdi.com -ar | --arch
-bw, --builtWith    | Shows with which tools and tech the site is built | Intel-One >> glovdi.com -bw | --builtWith
-rb, --robots       | Provides the link including the robots.txt file   | Intel-One >> glovdi.com -rb | --robots     
           
           
-- [ Other Options ] --
           
Options Short/Long  |  Description                                      |  Example                                 
=================== + ================================================= + =============================================
-sh, --shodan       | Performs shodan search for given keyword          | Intel-One >> zanussi -sh | --shodan          

""")
