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
| adult_mortality   | Adult mortality rate per 1,000 persons                             |
| infant_deaths     | Infant mortality rate (deaths per 1,000 live births)               |
| under_five_deaths | Number of deaths of children under 5 years of age per 1,000 births |

**Notes**
- Adult Mortality: recorded for both sexes; probability of death between ages 15 and 60 per 1,000 persons.

## Health outcomes & burden variables

| Variable              | Description                                               |
|-----------------------|-----------------------------------------------------------|
| overweight_prevalence | Prevalence of overweight adults within population         |
| measles               | Number of reported measles cases per 1,000 people         |
| hiv_aids              | Number of HIV/AIDS-related deaths among children          |
| thinness_10_19_years  | Prevalence of thinness among children and adolescents (%) |
| thinness_5_9_years    | Prevalence of thinness among children, 5-9 (%)            |

**Notes**
- overweight_prevalence: overweight adults with BMI > 25, expressed as a percentage (0-100%)
- hiv_aids: number of recorded deaths among children aged 0–4 per 1,000 live births
- thinness_10_19_years: percentage of thinness among children and adolescents aged 10 to 19
- thinness_5_9_years: percentage of thinness among children between aged 5 to 9

## Health system & interventions variables

| Variable                | Description                                                       |
|-------------------------|-------------------------------------------------------------------|
| total_expenditure       | Government expenditure on health as a % of total govt expenditure |
| percentage_expenditure  | Health expenditure per capita as a ratio of GDP per capita        |
| hepatitis_b_vaccination | Percentage of children vaccinated against hepatitis B (HepB)      |
| polio_vaccination       | Percentage of children vaccinated against poliomyelitis (Pol3)    |
| diphtheria_vaccination  | Percentage of one-year-old children vaccinated against (DTP3)     |

**Notes:**
- Hepatitis B: measured among one-year-old children
- Polio: measured among one-year-old children
- Diphtheria: measured among one-year-old children vaccinated against diphtheria, tetanus and whooping cough (DTP3)
- Percentage expenditure: An index; Values exceeding 100 indicate unit scaling differences in source data rather than a literal percentage.

## Economic and development variables

| Variable                        | Description                                            |
|---------------------------------|--------------------------------------------------------|
| gdp                             | Gross domestic product per capita in US dollars ($)    |
| income_composition_of_resources | Human Development Index in terms of income composition |
| schooling                       | Number of years of education                           |

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
| status            | Developed or developing status of a country (recoded as a binary variable)  |
