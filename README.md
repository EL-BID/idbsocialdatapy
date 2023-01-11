
![analytics image (flat)](https://raw.githubusercontent.com/vitr/google-analytics-beacon/master/static/badge.svg)
![analytics](https://www.google-analytics.com/collect?v=1&cid=555&t=pageview&ec=repo&ea=open&dp=/urbanpy/readme&dt=&tid=UA-4677001-16)

**SCL Data - Data Ecosystem Working Group**

[![IDB Logo](https://scldata.iadb.org/assets/iadb-7779368a000004449beca0d4fc6f116cc0617572d549edf2ae491e9a17f63778.png)](https://scldata.iadb.org)

# Welcome to idbsocialdatapy
 
The objective of this library is to help users access standardized SCLdata indicators on topics such as poverty, inequality, health, labor market, gender and diversity, education, and migration for the 26 countries of the region. 

The project to develop the library in Python resulted from the implementation workshop for IDBSocialData. Individual developers showed interest in the library in Python and decided to collaborate voluntarily with the IDB to develop this tool. 

## Installation

To install the idbsocialdatapy library you can use:

```sh
$ pip install idbsocialdatapy

```

# Metadata 

There are many indicators in this library, with the metadata functions you will be able to find all the indicators we have available. 

## Dictionary 

Get the dictionary for all the indicators in our API. 

```python
import idbsocialdatapy as idb
dictionary = idb.query_dictionary()

```

## Countries, themes & sources 

- See available countries with iso-codes and regions. 
- See themes included in our indicators. For instance, labor markets, education, and social protection. 
- Review the sources we use to construct our indicators.

```python
countries = idb.get_countries()
themes = idb.get_themes()
sources = idb.get_sources()

```

# Data

## Look for indicators 

This is the main function of the library. With this function, you will be able to query all the indicators from our API. 
The function has four main inputs. 

1. indicator: needed. Pick one or multiple indicators to query.

2. categories: optional. If no category is chosen, you will get the indicator for the total population. The categories you can pick from are the following: 

|categories| comments |
| :---: |:--- |
| sex | women or men |
| quintile | indicator for different income quintiles |
| area | urban or rural |
| age | indicators for populations with different ages |
| ethnicity | afro descendants, indigenous and non-afro non-indigenous |
| disability | indicators for the population living with and without disabilities |
| migration | migrant or non-migrant |

3. countries: optional. If you do not pick a category, you will get the information for all the countries available for that indicator. 
If you want to pick specific countries you will do so with the isoalpha3 code. You can get the isoalpha3 code for all the countries from the following function:

```python
countries = idb.get_countries()

```
4. yearstart: and yearend: optional. You can use these arguments if you want to limit the years you get data from. 

## Example

Here is an example using all the arguments. We will query the poverty indicators, disaggregated by gender, for Mexico, Colombia, and Brasil, for the period between 2005 and 2020.

```python
poverty = idb.query_indicator(indicator = 'pobreza', # define indicator to consult 
                          categories = 'sex', # define category/ies I want to see in the indicator
                          countries = 'COL,BRA,MEX', #define countries you want data from
                          yearstart = '2005', # starting period
                          yearend = '2021') # ending period
```

## Authors 

idbsocialdatapy's original authors are:

- [Genrry Hernández](https://github.com/genrry)
- [Juan Pablo Zorrilla Salgador](https://github.com/jpzorrilla)
- [Elena Fernández López](https://github.com/elainfl)
- [María Reyes Retana Torre](https://github.com/mariarrt94)
- [Sergio Andrés Herrera Velásquez](https://github.com/sahvsergio)
- [Juan Villa Hernández](https://github.com/juanfvilla)

## License

Copyright © 2020. Banco Interamericano de Desarrollo ("BID"). Uso autorizado. [AM-331-A3](LICENSE.md)

## Contributors

 <a href = "https://github.com/EL-BID/idbsocialdatapy/graphs/contributors">
   <img src = "https://contrib.rocks/image?repo=EL-BID/idbsocialdatapy"/>
 </a>
