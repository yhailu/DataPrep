*** Settings ***
Documentation    Suite description

Library     keywords.tableKeywords

*** Variables ***
${SiteUrl}  https://vebd1.vertexinc.com/vertex/open/veit/index.html#/login

*** Test Cases ***
Setup test
    setup test
Launch VE
    launch url  ${SiteUrl}
Login with parameters
    login with parameters  vedemo  iL0veTax
Create table
    create table    Autotable1    String1,Int2,Big3    1
Add Column to Table
    add column to table   open_yesu_test   Autotable1   newCol
Add reserved word as a new column
    add column to table   open_yesu_test   Autotable1   Date
Attempt to use a column name that starts with a number
    add column to table   open_yesu_test   Autotable1   2Name
Attempt to use column name with no name
    add column to table   open_yesu_test   Autotable1   ${EMPTY}
Attempt to use column name with special Characters
    add column to table   open_yesu_test   Autotable1   $!#$%^&*()
Add 2 additional columns
    add column to table   open_yesu_test   Autotable1   double4
    add column to table   open_yesu_test   Autotable1   Date5
Delete table 2
    delete table    open_yesu_test   Autotable1
Close browser and Driver
    close driver broswer