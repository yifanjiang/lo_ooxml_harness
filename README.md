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

### OOXML Test Procedures ###

Generically, current OOXML testing behaviors or so called processes
can be summarized as:

#### Import testing ####

    OOXML    --import-->    PDF

1. Open OOXML with Libreoffice
2. Open OOXML with MSOffice
3. Visually compare the document line by line. Interactive elements in
   the document, also need test here (i.e hyperlinks, indexes, fields
   etc.).
4. Verification:
    - *Pass* If the document is rendered exactly the same in both of the
      applications
    - *Feature Fail* If the document is rendered not same or
      interactive elements inside the document could not work
      correctly
    - *Hang/Crash Fail* - If Libreoffice is hang/crash during the
      opening procedure, the testing is considered as FAIL.
5. In the condition of testing FAIL and it is NOT REGRESSION:
    - Feature fail:
      Describe the issue and report the bug in bugzilla with the
      following documents attached:
        * original OOXML
        * produce a PDF of the OOXML through Libreoffice
        * produce a PDF of the OOXML through MS office
    - Hang/crash fail:
      Describe the issue and report the bug in bugzilla with the
      following documents attached:
        * original OOXML
        * crash traceback

#### Export testing ####

    MSO03    --export-->    OOXML

1. Open MSO03 with Libreoffice, then save it as OOXML
2. Open MSO03 with MSOffice, then save it as OOXML
3. Open both of the saved OOXML in MSOffice, visually compare the
   document line by line. Interactive elements in the document, also
   need test here (i.e hyperlinks, indexes, fields etc.).
4. Verification:
    - *Pass* If the document is rendered exactly the same in both of the
      applications
    - *Feature Fail* If the document is rendered not same or
      interactive functions inside the document could not work
      correctly (i.e hyperlinks, indexes, fields etc.)
    - *Hang/Crash Fail* - If Libreoffice is hang/crash during the
      opening procedure, the testing is considered as FAIL.
5. In the condition of testing FAIL and it is NOT REGRESSION
    - Feature Fail
      Describe the issue and report the bug in bugzilla with the
      following documents attached:
        * original MSO03
        * produce a PDF of the OOXML through Libreoffice
        * produce a PDF of the OOXML through MS office
    - Hang/crash Fail
      Describe the issue and report the bug in bugzilla with the
      following documents attached:
        * original MSO03
        * crash traceback

#### Rountrip testing ####

Roundtrip testing should be done for both OOXML and MSO03 with same
steps, however the path of testing can be defined through input:

    MSO03    --export-->    OOXML    --import-->    MSO03
    
    OOXML    --import-->    MSO03    --export-->    OOXML

Since the testing logics of the two steps are actually identical , we
can describe the detailed steps using MSO03 to explain. The OOXML
testing will share the exact steps except for the different target
input/output document formats:

1. With Libreoffice, open MSO03 and save as OOXML
2. With Libreoffice, open the produced OOXML and save back as MSO03
3. With MSOffice, open both MSO03 mentioned in the above 2
   steps, visually compare the document line by line. Interactive
   elements in the document, also need test here (i.e hyperlinks,
   indexes, fields etc.).
4. Verification:
    - PASS - If the documents are rendered exactly the same in
      MSOffice
    - Feature Fail - If the documents are rendered not same or
      interactive elements inside the document could not work
      consistently in MSOffice.
    - Hang/Crash Fail - If Libreoffice is hang/crash during the
      converting procedure in 3.1 and 3.2
5. In the condition of testing FAIL and it is NOT REGRESSION
    - Feature failure Identify it is an import or export
      problem. Describe the issue and report the bug in bugzilla with
      the following documents attached:
        * original MSO03
        * produce a PDF for necessary OOXML or MSO03 according to
          the importing/exporting test procedure
    - Hang/crash failure
      Describe the issue and report the bug in bugzilla with the
      following documents attached:
        * original MSO03
        * crash traceback

### Test Procedures Analysis ###

Imagine there are hundreds of testing samples input, according to the
procedures description above, we could easily feel challenge when
manually testing each of them. Thus it makes sense to review all the
steps by analyzing them as a whole, in which lots of common
characteristics are shared, and possibly to be done automatically,
more efficient or better organized. I will review those items from
following aspects one by one:

* Test documents mangement
* Reference documents generating
* Automated verification
* Regressions identification

#### Test documents management ####

Consider to manage hundreds of test documents, 2 major problems come
into the testing practices.

- Sample documents and reference PDF documents

The test input can be either an OOXML or MSO03 file for import or
export test respectively. For a particular testing topic
(e.g. hyperlink, font size, embedded picture etc.), we want the same
test content to be tested in all import, export and roundtrip
scenarios.

On the other hand, when the testing fails, we want PDF to be exported
for sharing bugs with other people (who probably do not have MSOffice
to see a correct behavior).

As a results the manifest of what we need for sample documents are:
    * OOXML, MSO03 documents
    * PDF documents for each of the testing samples

- Test documents classification

We once thought to use external test case management tool to tag or
name the testing topics for test documents. However relying on
external tools to classify test documents does not bring much
convenience, especially when the test documents partake as standalone
files. Alternatively defining the high level test topic on the file
name itself would bring more benifits for easiness.

- Test documents storage

The test documents set can be evolved by adding, updating and removing
from time to time. So it is not bad to store the test samples in a
centralized mantainable storage. Thus with the same up-to-date test
documents set feched, tests could be executed in any platform as SUSE,
Ubuntu, Fedora etc. at any time.

#### Results documents management ####

By the fact we usually execute and analyze the testing on Linux, which
MSOffice could not be naturally installed to verify correct rendering
behavior, it makes sense to have corresponding PDFs for each of the
original documents, as well as all documents generated over all
testing procedures. Consequently we will not have to review testing
results by switching between Linux and Windows.

#### Automated verification ####

As shown in the section of test procedure, we ultimately want to
verify every test results by visual comparison. The direct way to do
this automatically is to compare pictures derived from the testing
results in various testing phases using graphic techniques.

#### Manually verification ####

The limitation of visual comparison is that we can not test the
import/export quality of how interactive elements works. Even if the
graphic techniques could offer help to identify difference between
pictures, there might be yet random factors to influence the
accuracy. Hence it seems inevitable to have manual interference for
the testing results verification.

#### Spot regressions ####

Once a test is spot as failed, we usually want to identify the
regression status to tell if the bug has been there for some
time. Meanwhile we want to tell if the bug has been reported.

### Requirements Specification ###

#### Test documents management ####

#### Results documents management ####

#### Automated verification ####

#### Manually verification ####

#### Spot regressions ####

Design and Implementation
-------------------------
