*** Settings ***
Documentation    Generic Rest API Suite For All VE Functionality

Library   RestKeywords.RestAPI
*** Variables ***
${data}   {\"name\":\"appTest\"," \"\"widgets\":[{\"additionalProperties\":{}," \"\"name\":\"appTest\",\"sizeX\":2,\"sizeY\":2,\"col\":0,\"row\":0}]," \"\"additionalProperties\":{\"defaultDash\":\"NO\"}}

*** Test Cases ***
#GET
#    get    dashboards
#    get    joins
#    get    tablemap2s
#    get    databases
#    get    querys
#    get    unions
#    get    dataflows
#    get    hierarchys
#POST
#    post   dashboards
Delete
    delete    unions   autounion1

#DELETE
#    delete   tablemap2s   dktestpub
