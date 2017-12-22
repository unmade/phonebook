# API

Each GET-method accepts following parameters:

| Name      | Type | Description |
| :-------- | :--- | :---------- |
| limit     | int  | Defines page size. Default to 50 |
| offset    | int  | Defines offset of the elements |
| ordering  | str  | Field to apply ordering by |


## Companies

### /companies/api/company

**Method GET**

Returns list of companies

| Name           | Type | Description |
| :------------- | :--- | :---------- |
| search         | str  | Search by name |
| phones__number | str  | Filters by provided phone number |
| emails__emails | str  | Filters by provided email |


### /companies/api/company/:id

**Method GET**

Returns company with specified `id`


### /companies/api/center

**Method GET**

Returns list of centers

| Name           | Type | Description |
| :------------- | :--- | :---------- |
| company        | int  | Filters by id of the company |
| search         | str  | Search by name |
| phones__number | str  | Filters by provided phone number |
| emails__emails | str  | Filter by provided email |


### /companies/api/center/:id

**Method GET**

Returns center with specified `id`


### /companies/api/division

**Method GET**

Returns list of divisions

| Name           | Type | Description |
| :------------- | :--- | :---------- |
| center         | int  | Filters by id of the center |
| search         | str  | Search by name |
| phones__number | str  | Filters by provided phone number |
| emails__emails | str  | Filter by provided email |


### /companies/api/division/:id

**Method GET**

Returns division with provided `id`


## Employees

### /employees/api/employee

**Method GET**

Return list of employees

| Name           | Type | Description |
| :------------- | :--- | :---------- |
| company        | int  | Filters by id of the company |
| center         | int  | Filters  by id of the center |
| division       | int  | Filters by id of the division |
| search         | str  | Search by first name, surname and patronymic |
| phones__number | str  | Filters by provided phone number |
| emails__emails | str  | Filter by provided email |


### /employees/api/employee/:id

**Method GET**

Returns employee with specified `id`


## Feedback

### /feedback/api/feedback

**Method GET**

Returns list of feedbacks

**Method POST**

Create new feedback

| Name      | Type | Description |
| :---------| :--- | :---------- |
| sender    | str  | Sender name |
| text      | text | text |
