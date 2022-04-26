*** Settings ***
Library         s3bucket.py
Variables       variables.py


*** Test Cases ***
Check S3 Bucket ServerSide Encryption
   ${encryption}=                   Check Encryption    ${ADMIN_CREDS}              ${BUCKET}
   Should Be True                   ${encryption}   


Check S3 Bucket Encryption Deleting Constraints
    Run Keyword And Expect Error    ClientError:*       Check Encryption Deleting   ${READ_ONLY_CREDS}      ${BUCKET}
    Run Keyword And Expect Error    ClientError:*       Check Encryption Deleting   ${WITHOUT_ROLES_CREDS}  ${BUCKET}


Check Test File Presented in S3 Bucket
    ${file_presented}=              Check File Presented                            ${ADMIN_CREDS}          ${BUCKET}       ${FILE}
    Should Be Equal                 ${file_presented}   manual/amazon.txt
    ${file_presented}=              Check File Presented                            ${READ_ONLY_CREDS}      ${BUCKET}       ${FILE}
    Should Be Equal                 ${file_presented}   manual/amazon.txt
    Run Keyword And Expect Error    ClientError:*       Check File Presented        ${WITHOUT_ROLES_CREDS}   ${BUCKET}      ${FILE}
