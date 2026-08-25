#Day 5: 30 Days Of Pyhton
empty = []

lst = ['l','m','n','o','p']

print(len(lst))

print(lst[0])
print(lst[2])
print(lst[4])

mixed_data_types = ['Amir',19,167,'Not married','Malaysia']
print(mixed_data_types)

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

print(it_companies)

print(len(it_companies))

print(it_companies[0])
print(it_companies[3])
print(it_companies[6])

it_companies[0] = 'Instagram'
print(it_companies)

it_companies.append('Meta')

it_companies.insert(3,'Facebook')

it_companies[2] = it_companies[2].upper()
print(it_companies)

it_companies = '#;'.join(it_companies)
print(it_companies)

print(it_companies.find('Amazon'))

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[:3])

print(it_companies[-3:])

print(it_companies[3])

del it_companies[0]
print(it_companies)

del it_companies[2]
print(it_companies)

del it_companies[-1]
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

front_end = ['HTML','CSS','JS','React','Redux']
back_end = ['Node','Express','MongoDB']
front_end.extend(back_end)
print(front_end)

full_stack = front_end
full_stack.append('Python')
full_stack.append('SQL')
print(full_stack)

#Exercie 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[-1]
median = len(ages)/2
median += 1
median = int(median)
print(ages[median])
sum = sum(ages)
avg = sum/len(ages)
print(avg)
range = max_age - min_age
print(range)
com = (min_age-avg) - (max_age-avg)
abs(com)
print(com)

countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cabo Verde',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombia',
    'Comoros',
    'Congo, Democratic Republic of the',
    'Congo, Republic of the',
    'Costa Rica',
    "Côte d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor-Leste)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Eswatini',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Montenegro',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'North Macedonia',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Palestine',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent and the Grenadines',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'South Sudan',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Sweden',
    'Switzerland',
    'Syria',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe'
];

mid = len(countries)/2
mid = int(mid)
print(countries[mid])

half1 = countries[0:mid]
half2 = countries[mid:0]

country = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *rest = country
print(china) 