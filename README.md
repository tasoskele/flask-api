## Python REST API - In progress...

## ROUTE LIST

| METHOD   | ROUTE                                    | FUNCTIONALITY                 | ACCESS      |
| -------- | ---------------------------------------- | ----------------------------- | ----------- |
| _POST_   | `/auth/signup/`                          | _Register new user_           | _All users_ |
| _POST_   | `/auth/login/`                           | _Login user_                  | _All users_ |
| _POST_   | `/requests/request/`                     | _Place an request_            | _All users_ |
| _PUT_    | `/requests/request/update/{request_id}/` | _Update an request_           | _All users_ |
| _PUT_    | `/requests/request/status/{request_id}/` | _Update request status_       | _Superuser_ |
| _DELETE_ | `/requests/request/delete/{request_id}/` | _Delete/Remove an request_    | _All users_ |
| _GET_    | `/requests/user/requests/`               | _Get user's requests_         | _All users_ |
| _GET_    | `/requests/requests/`                    | _List all requests made_      | _Superuser_ |
| _GET_    | `/requests/requests/{request_id}/`       | _Retrieve an request_         | _Superuser_ |
| _GET_    | `/requests/user/request/{request_id}/`   | _Get user's specific request_ |
| _GET_    | `/docs/`                                 | _View API documentation_      | _All users_ |
