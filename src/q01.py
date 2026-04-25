HAAB_MONTHS = [
    'pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen',
    'yax', 'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu', 'uayet',
]

TZOLKIN_NAMES = [
    'imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat',
    'mulok', 'ok', 'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban',
    'eznab', 'canac', 'ahau',
]


def solve(haab_date: str) -> str:
    parts = haab_date.split()
    if len(parts) != 3:
        return ""

    try:
        day = int(parts[0].rstrip('.'))
        year = int(parts[2])
    except ValueError:
        return ""

    month = parts[1]

    if year < 0 or year >= 5000:
        return ""

    if month not in HAAB_MONTHS:
        return ""

    month_index = HAAB_MONTHS.index(month)
    max_day = 4 if month_index == 18 else 19

    if day < 0 or day > max_day:
        return ""

    absolute = year * 365 + month_index * 20 + day
    tzolkin_number = absolute % 13 + 1
    tzolkin_name = TZOLKIN_NAMES[absolute % 20]
    tzolkin_year = absolute // 260

    return f"{tzolkin_number} {tzolkin_name} {tzolkin_year}"
