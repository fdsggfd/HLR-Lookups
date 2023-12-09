# HLR-Lookups FIXED AND UPDATED 2023
This script is used to automate hlr-lookup process using the api from hlr-lookups and extract important data from it like the IMSI of the subscriber, which country is he/she roaming in that is provided in the current MSC GT along with the HLR GT, these information could be useful to conduct further attacks... using sigploit.

Must be noted that those public services like HLR-Lookups are using one variant of SS7 messages that is most probably SendRoutingInformationForSM(SRISM) that is used to locate the target location before sending SMS, some operators implement an SMS Firewall/proxy that scarambles the IMSI and/or HLR and returns back a fake MSC. To overcome this kind of protection its always recommended to perform TCAP scanning on the range of GT as the implementation of such scrambling is very weak and predicatedble. Thus its recommended to run the script twice for each msisdns to make sure that the returned information is the same and is not changing per request

This script currently works for 
-Qtel 

-Zain KW

-Etisalat UAE

-DU UAE

-jawal palestine 

-India (Airtel, Reliance, Vodafone)

-Russia (MTS)


This is not by any means a comprehensive way to gather info and shouldnt be the only way to gather information

The script also could detect if home routing (SMS FW) is being implemented

# How does it work
1- First you need to create an account on HLR-Lookups which will give you free credit at the begnning along with the API username and passowrds that will be used in the script

2- run the script as the below

Usage: ./hlr-lookup.py MSISDN
  
Example: ./hlr-lookup.py +20123456789

Please note: You may need to change the route (route="") if the results are uncertain.
