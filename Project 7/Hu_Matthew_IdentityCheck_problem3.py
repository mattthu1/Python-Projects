def validate_SSN():
    ssn = input("What is your SSN? ")
    while True:
        # Check for alphabetical characters and for missing hyphens
        if not ssn.replace("-", "").isdigit() and ssn.count("-") != 2:
            print("Invalid SSN, try again! Only digits allowed. Missing hyphen(s)")
        else:
            if not ssn.replace("-", "").isdigit():
                print("Invalid SSN, try again! Only digits allowed.")
            elif ssn.count("-") != 2:
                print("Invalid SSN, try again! Missing hyphen(s).")
            else:
               
               
                # Split ssn into area, group, and serial numbers
                area, group, serial = ssn.split("-")


                # Check area number
                if area in ["000", "666"] or 900 <= int(area) <= 999:
                    print("Invalid SSN, try again! Area number violated.")


                # Check group number
                elif int(area) <= 499 and int(group) % 2 != 0:
                    print("Invalid SSN, try again! Group number violated.")

                elif 500 <= int(area) <= 899 and int(group) % 2 != 1:
                    print("Invalid SSN, try again! Group number violated.")

                else:
                    print("Valid SSN.")
                    return
                

        ssn = input("What is your SSN? ")
        

validate_SSN()
    