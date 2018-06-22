DRIVE HEALTH
===

Description
---
This tool provides options for the pySMART wrapper of smartmontools.  
It requires the installation of smartmontools onto the OS itself, before  
it can be used by this tool.  

Installation varies by OS, but ultimately one of the following:  

* `sudo apt install smartmontools`
* `sudo yum install smartmontools`
* Download [smartmontools](https://www.smartmontools.org)


CAVEAT
---
This tool **MUST** be used with sudo, in order to get drive data.  


pySMART 0.4
---
pySMART 0.3 was forked, then updated to better handle the `None` return  
for the all_selftest() function. This updated version handles the output  
as a string, which lends itself to data manipulation.  


NOTIFICATIONS
---
In order to receive email notification, or Telegram notifications, the  
variables will need to be updated.  

#### EMAIL
The email sender and recipeint are all that need to be changed.  
Due to the content sent, be sure to check the spam folder for the emails sent.  
The email notification is the same as the output from the tool.  

Required fields to update:  
* sender
* receiver

#### TELEGRAM
Telegram bots are quick and easy to create. To ensure notifications are not  
flagged for spamming, the output may be altered or broken into smaller  
messages. See samples below for further details.  

Check in with the Botfather for bot creation assistance; instructions here:  

https://core.telegram.org/bots

Required fields to update:  
* tg_token
* tg_chat_id


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

##### Telegram Notification Sample
Same output as above is provided in a single message  

    Drive Check
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

##### Telegram Notification Sample
One message received per drive  

    Drive Info sda
    model: ST1000DX002-2DV162
    firmware: CC41
    capacity: 1.00 TB
    check: PASS
    serial: Z4YEZPGK


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

##### Telegram Notification Sample
One message per drive, contains drive name, header, and latest test result  

    sde
    ID Test_Description Status                    Left Hours  1st_Error@LBA
    1 Short offline     Completed without error    00%  5691   -


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


