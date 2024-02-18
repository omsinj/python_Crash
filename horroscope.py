from datetime import datetime

def get_horoscope(birthdate):
    try:
        # Parse the input birthdate string into a datetime object
        birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
        
        # Check for leap year
        if birthdate.year % 4 == 0 and (birthdate.year % 100 != 0 or birthdate.year % 400 == 0):
            leap_year = True
        else:
            leap_year = False
        
        # Define the date ranges for each zodiac sign
        zodiac_signs = [
            (datetime(birthdate.year, 3, 21), datetime(birthdate.year, 4, 19)),  # Aries
            (datetime(birthdate.year, 4, 20), datetime(birthdate.year, 5, 20)),  # Taurus
            (datetime(birthdate.year, 5, 21), datetime(birthdate.year, 6, 20)),  # Gemini
            (datetime(birthdate.year, 6, 21), datetime(birthdate.year, 7, 22)),  # Cancer
            (datetime(birthdate.year, 7, 23), datetime(birthdate.year, 8, 22)),  # Leo
            (datetime(birthdate.year, 8, 23), datetime(birthdate.year, 9, 22)),  # Virgo
            (datetime(birthdate.year, 9, 23), datetime(birthdate.year, 10, 22)),  # Libra
            (datetime(birthdate.year, 10, 23), datetime(birthdate.year, 11, 21)),  # Scorpio
            (datetime(birthdate.year, 11, 22), datetime(birthdate.year, 12, 21)),  # Sagittarius
            (datetime(birthdate.year, 12, 22), datetime(birthdate.year, 1, 19)),  # Capricorn
            (datetime(birthdate.year, 1, 20), datetime(birthdate.year, 2, 18)),  # Aquarius
            (datetime(birthdate.year, 2, 19), datetime(birthdate.year, 3, 20)),  # Pisces
        ]
        
        # Determine the zodiac sign based on the birthdate
        for sign, date_range in enumerate(zodiac_signs, start=1):
            if date_range[0] <= birthdate <= date_range[1]:
                return f'Your horoscope sign is {sign}'

        # Handle cases where birthdate is on the cusp of two signs
        if (birthdate.month == 3 and birthdate.day >= 20) or (birthdate.month == 4 and birthdate.day <= 19):
            return 'Your horoscope sign is on the cusp of Aries and Pisces'
        # Add similar checks for other sign cusps...

        return 'Unable to determine horoscope sign for the given birthdate'

    except ValueError:
        return 'Invalid date format. Please use the format YYYY-MM-DD'
    except Exception as e:
        return f'An error occurred: {str(e)}'

# Example usage:
birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
result = get_horoscope(birthdate_input)
print(result)
