**SCL Data - Data Ecosystem Working Group**

[![IDB Logo](https://scldata.iadb.org/assets/iadb-7779368a000004449beca0d4fc6f116cc0617572d549edf2ae491e9a17f63778.png)](https://scldata.iadb.org)


## Table of Contents:
---

- [Objective and context](#objective-and-context)
- [Collaboration](#description-and-context)
- [Road Map](#road-map)
- [Author/s](#authors)
- [License](#license)
- [Limitation of responsibilities](#limitation-of-responsibilities)

## Objective and context
 <font size="1">**Important**: This package is in the development phase</font>
 
The objective of this tool is to help users access standardized SCLdata indicators on topics such as poverty, inequality, health, labor market, gender and diversity, education, and migration for the 26 countries of the region.  This tool will be developed to facilitate the consultation of the region's indicators, providing a unified source of data on different topics that can be easily used to generate comparative analyses or studies on the region. This will boost knowledge about the region, facilitating decision-making with a reliable and comparable source of information for the countries of Latin America and the Caribbean. 

The project to develop the library in Python resulted from the implementation workshop for IDBSocialData. Individual developers showed interest in the library in Python and decided to collaborate voluntarily with the IDB to develop this tool. 
At the end of the project, all the developers who participate will be included in the package as authors.


## Collaboration 

### Structure

To keep the work structured, the repository will have two main branches: 1) main and 2) development that helps to minimize errors and make the work more effective:

**1) Main:** The version contained in this Branch is always the most current version and the one which is reviewed and approved to run. This Branch should not be modified unless all changes are approved in the Development Branch. 

**2) Development:** This Branch is designated to test the changes or additions made to the scripts. From this Branch, we will create individual branches to do given tasks. 

Because the work will be done simultaneously by several developers, it is required that each one works with a personal branch where the required feature is solved or worked on and the following steps must be followed: 

1) To work on the feature, a Branch that is a copy of the Development version must be created.  
    
2) Once the process of modification or adjustment of the scripts is finished, the pull request must be made to perform the merge. The merge must always be requested with the Development branch. 

3) Once the merge request is made, it is reviewed and verified that there are no errors in the new pull. Then the pull and merge will be done with the main Branch. 

### Language

To keep things as neat as possible and to maximize the reach of the library, we will use English for all contributions. 

## Road-map

To make the work more effective the roadmap to develop this library will be based on the R package [idbsocialdataR](https://github.com/EL-BID/idbsocialdataR). We will work to replicate the different functions in the R package. 

The functions are ordered by importance, thus we will start working from the top and move to the bottom. The last column shows the category of each function, we will do one script by category. For instance, query_indicator, get_themes, get_countries and get_sources will be in the same metadata script.

| Function | Objective | Status | Developer | Script type |
| :---: | :--- | :--- | :--- | :--- |
| iadburls | Function to get urls of the API | Done | Genrry| utils |
| query_indicator | Main function, query indicators | Done | Genrry | scldata (core) |
| query_dictionary | See available indicators | In progress | María | Metadata |
| get_countries | Search available countries | Done | JP y Elena | Metadata |
| get_themes | Search available topics | Done | JP y Elena| Metadata |
| search_indicator | Give string to search within the dictionary for an indicator | Done | Genrry | scldata (core) |
| get_sources | Get available sources | In progress | JP y Elena | Metadata |
| idbsocial_plot | Create plot | In progress | Juan & Sergio | Plot |
| get_map | Get a map from regions | In progress | Juan & Sergio | Map |
| idbsocial_choropleth | Create a map with indicator | In progress | Juan & Sergio | Map |


The developers will choose a function/functions, via slack, and we will create the repository's project and assign the tasks to have control and avoid repetitions.

## Authors

This section will be added when we finish the library.

## Thanks to all contributors ❤

 <a href = "https://github.com/EL-BID/idbsocialdatapy/graphs/contributors">
   <img src = "https://contrib.rocks/image?repo=EL-BID/idbsocialdatapy"/>
 </a>

## License


## Limitation of responsibilities
