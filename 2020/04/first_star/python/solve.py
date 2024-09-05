required_keywords = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
]

valid_passports = 0
passports = []
with open('../../passports.txt') as fh:
    dirty_passports = fh.read().split('\n\n')

for passport in dirty_passports:
    attributes = passport.replace('\n', ' ').split(' ')
    while '' in attributes:
        attributes.remove('')

    passport_dict = dict(attribute.split(':') for attribute in attributes)

    if all(keyword in passport_dict for keyword in required_keywords):
        valid_passports += 1

print(f"Valid passports: {valid_passports}")
