*** Settings ***
Documentation    Suite description

Library     keywords.manualFileUpload

*** Variables ***
${SiteUrl}  https://vebd1.vertexinc.com/vertex/open/veit/index.html#/login

*** Test Cases ***
Setup Test
    setup test
Launch VE
    launch URL    ${SiteUrl}
Login
    login with parameters   vedemo  iL0veTax
Manual File Upload
    manual file upload  C:/Test Files/Main Files/DatatypesEXT.csv
Close browser and Driver
    close driver browser

