import re


all_passports = 0
before_valid = 0
valid_passports = 0
passports = []
with open('../../passports.txt') as fh:
    dirty_passports = fh.read().split('\n\n')


def check_height(b):
    match = re.match(r'^(\d+)(cm|in)$', b)
    if match:
        if match[2] == "cm":
            return 150 <= int(match[1]) <= 193
        elif match[2] == "in":
            return 59 <= int(match[1]) <= 76

    return False


required_keywords = {
    'byr': lambda b: 1920 <= int(b) <= 2002,
    'iyr': lambda b: 2010 <= int(b) <= 2020,
    'eyr': lambda b: 2020 <= int(b) <= 2030,
    'hgt': lambda b: check_height(b),
    'hcl': lambda b: re.match(r'^#[0-9a-f]{6}$', b),
    'ecl': lambda b: b in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda b: re.match(r'^\d{9}$', b)
}

for passport in dirty_passports:
    all_passports += 1

    attributes = passport.replace('\n', ' ').split(' ')
    while '' in attributes:
        attributes.remove('')

    passport_dict = dict(attribute.split(':') for attribute in attributes)

    if all(keyword in passport_dict for keyword in required_keywords):
        before_valid += 1
        is_valid = True
        for keyword in required_keywords:
            lambda_function = required_keywords[keyword]
            if not lambda_function(passport_dict[keyword]):
                is_valid = False

        if is_valid:
            valid_passports += 1

print(f"All passports: {all_passports}")
print(f"Before valid passports: {before_valid}")
print(f"Valid passports: {valid_passports}")
