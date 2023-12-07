# dateffix

### EXPLANATION
**dateffix adds the proper suffix(es) to the day(s) in a list of date / datetime strings or to a single date / datetime string**

### BEHAVIOR
1. Accepts single date and/or datetime string or list thereof
2. With no arguments, it will return MonthName DD(suffix), YYYY

### EXAMPLE INPUT
```python
    date_list = ["2023-12-07", "2023/08/30", "2023/7/3", "20231221", "01/25/1809", "02-21-2023", "30-Aug-2023", "Sep 23, 2023", "April 20, 2023", "21 May 2020", "Fri, 22 December 2023", "2023-10-07 15:30:10", "Sat, 9 Dec 2023 15:30:10 +0000", "1909-11-12T15:30:15.123456Z"]
```

### OPTIONS
1. **Custom Format:**
    - Format the returned dates by passing `formatted=OPTION`:
    ```python
        dateffix(date_list, formatted="YMD")
    ```
    - Format options:
        - `MDY`
        - `MD,Y`
        - `DMY`
        - `DM,Y`
        - `D,MY`
        - `YDM`
        - `Y,DM`
        - `YD,M`
        - `YMD`
        - `Y,MD`
        - `YM,D`
    
2. **Suffix only:**
    - Return only the day portion(s) with the proper suffix(es) appended
    ```python
        dateffix(date_list, suffixed_only=True)
    ```

3. **Remove timestamps:**
    - Return the properly suffixed date(s) without timestamps
    ```python
        dateffix(date_list, no_times=True)
    ```

### Supplimentary Functions
1. **generate_custom_format**
    - EXPLANATION:
        - Re-organizes the returned date format according to custom input

    - POSITIONAL ARGUMENTS:
        - format_str: e.g. "YMD"
        - the_day: Day portion of date
        - the_month: Month portion of date
        - the_year: Year portion of date

    - RETURNS:
        - type: string
        - Re-formatted date / datetime string

2. **validate_date**
    - EXPLANATION:
        - Ensures we have a valid date and checks if it has a timestamp

    - POSITIONAL ARGUMENT:
        - date_str: the date / datetime string

    - RETURNS:
        - type: datetime object / string
        - Returns datetime object or datetime, timestamp string if it has a timestamp