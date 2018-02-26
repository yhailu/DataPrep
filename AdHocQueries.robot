*** Settings ***
Documentation    Suite description

Library   smokeKeywords.regressionKeywords



*** Variables ***
${SiteUrl}  https://vebd1.vertexinc.com/vertex/open-sso/auth/login.html?originalUrl=https://vebd1.vertexinc.com/vertex/open/veit/index.html#/login


*** Test Cases ***
Login with parameters
    launch test   ${SiteUrl}   daniel   iL0veTax
#Create Table
#    create table   open_robot   automated_table2    String1,Int2,Big3    1
#Delete Table
#    delete table   open_robot   automated_table2
#Manual File Upload
#    manual file upload  C:/Test Files/Main Files/DatatypesEXT.csv
Adhoc Select Database and Table
    select db table   open_dan   autotable1
Run Query
    run query
Save Query
    save query   AutoQuery1   AutoQuery Description   False
Save as new Query
    save query   blank   blank   True
Delete Query
    delete query   autoquery2
    delete query   autoquery1
    delete query   autoquery3
Pivot test
    pivot test   open_dan   autotable1
Close Test
    Close Test
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