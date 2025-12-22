# Data Dictionary

## Variable Categories

- Target: life_expectancy
- Identifier: year, country
- Demographic: population, infant mortality, adult mortality, under-5 deaths
- Health outcomes & burden: HIV/AIDS deaths, measles cases, BMI, thinness prevalence
- Health system & interventions: health expenditure, immunization coverage
- Economic & development: GDP, income composition, schooling years
- Behavioral risk factors: alcohol consumption
- Country classification: development status

## Target variable

| Variable          | Description                                             |
|-------------------|---------------------------------------------------------|
| life_expectancy   | Average number of years a newborn is expected to live   |

## Identifier variables

| Variable    | Description                                |
|-------------|--------------------------------------------|
| year        | The year in which the data was collected   |
| country     | Country name                               |

## Demographic variables

| Variable          | Description                                                        |
|-------------------|--------------------------------------------------------------------|
| population        | Total population of a country                                      |
| adult mortality   | Adult mortality rate per 1,000 persons                             |
| infant deaths     | Infant mortality rate (deaths per 1,000 live births)               |
| under-five deaths | Number of deaths of children under 5 years of age per 1,000 births |

**Notes**
- Adult Mortality: recorded for both sexes; probability of death between ages 15 and 60 per 1,000 persons.

## Health outcomes & burden variables

| Variable             | Description                                               |
|----------------------|-----------------------------------------------------------|
| BMI                  | Average body mass index (BMI) of the entire population    |
| Measles              | Number of reported measles cases per 1,000 people         |
| HIV/AIDS             | Number of HIV/AIDS-related deaths among children          |
| thinness 1-19 years  | Prevalence of thinness among children and adolescents (%) |
| thinness 5-9  years  | Prevalence of thinness among children, 5-9 (%)            |

**Notes**
- HIV/AIDS: number of recorded deaths among children aged 0–4 per 1,000 live births
- thinness 1-19 years: percentage of thinness among children and adolescents aged 10 to 19
- thinness 5-9 years: percentage of thinness among children between aged 5 to 9

## Health system & interventions variables

| Variable            | Description                                                       |
|---------------------|-------------------------------------------------------------------|
| Total expenditure   | Government expenditure on health as a % of total govt expenditure |
| health expenditure  | Expenditure on health as a percentage of GDP (%)                  |
| Hepatitis B         | Percentage of children vaccinated against hepatitis B (HepB)      |
| Polio               | Percentage of children vaccinated against poliomyelitis (Pol3)    |
| Diphtheria          | Percentage of one-year-old children vaccinated against (DTP3)     |

**Notes:**
- Hepatitis B: measured among one-year-old children
- Polio: measured among one-year-old children
- Diphtheria: measured among one-year-old children vaccinated against diphtheria, tetanus and whooping cough (DTP3)

## Economic and development variables

| Variable                        | Description                                            |
|---------------------------------|--------------------------------------------------------|
| GDP                             | Gross domestic product per capita in US dollars ($)    |
| Income composition of resources | Human Development Index in terms of income composition |
| Schooling                       | Number of years of education                           |

**Notes**
- Income composition of resources: index on a scale from 0 to 1

## Behavioral risk factors variables

| Variable       | Description                                         |
|----------------|-----------------------------------------------------|
| alcohol        | Alcohol consumption, in litres of pure alcohol      |

**Notes:**
- Alcohol consumption is recorded per capita for individuals aged 15 and over.

## Country classification variables

| Variable          | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| Status            | Developed or developing status of a country (recoded as a binary variable)  |
