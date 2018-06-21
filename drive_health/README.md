DRIVE HEALTH
===

Description
---
This tool requires the installation of smartmontools onto the OS itself.  
Once installed, installing pySMART vi pip will handle the use of smartctl.  
At the time of this writing, pySMART is 0.3, from June 11, 2015.  


NOTIFICATIONS
---
In order to receive email notification, or Telegram notifications, the  
variables will need to be updated.  

#### EMAIL
The email sender and recipeint are all that need to be changed.  
Due to the nature of the content sent, be sure to check the spam folder  
for the emails sent.  

Required fields to update:  
* sender
* receiver

#### TELEGRAM
Telegram bots are quick and easy to create. Check in with the Botfather  
for assistance; instructions here:  

https://core.telegram.org/bots

Required fields to update:  
* tg_token
* tg_chat_id


CAVEAT
---
The all_selftests() function returns None because the print statement is  
contained within the function, providing nothing back to the call itself.  
For this reason, there isn't a notification option set for the '-r' option.  

This tool **MUST** be used with sudo, in order to get drive data.  


Usage
---
### Help Menu

    usage: dhealth.py [options]

    SMART drive health monitor tool

    optional arguments:
    -h, --help       show this help message and exit
    -c               Check PASS/FAIL self-test status
    -i               Info for each drive
    -r               Results from self-tests
    -t {long,short}  Perform drive self-test
    --notify         Send email and Telegram alert


#### == CHECK DRIVE STATUS ==

    sudo dhealth.py -c

    sda: PASS
    sdb: PASS
    sdc: PASS
    sdd: PASS
    sde: PASS
    sdf: PASS


#### == DRIVE INFORMATION ==

    sudo dhealth.py -i

    {
        "sda":{
            "capacity":"1.00 TB",
            "check":"PASS",
            "firmware":"CC41",
            "model":"ST1000DX002-2DV162",
            "serial":"Z4YEZPGK"
        },
        "sdb":{
            "capacity":"4.00 TB",
            "check":"PASS",
            "firmware":"CC52",
            "model":"ST4000DM000-1F2168",
            "serial":"S3001JVR"
        },
        "sdc":{
            "capacity":"4.00 TB",
            "check":"PASS",
            "firmware":"CC52",
            "model":"ST4000DM000-1F2168",
            "serial":"W300LVX3"
        },
        "sdd":{
            "capacity":"4.00 TB",
            "check":"PASS",
            "firmware":"CC52",
            "model":"ST4000DM000-1F2168",
            "serial":"S3002XJN"
        },
        "sde":{
            "capacity":"10.0 TB",
            "check":"PASS",
            "firmware":"DN01",
            "model":"ST10000DM0004-1ZC101",
            "serial":"ZA225G60"
        },
        "sdf":{
            "capacity":"4.00 TB",
            "check":"PASS",
            "firmware":"0001",
            "model":"ST4000DM005-2DP166",
            "serial":"ZDH332H9"
        }
    }


#### == RESULTS FROM SELF-TESTS ==

    sudo dhealth.py -r

    1) sda
    2) sdb
    3) sdc
    4) sdd
    5) sde
    6) sdf
    A) ALL
    Q) Quit
    Select drive(s) to check: 5
    sde
    ID Test_Description Status                        Left Hours  1st_Error@LBA
    1 Short offline    Completed without error       00%  5691   -
    2 Short offline    Completed without error       00%  5589   -
    3 Conveyance offlineCompleted without error       00%  5503   -
    4 Extended offline Completed without error       00%  5503   -
    5 Short offline    Completed without error       00%  5477   -


#### == TEST THE DRIVE ==

    sudo dhealth.py -t short

    1) sda
    2) sdb
    3) sdc
    4) sdd
    5) sde
    6) sdf
    A) ALL
    Q) Quit
    Select drive(s) to test: 6
    sdf: Self-test started successfully


