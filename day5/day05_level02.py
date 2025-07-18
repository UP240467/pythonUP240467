#Exercise 1 (Level 2)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print('La minima edad es:',ages[0])
print('La maxima edad es:',ages[-1])

#Exercise 2 (Level 2 )

min_age= ages[0]
max_age= ages[-1]

ages.append(min_age)
ages.append(max_age)

print('La lista actualizada es:',ages)

#Exercise 3 (Level 2)

middle_ages = len(ages) // 2
if (len(ages)%2 != 0 ):
    print('El elemento de enmedio es: ',ages[middle_ages])
else:
    print('Los elementos de enmedio son: ',ages[middle_ages -1: middle_ages+1 ])

#Exercise 4 (Level 2)

promedio = sum(ages) / len(ages)

print('El promedio de los valores de la lista es: ', promedio)

#Exercise 5 (Level 2)

rango = max_age - min_age
print('El rango de edades es: ',rango)

#Exercise 6 (Level 2)

min_diferencia = abs(min_age-promedio)
max_diferencia = abs(max_age-promedio)

print('Minimo - promedio :',min_diferencia)
print('Maximo - promedio :',max_diferencia)
if (min_diferencia>max_diferencia):
    print('Min - el promedio es mayor')
elif (max_diferencia<min_diferencia):
    print(' Max - el promedio es mayor ')
else:
    print('Ambos son iguales')

#Exercise 7 (Level 2)
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
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
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
  'Macedonia',
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
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
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
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
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
  'Zimbabwe',
];

middle_contries = len(countries)//2 
if (len(countries)%2 != 0 ):
    print('El elemento de enmedio es: ',countries[middle_contries])
else:
    print('Los elementos de enmedio son: ',countries[middle_contries -1: middle_contries+1 ])

#Exercise 8 (Level 2)

elementos = len(countries)
mid = (elementos//2) + (elementos%2)

primera_parte = countries[:mid]
segunda_parte = countries[mid:]

print(primera_parte)
print(segunda_parte)

#Exercise 9 (Level 2 )

countries2 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

primero , segundo , tercero, * resto = countries2

print('El primer pais es: ',primero)
print('El segundo de los paises es:',segundo)
print('El tercero de los paieses es: ',tercero)
print('El resto de los paises es:', resto)
