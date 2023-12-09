import requests
import time

def hlrLookup(argv):
    try:
        # Set your HLR-lookups API username and password here
        username = "foravay-api-2e744af64e4e"
        passwd = "26jb-mhKq-Qd2W-Mv2!-4zFw-GmZ!"

        api_url = "https://www.hlr-lookups.com/api/?action=submitSyncLookupRequest"

        params = {
            'msisdn': argv,
            'username': username,
            'password': passwd
        }

        response_imsi = requests.get(api_url, params=params)
        response_data = response_imsi.json()  # Get the entire response data

        print("[*] Response from HLR-lookups API:")
        print(response_data)

        results = response_data.get('results', [])
        if results:
            print("[*] Checking for Home Routing/SMS FW...")

            mccmnc = results[0].get('mccmnc', '')
            msin = results[0].get('msin', '')

            if msin:
                imsi_ver = requests.get(api_url, params=params)
                msin_ver = imsi_ver.json()['results'][0]['msin']

                if msin == msin_ver:
                    print("[+] Target IMSI:", mccmnc + msin)
                else:
                    print("[!] Possible Implementation of Home Routing Detected: IMSI is Scrambled",
                          f"{{{mccmnc + msin}, {mccmnc + msin_ver}}}")

            else:
                print("[-] Target IMSI is Null")

            msc = results[0].get('servingmsc', '')
            hlr = results[0].get('servinghlr', '')
            network_name = results[0].get('originalnetworkname', '')

            if msc:
                msc_ver = requests.get(api_url, params=params)
                msc_ver = msc_ver.json()['results'][0]['servingmsc']

                if msc == msc_ver:
                    print("[+] Target Serving MSC:", msc)
                else:
                    print("[!] Different MSC GT returned: Further Scanning Required",
                          f"{{{msc}, {msc_ver}}}")

            if hlr:
                hlr_ver = requests.get(api_url, params=params)
                hlr_ver = hlr_ver.json()['results'][0]['servinghlr']

                if hlr == hlr_ver:
                    print("[+] Target's HLR:", hlr)
                else:
                    print("[!] Different HLR GT returned: Further Scanning Required",
                          f"{{{hlr}, {hlr_ver}}}")

            print("[+] Target's Operator:", network_name)
            print("[*] Information Retrieved at", time.asctime())

        else:
            print("[-] No results returned from the HLR-lookups API.")

    except Exception as e:
        print("Error:", e)

# Example usage:
argv = input("Enter the MSISDN to look up: ")
hlrLookup(argv)
