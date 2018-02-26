*** Settings ***
Documentation    Suite description
Library     smokeKeywords.regressionKeywords


*** Variables ***
${SiteUrl}  https://vebd1.vertexinc.com/vertex/open/veit/index.html#/login


*** Test Cases ***
Login with parameters
    launch test   ${SiteUrl}   daniel   iL0veTax
unions Regression
   unions regression
open and run existing union
    open and run   autounion1
delete union
    delete union   autounion1
    delete union   autounion2
Close Test
    close test