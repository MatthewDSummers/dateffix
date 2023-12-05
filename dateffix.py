
from datetime import datetime

MONTHS = {
    "01":"January", "02":"February", "03":"March", "04":"April", 
    "05":"May", "06":"June", "07":"July", "08":"August", "09":"September",
    "10":"October", "11":"November", "12":"December"
}

# Return formatted dates
def dateffix(date_list, formatted=None, suffixed_only=False, no_times=False):
    if not isinstance(date_list, list):
        date_list = [date_list]

    formatted_dates = []

    for date_str in date_list:
        if not isinstance(date_str, str):
            raise ValueError("Date should be a string")

        the_date = date_str.strip()
        date_obj, has_time = validate_date(the_date)

    # get just the DAY portion, remove any leading 0's and replace
        the_day = date_obj.strftime("%d").lstrip("0")
    # do the same for the month and retrieve it from the MONTHS dictionary
        the_month = MONTHS[date_obj.strftime("%m")]
    # get just the YEAR portion
        the_year = date_obj.strftime("%Y")

    # Suffix is "th" if the DAY portion is 4 to 20, otherwise the modulus 10 will get just the number (in case of single digits) or the 2nd digit of the number (in case of double digit days),
    # then use it as the key to retrieve the desired suffix value from the created dictionary.
    # If the digit (key) is not present in the dict, it will use the default suffix "th".
        suffix = "th" if int(the_day) >= 4 and int(the_day) <= 20 else {1: "st", 2: "nd", 3: "rd"}.get((int(the_day) % 10), "th")

    # add the suffix to the day
        the_day += suffix

        if formatted and not suffixed_only:
            the_formatted_date = generate_custom_format(formatted, the_day, the_month, the_year)
        elif suffixed_only:
            the_formatted_date = the_day
        else:
            the_formatted_date = f"{the_month} {the_day}, {the_year}"

        if not no_times and has_time and not suffixed_only:
            time_portion = date_obj.strftime("%H" + has_time)
            the_formatted_date += " " + time_portion

        formatted_dates.append(the_formatted_date)
    return formatted_dates

# Generate custom format for returned strings
def generate_custom_format(format_str, the_day, the_month, the_year):
    formats = {
        # Month first
        "MDY": f"{the_month} {the_day} {the_year}",     #December 7th 2023
        "MD,Y": f"{the_month} {the_day}, {the_year}",   #December 7th, 2023

        # Day first 
        "DMY": f"{the_day} {the_month} {the_year}",     #7th December 2023
        "DM,Y": f"{the_day} {the_month}, {the_year}",   #7th December, 2023
        "D,MY": f"{the_day}, {the_month} {the_year}",   #7th, December 2023

        # Years first - month second
        "YDM": f"{the_year} {the_day} {the_month}",     #2023 7th December 
        "Y,DM": f"{the_year}, {the_day} {the_month}",   #2023, 7th December
        "YD,M": f"{the_year} {the_day}, {the_month}",   #2023 7th, December

        # Years first - day second
        "YMD": f"{the_year} {the_month} {the_day}",     #2023 December 7th
        "Y,MD": f"{the_year}, {the_month} {the_day}",   #2023, December 7th
        "YM,D": f"{the_year} {the_month}, {the_day}",   #2023 December, 7th
    }

    if format_str in formats:
        return formats[format_str]
    else:
        raise ValueError(f"Unsupported date format: {format_str}")

# Validate date strings
def validate_date(date_str):
    date_formats = [
        "%Y-%m-%d", # 2023-12-07
        "%Y/%m/%d", # 2023/12/07
        "%Y%m%d",   # 20231207
        "%m/%d/%Y", # 12/07/2023
        "%m-%d-%Y", # 12-07-2023
        "%d-%b-%Y", # 07-Dec-2023
        "%b %d, %Y", # Dec 07, 2023
        "%B %d, %Y", # December 07, 2023
        "%d %B %Y",  # 07 December 2023
        "%A, %d %B %Y", # Thursday, 07 December 2023
        "%a, %d %B %Y", # Thu, 07 December 2023
        # with times
        "%Y-%m-%d %H:%M:%S", # 2023-12-07 15:30:10
        "%a, %d %b %Y %H:%M:%S %z", #Thurs, 07 Dec 2023 15:30:10 +0000
        "%Y-%m-%dT%H:%M:%S.%fZ",  # 2023-12-07T15:30:15.123456Z
    ]

    for format_str in date_formats:
        try:
            date_obj = datetime.strptime(date_str, format_str)
            has_time = ("%H" in format_str) and ("%M" in format_str)
            if has_time:
                has_time = format_str.split("%H")[1]
            return date_obj, has_time
        except ValueError:
            pass

    raise ValueError(f"Date string '{date_str}' not in recognized formats.")

