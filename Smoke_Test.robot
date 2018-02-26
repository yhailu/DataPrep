*** Settings ***
Documentation    Suite description

Library   smokeKeywords.regressionKeywords



*** Variables ***
${SiteUrl}  https://vebd1.vertexinc.com/vertex/open/veit/index.html#/login


*** Test Cases ***
Login with parameters
    launch test   ${SiteUrl}   daniel   iL0veTax
#Create Table
#    create table   open_robot   automated_table2    String1,Int2,Big3    1
#    create table   open_robot   automated_table3    String1,Int2,Big3    1
#Delete Table
#    delete table   open_robot   automated_table2
#Manual File Upload
#    manual file upload  C:/Test Files/Main Files/DatatypesEXT.csv
Adhoc Select Database and Table
    select db table   open_dan   autotable1
Run Query
    run query
Filter =
    adhoc filter   =   string1
Filter >=
    adhoc filter   >=   string6
Filter >
    adhoc filter   >   string6
Filter <=
    adhoc filter   <=   string3
Filter <
    adhoc filter   <   string3
Filter <>
    adhoc filter   <>   string3
Filter in
    adhoc filter   =   blank
Filter not in
    adhoc filter   not in   blank
Filter in Free Form
    adhoc filter   in_free_form   string1
Filter like
    adhoc filter   like   string3
Filter not like
    adhoc filter   not like   string3
Filter equal field
    adhoc filter   =F   date5
Filter not equal field
    adhoc filter   <>F   date5
Save Query
    save query  auto_query_test4   test   False
Add col to Query
    add col   substrTest
    run query
Delete Query
    delete query   test321
##Joins
##    Joins Select Dbs And Tables   open_automated   open_automated   open_automated   autotable1   autotable2
#Union
#    union
#Mappings Select db and table
#    mappings select db table   open_dan   autotable1   open_dan   autotable2
#Mapping Test
#    mapping test
#Delete Mapping
#    delete mapping   autoMaptest1
#Closing test ...
#    Close Test


