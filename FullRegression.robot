*** Settings ***
Documentation    Suite description

Library   smokeKeywords.regressionKeywords



*** Variables ***
${SiteUrl}  https://vebd1.vertexinc.com/vertex/open/veit/index.html#/login


*** Test Cases ***
Login with parameters
    launch test   ${SiteUrl}   daniel   iL0veTax
#Create table
#    create table    open_robot   autotable    String1,Int2,Big3    1
#Add Column to Table
#    add col to table   open_robot   autotable  newCol
#Add reserved word as a new column
#    add col to table   open_robot   autotable   Date
#Attempt to use a column name that starts with a number
#    add col to table  open_robot   autotable   2Name
#Attempt to use column name with no name
#    add col to table   open_robot   autotable   ${EMPTY}
#Attempt to use column name with special Characters
#    add col to table   open_robot   autotable  $!#$%^&*()
#Add 2 additional columns
#    add col to table   open_robot   autotable   double4
#    add col to table   open_robot   autotable   Date5
#Delete table 2
#    delete table    open_robot   autotable

*** Test Cases ***
Adhoc Select Database and Table
    select db table   open_dan   autotable1
Run Query
    run query
#Filter =
#    adhoc filter   =   string1
#Filter >=
#    adhoc filter   >=   string6
#Filter >
#    adhoc filter   >   string6
#Filter <=
#    adhoc filter   <=   string3
#Filter <
#    adhoc filter   <   string3
#Filter <>
#    adhoc filter   <>   string3
#Filter in
#    adhoc filter   =   blank
#Filter not in
#    adhoc filter   not in   blank
#Filter in Free Form
#    adhoc filter   in_free_form   string1
#Filter like
#    adhoc filter   like   string3
#Filter not like
#    adhoc filter   not like   string3
#Filter equal field
#    adhoc filter   =F   date5
#Filter not equal field
#    adhoc filter   <>F   date5
#Save Query
#    save query  auto_query_test4   test   False
##Add col to Query
##    add col   substrTest
##    run query
#Delete Query
#    delete query   test321
#Adhoc Select Database and Table
#    select db table   open_dan   autotable1
#Run Query
#    run query
#Save Query
#    save query   robotquery   AutoQuery Description   False
#Save as new Query
    save query   blank   blank   True
Delete Query
    delete query   robotquery
    delete query   robotquery
    delete query   autoquery2
#Pivot test
#    pivot test   open_dan   autotable1
close test
    close test