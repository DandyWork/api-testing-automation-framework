# API Testing Automation Framework

A Python-based API automation framework built using Pytest and Requests.

This framework validates REST API functionality through automated tests, including authentication, CRUD operations, negative testing, response validation, schema validation, and CI/CD execution using GitHub Actions.

The project uses a layered structure to separate API logic, test scenarios, test data, configuration, and validation utilities to make the framework easier to maintain and scale.

---

## Framework Structure

apis/

Contains API service classes that handle endpoint actions.

auth_api.py:
Handles authentication API requests and generates authentication tokens.

booking_api.py:
Handles booking API operations:
- Create booking
- Get booking details
- Update booking
- Delete booking
- Get booking list

The API classes separate endpoint logic from test cases, allowing tests to focus only on validation.

---

framework/

Contains reusable framework components.

api_client.py:
A common HTTP client wrapper responsible for sending GET, POST, PUT, and DELETE requests.

api_response.py:
Handles API response objects and provides access to:
- Status code
- Response body
- Response data

---

config/

Contains environment configuration.

environment.py:
Loads environment variables from .env files.

settings.py:
Provides centralized access to:
- Base URL
- Username
- Password

---

test_data/

Contains external test payload data.

authentication_data.json:
Stores valid and invalid authentication scenarios.

booking_data.json:
Stores booking request payloads for:
- Successful creation
- Update scenarios
- Negative testing cases

---

schemas/

Contains JSON response schemas used for contract validation.

auth_schema.json:
Validates authentication response structure.

booking_create_schema.json:
Validates booking creation response structure.

booking_schema.json:
Validates booking detail response structure.

---

tests/

Contains all automated test scenarios.

test_authentication.py:
Validates authentication functionality.

Covered cases:
- Successful login
- Invalid password
- Missing username
- Missing password

---

test_booking_create.py:
Validates successful booking creation.

Checks:
- HTTP response status
- Response structure
- Required booking fields

---

test_booking_get.py:
Validates retrieving booking details by booking ID.

Checks:
- Returned booking data matches created booking
- Response schema validation

---

test_booking_update.py:
Validates updating existing booking data.

Checks:
- Update request success
- Updated response data
- Authentication requirement

---

test_booking_delete.py:
Validates deleting a booking.

Checks:
- Delete request success
- Deleted booking cannot be retrieved again

---

test_booking_health.py:
Validates booking listing endpoint availability.

Checks:
- Endpoint accessibility
- Response status

---

test_booking_negative.py:
Validates API behavior with invalid requests.

Covered cases:
- Missing firstname
- Missing lastname
- Invalid datatype handling

Some negative scenarios are marked as expected failure (xfail) when the API accepts invalid input by design.

---

utils/

Contains reusable helper functions.

schema_validator.py:
Validates API responses against JSON schemas using jsonschema.

This ensures API responses follow the expected contract.

---

.github/workflows/

Contains GitHub Actions CI/CD configuration.

The workflow automatically:
- Installs dependencies
- Executes automated tests
- Generates test reports
- Validates framework stability after code changes

---

## Technology Stack

Python  
Pytest  
Requests  
JSON Schema Validation  
Python-dotenv  
GitHub Actions  
HTML Test Report