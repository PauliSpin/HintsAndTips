import holidays
import datetime

# for date in holidays.UnitedKingdom(years=2021).items():
# for date in holidays.India(years=2021).items():
for date in holidays.UnitedStates(years=2021).items():
    print(date)
