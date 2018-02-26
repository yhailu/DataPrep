*** Settings ***
Documentation    Adhoc Regression Suite
#Test Teardown   close test

Library   keywords.adhoc

*** Variables ***
${SiteUrl}   https://54.183.155.232:9443/vertex/open/veit/scroll/index.html#/login
#${SiteUrl}   https://vebd1.vertexinc.com/vertex/open/veit/index.html#/login

*** Test Cases ***
Setting up test ...
    setup test
Launch VE
    launch URL  ${SiteUrl}
Login to VE
##    login   vedemo  iL0veTax
##Select Database and Table
##    select db table   vedemo   a
##Run Query
##    run query
##Save Query
##    save query  auto_query_test4
##Add col to Qury
##    add col   substrTest
##    run query
##Delete Query
##    delete   auto_query_test4
#Closing test ...
    Close Test
