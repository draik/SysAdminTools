MYJIRA
===

Description
---
This script connects to Jira, using the REST API.  
The creation and updating of a Jira issue is faster  
through the REST API, than through the web interface.  


Usage
---
### Help Menu

    usage: myjira [options]  
    
    Login options are 'basic' or 'oauth', storing your credentials  
    in the 'jira.cfg' configuration file.  
    
    NOTICE: storing your Jira password (plaintext) is OPTIONAL  
    
    optional arguments:  
      -h, --help          show this help message and exit  
      -a ASSIGNEE         Assign Jira issue to a user  
      -c                  Comment on the Jira issue  
      -i {epic,task}      Issue type as Epic or Task  
      -j JIRA             Specify the Jira issue  
      -l [{basic,oauth}]  Update login method between basic or oauth  
      -n NAME             Specify Epic Name when creating Epic issue  
      -p PARENT           Parent Jira issue for creating sub-task issue  
      -q QUEUE            Specify the Jira project  
      -s [ID]             Set the Jira issue status  
      -t TITLE            Specify the Jira issue title  
      --man               Print the Help menu with examples  


### Man Page Examples

#### == LOGIN ==  

Upate login credentials, and authentication method  
(basic for un/pw, oauth for tokens)  

    myjira --login basic  

 -or-  

    myjira --login oauth  



#### == JIRA ISSUE INFO ==  

View Jira issue information  

    myjira -j TEST-1  

    URL: http://your.jiraserver.com/browse/TEST-1  
    Title: My First Automated Jira Issue  
    Reporter: Draik  
    Assignee: None  
    Status: Done  



#### == ISSUE CREATION ==  

Create a task in the default queue  

    myjira -t 'Epilogue Sample'  

    New task issue created successfully: TEST-10  
    URL: http://your.jiraserver.com/browse/TEST-10  


Specify issue type, project queue, title, and assignee  

    myjira -i epic -q TEST -t 'Title Here' -a bsmith  


Create a sub-task issue  

    myjira -p TEST-3 -t 'Sub-Task Title Here'  



#### == STATUS CHANGE ==  

Change issue status between 'open', 'in progress', 'done', etc  

    myjira -j TEST-2 -s  

    Current status: DONE  

     ID - Status  
     31 - In Progress  
     41 - Done  
     51 - Open  

    Enter status ID: <user_input>  



Change issue by specifying the status ID  

    myjira -j TEST-2 -s 41  

    TEST-2 changed to DONE  



#### == COMMENTING ==  

Add a comment to the issue; press [CTRL+d] when done  

    myjira -j TEST-2 -c  



#### == ASSIGNING JIRA ISSUE ==

Update Jira issue with assignee

    myjira -j TEST2 -a bsmith


