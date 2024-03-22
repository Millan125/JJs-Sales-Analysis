def do_rwr(year):

    weeks_for_long_years = list(range(1,54))
    weeks_for_short_years = list(range(1,53))
    long_years = ['2005', '2011', '2016', '2021']
    

#is requested year long or short
    if str(year) in long_years:
        long_year = True
    else:
        long_year = False

#long year checks weeks are 1-53 and sets weekrange
    if long_year:

        first_week = input("what's the first week in your range? (select 1-53)")
        last_week = input("What's the last week in your range?(select 1-53)")
        
        if int(first_week) not in weeks_for_long_years:
            return do_rwr()
        elif int(last_week) not in weeks_for_long_years:
            return do_rwr()
        else:
            week_range = list(range(int(first_week), int(last_week) + 1))

#short year checks weeks are 1-52 and sets weekrange        
    elif long_year == False:

        first_week = input("what's the first week in your range? (select 1-52)")
        last_week = input("What's the last week in your range?(select 1-52)")
        
        if int(first_week) not in weeks_for_short_years:
            return do_rwr()
        elif int(last_week) not in weeks_for_short_years:
            return do_rwr()
        else:
            week_range = list(range(int(first_week), int(last_week) + 1))

    return week_range


if __name__ == "__main__":
    yeard = input("year?")
    do_rwr(yeard)
