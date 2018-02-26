*** Settings ***
Documentation    Suite description
Library   smokeKeywords.regressionKeywords



*** Variables ***
${SiteUrl}   https://vebd1.vertexinc.com/vertex/open/veit/index.html#/login


*** Test Cases ***
Login with parameters
    launch test   ${SiteUrl}   daniel   iL0veTax
Logout
    logout