######
# EXAMPLE USAGE:
######

if __name__ == "__main__":

### LIST OF DATES 
    date_list = ["2023-12-07", "2023/08/30", "2023/7/3", "20231221", "01/25/1809", "02-21-2023", "30-Aug-2023", "Sep 23, 2023", "April 20, 2023", "21 May 2020", "Fri, 22 December 2023", "2023-10-07 15:30:10", "Sat, 9 Dec 2023 15:30:10 +0000", "1909-11-12T15:30:15.123456Z"]
    print("Original Dates:", date_list, "\n")
    # output:
    #     Original Dates: ['2023-12-07', '2023/08/30', '2023/7/3', '20231221', '01/25/1809', '02-21-2023', '30-Aug-2023', 'Sep 23, 2023', 'April 20, 2023', '21 May 2020', 'Fri, 22 December 2023', '2023-10-07 15:30:10', 'Sat, 9 Dec 2023 15:30:10 +0000', '1909-11-12T15:30:15.123456Z'] 


### GET THE DATES WITH PROPER SUFFIXES
    formatted_dates = dateffix(date_list)
    print("Standard formatted dates:")

    for formatted_date in formatted_dates:
        print(formatted_date)
        # output:
            # Standard formatted dates:
            # December 7th, 2023
            # August 30th, 2023
            # July 3rd, 2023
            # December 21st, 2023
            # January 25th, 1809
            # February 21st, 2023
            # August 30th, 2023
            # September 23rd, 2023
            # April 20th, 2023
            # May 21st, 2020
            # December 22nd, 2023
            # October 7th, 2023 15:30:10
            # December 9th, 2023 15:30:10 +0000
            # November 12th, 1909 15:30:15.123456Z



### CUSTOM FORMAT
    custom_formatted_dates = dateffix(date_list, "YMD")
    # Format options:
        # MDY
        # MD,Y
        # DMY
        # DM,Y
        # D,MY
        # YDM
        # Y,DM
        # YD,M
        # YMD
        # Y,MD
        # YM,D
    print("\nCustom formatted dates example (YMD): ")

    for formatted_date in custom_formatted_dates:
        print(formatted_date)

        # output:
            # Custom formatted dates example (YMD): 
            # 2023 December 7th
            # 2023 August 30th
            # 2023 July 3rd
            # 2023 December 21st
            # 1809 January 25th
            # 2023 February 21st
            # 2023 August 30th
            # 2023 September 23rd
            # 2023 April 20th
            # 2020 May 21st
            # 2023 December 22nd
            # 2023 October 7th 15:30:10
            # 2023 December 9th 15:30:10 +0000
            # 1909 November 12th 15:30:15.123456Z

### SUFFIXES ONLY
    suffix_only_from_dates = dateffix(date_list, suffixed_only=True)
    print("\nSuffixes only example: ")

    for formatted_date in suffix_only_from_dates:
        print(formatted_date)

        # output:
            # Suffixes only example: 
            # 7th
            # 30th
            # 3rd
            # 21st
            # 25th
            # 21st
            # 30th
            # 23rd
            # 20th
            # 21st
            # 22nd
            # 7th
            # 9th
            # 12th

### NO TIMES
    no_time_formatted_dates = dateffix(date_list, no_times=True)
    print("\nDates returned without timestamps: ")

    for formatted_date in no_time_formatted_dates:
        print(formatted_date)

    # output: 
        # Dates returned without timestamps:
        # December 7th, 2023
        # August 30th, 2023
        # July 3rd, 2023
        # December 21st, 2023
        # January 25th, 1809
        # February 21st, 2023
        # August 30th, 2023
        # September 23rd, 2023
        # April 20th, 2023
        # May 21st, 2020
        # December 22nd, 2023
        # October 7th, 2023
        # December 9th, 2023
        # November 12th, 1909