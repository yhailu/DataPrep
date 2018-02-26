*** Settings ***
Documentation    Suite description
Library     smokeKeywords.regressionKeywords


*** Variables ***
${SiteUrl}  https://vebd1.vertexinc.com/vertex/open/veit/index.html#/login


*** Test Cases ***
Login with parameters
    launch test   ${SiteUrl}   daniel   iL0veTax
Select db and table
    mappings select db table   open_dan   autotable1   open_dan   autotable2
Map source fields to destination table
    map source to dest   string1   string1
    map source to dest   int2   int2
    map source to dest   big3   big3
    map source to dest   double4   double4
    map source to dest   date5   date5
    map source to dest   filename   filename
Save map
    save mappings   AutomatedMap1   map description
Run map
    run mapping
map test
    map test
Delete Mapping
    delete mapping   AutomatedMap1
Closing Test ....
    close test

