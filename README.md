Libreoffice OOXML QA Automation Proposal (Mar/2013)
===================================================


Motivation and Purpose
----------------------

Libreoffice OOXML import/export/roundtrip testing is time consuming,
especially it matters to be efficiency awared in product release
phases, when testing plan is more intensive than usual times.

This project is motivated by conducting automated results verification
as many as possible based on current software conditions, meanwhile
optimizing the process of manual interfered testing results analysis
via user friendly results reporting tools.


Requirements Analysis and Specification
---------------------------------------

### Terms ###

__OOXML__ MSOffice OpenXML format with file name suffixdocx/xlsx/pptx

__MSO03__ MSOffice 97-03 binary document format with file name suffix doc/xls/ppt

__ODF__   Open Document Format with file name suffix odt/ods/odp

### OOXML testing procedures ###

Generically, current OOXML testing behaviors or so called processes
can be summarized as:

#### Import testing ####

1. Open OOXML with Libreoffice
2. Open OOXML with MSOffice
3. Visually compare the document line by line
4. Verification:
    - *PASS* If the document is rendered exactly the same in both of the
      applications, the testing is considered
    - *Feature FAIL* If the document is rendered not same or
      interactive functions inside the document could not work
      correctly (i.e hyperlinks, indexes, fields etc.)
    - *Hang/Crash FAIL* - If Libreoffice is hang/crash during the
      opening procedure, the testing is considered as FAIL.
5. In the condition of testing FAIL and it is NOT REGRESSION:
    - Feature failure:
      Describe the issue and report the bug in bugzilla with the
      following documents attached:
        * original OOXML
        * produce a pdf file of the OOXML through Libreoffice
        * produce a pdf file of the OOXML through MS office
    - Hang/crash failure:
      Describe the issue and report the bug in bugzilla with the
      following documents attached:
        * original OOXML
        * crash traceback

#### Export testing ####

1. Open MSO03 with Libreoffice, then save it as OOXML
2. Open MSO03 with MSOffice, then save it as OOXML
3. Open both of the saved OOXML in MSOffice, visually compare the
   document line by line
4. Verification:
    - *PASS* If the document is rendered exactly the same in both of the
      applications, the testing is considered
    - *Feature FAIL* If the document is rendered not same or
      interactive functions inside the document could not work
      correctly (i.e hyperlinks, indexes, fields etc.)
    - *Hang/Crash FAIL* - If Libreoffice is hang/crash during the
      opening procedure, the testing is considered as FAIL.
5. In the condition of testing FAIL and it is NOT REGRESSION
    - Feature failure
      Describe the issue and report the bug in bugzilla with the
      following documents attached:
        * original MSO03
        * produce a pdf file of the OOXML through Libreoffice
        * produce a pdf file of the OOXML through MS office
    - Hang/crash failure
      Describe the issue and report the bug in bugzilla with the
      following documents attached:
        * original MSO03
        * crash traceback

#### Rountrip testing ####

Roundtrip testing should be done for both OOXML and MSO03 with same
steps, however the path of testing can be defined through input:

    MSO03    --export-->    OOXML    --import-->    MSO03
    
    OOXML    --import-->    MSO03    --export-->    OOXML

Since the testing logic is actually identical , we can be describe the process
using MSO03 as input for now, then the OOXML testing shares the exact
steps except for the different target input/output document formats:

1. With Libreoffice, open MSO03 and save as OOXML
2. With Libreoffice, open the produced OOXML and save back as MSO03
3. With MSOffice, open both MSO03 in 3.1 and 3.2, then visually
   compare the two documents line by line:
4. Verification:
    - PASS - If the documents are rendered exactly the same in
      MSOffice
    - Feature FAIL - If the documents are rendered not same or
      interactive items inside the document (i.e hyperlinks,
      indexes, fields etc.) could not work consistently in
      MSOffice.
    - Hang/Crash FAIL - If Libreoffice is hang/crash during the
      converting procedure in 3.1 and 3.2, the testing is
      considered as FAIL.
5. In the condition of testing FAIL and it is NOT REGRESSION
    - Feature failure
      Describe the issue and report the bug in bugzilla with the
      following documents attached:
        * original MSO03
        * produce a pdf file of the OOXML through Libreoffice
        * produce a pdf file of the OOXML through MS office
    - Hang/crash failure
      Describe the issue and report the bug in bugzilla with the
      following documents attached:
        * original MSO03
        * crash traceback

### OOXML Procedure Analysis ###

Imagine there are hundreds of testing samples input, according to the
above behaviors, we could easily find challenges when manually testing
each of them.

As follows, I would analyze the possible improvements of the steps
taking all above procedures as a whole, in which the procedures
actually share lots of common characteristics possibly to be
automatically implemented, more efficient or better organized:

1. Test documents mangement
2. Reference documents generating
3. Automated verification
4. Spot regressions

#### Test documents management ####

#### Reference documents generating ####

#### Automated verification ####

#### Spot regressions ####

### Requirements Specification ###


Design and Implementation
-------------------------
