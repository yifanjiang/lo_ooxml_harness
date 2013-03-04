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

Requirements Analysis and Definition
------------------------------------

### Key Terms ###

*OOXML* MSOffice OpenXML format with file name suffixdocx/xlsx/pptx
*MSO03* MSOffice 97-03 binary document format with file name suffix doc/xls/ppt
*ODF*   Open Document Format with file name suffix odt/ods/odp

### OOXML testing analysis ###

Generically, current OOXML testing behaviors or so called processes
can be summarized as:

1. Import testing

    1. Open OOXML with Libreoffice
    
    2. Open OOXML with MSOffice
    
    3. Visually compare the document line by line
    
    4. Verification
    
        a. PASS - If the document is rendered exactly the same in both of the
        applications, the testing is considered

        b. Feature FAIL - If the document is rendered not same or
        interactive functions inside the document could not work
        correctly (i.e hyperlinks, indexes, fields etc.)

        c. Hang/Crash FAIL - If Libreoffice is hang/crash during the
        opening procedure, the testing is considered as FAIL.

    5. In the condition of testing FAIL and it is NOT REGRESSION

        a. Feature failure

        Describe the issue and report the bug in bugzilla with the
        following documents attached:

            1. original OOXML
            2. produce a pdf file of the OOXML through Libreoffice
            3. produce a pdf file of the OOXML through MS office

        b. Hang/crash failure

        Describe the issue and report the bug in bugzilla with the
        following documents attached:

            1. original OOXML
            2. crash traceback

2. Export testing

    1. Open MSO03 with Libreoffice, then save it as OOXML

    2. Open MSO03 with MSOffice, then save it as OOXML

    3. Open both of the saved OOXML in MSOffice, visually compare the
    document line by line

    4. Verification

        a. PASS - If the document is rendered exactly the same in both of the
        applications, the testing is considered

        b. Feature FAIL - If the document is rendered not same or
        interactive functions inside the document could not work
        correctly (i.e hyperlinks, indexes, fields etc.)

        c. Hang/Crash FAIL - If Libreoffice is hang/crash during the
        opening procedure, the testing is considered as FAIL.

    5. In the condition of testing FAIL and it is NOT REGRESSION

        a. Feature failure
        Describe the issue and report the bug in bugzilla with the
        following documents attached:

            1. original MSO03
            2. produce a pdf file of the OOXML through Libreoffice
            3. produce a pdf file of the OOXML through MS office

        b. Hang/crash failure
        Describe the issue and report the bug in bugzilla with the
        following documents attached:

            1. original MSO03
            2. crash traceback        

3. Rountrip testing

    Roundtrip testing should be done for both OOXML and MSO03 with
    same steps, however the path of testing can be defined through
    input:

        MSO03 (export to) -> OOXML (import to) -> MSO03

        OOXML (import to) -> MSO03 (export to) -> OOXML

    Since the testing logic is the same, we can be describe the process
    using MSO03 as input for now, then the OOXML testing shares the
    exact steps except for the different target input/output document
    formats.

    1. With Libreoffice, open MSO03 and save as OOXML

    2. With Libreoffice, open the produced OOXML and save back as MSO03

    3. With MSOffice, open both MSO03 in 3.1 and 3.2, then visually
    compare the two documents line by line

    4. Verification:

        a. PASS - If the documents are rendered exactly the same in
        MSOffice

        b. Feature FAIL - If the documents are rendered not same or
        interactive items inside the document (i.e hyperlinks,
        indexes, fields etc.) could not work consistently in MSOffice.

        c. Hang/Crash FAIL - If Libreoffice is hang/crash during the
        converting procedure in 3.1 and 3.2, the testing is considered as FAIL.    

    5. In the condition of testing FAIL and it is NOT REGRESSION

        a. Feature failure
        
        Describe the issue and report the bug in bugzilla with the
        following documents attached:

            1. original MSO03
            2. produce a pdf file of the OOXML through Libreoffice
            3. produce a pdf file of the OOXML through MS office

        b. Hang/crash failure
        
        Describe the issue and report the bug in bugzilla with the
        following documents attached:

            1. original MSO03
            2. crash traceback
    
    
### Challenges ###

Major constraints against our efficiency of testing OOXML filters can
be summarized as:

    1. test documents management
    2. conversions
    3. search for regressions
    4. confirm import/export issue
    5. snapshots generation in different filtering phases (pdf)
    6. automatic verification

### Requirements ###    

Design and Implementation
-------------------------
