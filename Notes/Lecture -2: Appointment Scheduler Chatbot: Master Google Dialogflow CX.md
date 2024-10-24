# Lecture -2: Appointment Scheduler Chatbot: Master Google Dialogflow CX

**Dialogflow CX** provides a set of **system functions** that allow you to perform dynamic operations within your agent's conversational flows. These functions enable you to manipulate data, evaluate conditions, and generate dynamic responses during conversations. You can use system functions in conditions, static response messages, parameter presets, and webhook header values.

---

### **Function Syntax**

All system functions follow a specific syntax pattern:

```
$sys.func.<FUNCTION_NAME>(<ARGUMENT_1>, <ARGUMENT_2>, ...)
```

- **Function Name**: The name of the system function you want to use, written in uppercase letters (e.g., `ADD`, `SUBSTITUTE`).
- **Arguments**: The inputs required by the function, which can be inline values (like numbers, strings, booleans, lists), references to parameters (e.g., `$session.params.parameterName`), or nested functions.

**Example:**

```plaintext
$sys.func.ADD(1, 2) // Adds 1 and 2, resulting in 3
```

---

### **Using System Functions**

System functions can be applied in various parts of your agent:

- **Conditions**: To evaluate expressions and control the flow of the conversation.
- **Static Response Messages**: To generate dynamic content in text responses, custom payloads, or conditional responses.
- **Parameter Presets**: To assign values to parameters based on dynamic calculations or manipulations.
- **Webhook Header Values**: To include dynamic data in webhook requests.

---

### **Checking Function Results**

During a conversation, the results of system function evaluations are stored in the `QueryResult`. Specifically, you can find them under the `SystemFunctionResults` key within the `DiagnosticInfo` structure. This is useful for debugging and ensuring that your functions are producing the expected outputs.

---

### **Key System Functions**

Below is an overview of some commonly used system functions, along with examples of how to use them.

#### **1. Arithmetic Functions**

- **ADD**: Adds multiple numbers.
  - **Syntax**: `$sys.func.ADD(number1, number2, ...)`
  - **Example**: `$sys.func.ADD(5, 10)` results in `15`.

- **SUBTRACT (MINUS)**: Subtracts one number from another.
  - **Syntax**: `$sys.func.MINUS(minuend, subtrahend)`
  - **Example**: `$sys.func.MINUS(10, 4)` results in `6`.

- **MULTIPLY**: Multiplies multiple numbers.
  - **Syntax**: `$sys.func.MULTIPLY(factor1, factor2, ...)`
  - **Example**: `$sys.func.MULTIPLY(2, 3, 4)` results in `24`.

- **DIVIDE**: Divides one number by another.
  - **Syntax**: `$sys.func.DIVIDE(dividend, divisor, scale)`
    - **Scale** (optional): Number of decimal places in the result (default is 3).
  - **Example**: `$sys.func.DIVIDE(10, 3, 2)` results in `3.33`.

- **ROUND**: Rounds a decimal number to a specified number of decimal places.
  - **Syntax**: `$sys.func.ROUND(number, decimalPlaces)`
  - **Example**: `$sys.func.ROUND(10.5678, 2)` results in `10.57`.

#### **2. String Functions**

- **CONCATENATE**: Joins multiple strings together.
  - **Syntax**: `$sys.func.CONCATENATE(string1, string2, ...)`
  - **Example**: `$sys.func.CONCATENATE("Hello, ", "world!")` results in `"Hello, world!"`.

- **SUBSTITUTE**: Replaces occurrences of a pattern within a string.
  - **Syntax**: `$sys.func.SUBSTITUTE(originalString, pattern, replacement)`
  - **Example**: `$sys.func.SUBSTITUTE("I like cats", "cats", "dogs")` results in `"I like dogs"`.

- **SPLIT**: Splits a string into a list based on a delimiter.
  - **Syntax**: `$sys.func.SPLIT(string, delimiter)`
  - **Example**: `$sys.func.SPLIT("apple,banana,cherry", ",")` results in `["apple", "banana", "cherry"]`.

- **JOIN**: Joins elements of a list into a string using a delimiter.
  - **Syntax**: `$sys.func.JOIN(delimiter, list, finalDelimiter)`
    - **FinalDelimiter** (optional): Used before the last element.
  - **Example**: `$sys.func.JOIN(", ", ["Alice", "Bob", "Charlie"], ", and ")` results in `"Alice, Bob, and Charlie"`.

- **UPPER**: Converts a string to uppercase.
  - **Syntax**: `$sys.func.UPPER(string)`
  - **Example**: `$sys.func.UPPER("hello")` results in `"HELLO"`.

- **LOWER**: Converts a string to lowercase.
  - **Syntax**: `$sys.func.LOWER(string)`
  - **Example**: `$sys.func.LOWER("HELLO")` results in `"hello"`.

- **LEN**: Returns the length of a string.
  - **Syntax**: `$sys.func.LEN(string)`
  - **Example**: `$sys.func.LEN("Dialogflow")` results in `10`.

- **MID**: Extracts a substring from a string.
  - **Syntax**: `$sys.func.MID(string, startPosition, length)`
    - **StartPosition**: 1-indexed position to start extraction.
  - **Example**: `$sys.func.MID("Dialogflow", 2, 4)` results in `"ialo"`.

- **URL_ENCODE**: Encodes a string for use in a URL.
  - **Syntax**: `$sys.func.URL_ENCODE(string)`
  - **Example**: `$sys.func.URL_ENCODE("a+b=c")` results in `"a%2Bb%3Dc"`.

#### **3. List Functions**

- **APPEND**: Adds elements to the end of a list.
  - **Syntax**: `$sys.func.APPEND(list, value1, value2, ...)`
  - **Example**: `$sys.func.APPEND([1, 2], 3, 4)` results in `[1, 2, 3, 4]`.

- **REMOVE**: Removes elements from a list.
  - **Syntax**: `$sys.func.REMOVE(list, value1, value2, ...)`
  - **Example**: `$sys.func.REMOVE([1, 2, 3, 2], 2)` results in `[1, 3]`.

- **UNIQUE**: Removes duplicate elements from a list.
  - **Syntax**: `$sys.func.UNIQUE(list)`
  - **Example**: `$sys.func.UNIQUE([1, 2, 2, 3])` results in `[1, 2, 3]`.

- **COUNT**: Returns the number of elements in a list.
  - **Syntax**: `$sys.func.COUNT(list)`
  - **Example**: `$sys.func.COUNT([1, 2, 3])` results in `3`.

- **GET**: Retrieves an element from a list by index.
  - **Syntax**: `$sys.func.GET(list, index)`
    - **Index**: 0-based index of the element.
  - **Example**: `$sys.func.GET(["a", "b", "c"], 1)` results in `"b"`.

- **CONTAIN**: Checks if a list contains a specific element.
  - **Syntax**: `$sys.func.CONTAIN(list, value)`
  - **Example**: `$sys.func.CONTAIN([1, 2, 3], 2)` results in `true`.

- **MATCH**: Finds the index of an element in a list.
  - **Syntax**: `$sys.func.MATCH(list, value)`
  - **Example**: `$sys.func.MATCH(["x", "y", "z"], "y")` results in `1`.

#### **4. Date and Time Functions**

- **NOW**: Returns the current date and time.
  - **Syntax**: `$sys.func.NOW()`
  - **Example**: Produces a datetime object representing the current time.

- **FORMAT_DATE**: Formats a date/time object into a string.
  - **Syntax**: `$sys.func.FORMAT_DATE(datetime, format, language)`
    - **Language** (optional): Language code for localization (default is "en").
  - **Example**: `$sys.func.FORMAT_DATE($session.params.date, "yyyy-MM-dd")` might result in `"2023-10-22"`.

- **ADD_DATE**: Adds or subtracts time units from a date/time object.
  - **Syntax**: `$sys.func.ADD_DATE(datetime, value, unit)`
    - **Unit**: `"YEARS"`, `"MONTHS"`, `"DAYS"`, `"HOURS"`, etc.
  - **Example**: `$sys.func.ADD_DATE($session.params.date, 7, "DAYS")` adds 7 days to the date.

- **IS_PAST_DATE**: Checks if a date/time is in the past.
  - **Syntax**: `$sys.func.IS_PAST_DATE(datetime)`
  - **Example**: `$sys.func.IS_PAST_DATE($session.params.date)` returns `true` if the date is before the current date.

- **IS_FUTURE_DATE**: Checks if a date/time is in the future.
  - **Syntax**: `$sys.func.IS_FUTURE_DATE(datetime)`
  - **Example**: `$sys.func.IS_FUTURE_DATE($session.params.date)` returns `true` if the date is after the current date.

#### **5. Conditional Functions**

- **IF**: Evaluates a condition and returns one of two values.
  - **Syntax**: `$sys.func.IF("condition", valueIfTrue, valueIfFalse)`
  - **Example**: `$sys.func.IF("5 > 3", "Yes", "No")` results in `"Yes"`.

#### **6. Conversion Functions**

- **TO_TEXT**: Converts a value to a string.
  - **Syntax**: `$sys.func.TO_TEXT(value)`
  - **Example**: `$sys.func.TO_TEXT(123)` results in `"123"`.

- **TO_NUMBER**: Converts a value to a number.
  - **Syntax**: `$sys.func.TO_NUMBER(value)`
  - **Example**: `$sys.func.TO_NUMBER("45")` results in `45`.

- **TO_OBJECT**: Converts a JSON string to an object.
  - **Syntax**: `$sys.func.TO_OBJECT(jsonString)`
  - **Example**: `$sys.func.TO_OBJECT("{'key':'value'}")` results in an object with a key-value pair.

- **TO_PHONE_NUMBER**: Parses a phone number string into its components.
  - **Syntax**: `$sys.func.TO_PHONE_NUMBER(phoneNumber, regionCode)`
  - **Example**: `$sys.func.TO_PHONE_NUMBER("+16502065555")` results in an object with country code, area code, and number.

#### **7. Utility Functions**

- **RAND**: Generates a random floating-point number between 0 (inclusive) and 1 (exclusive).
  - **Syntax**: `$sys.func.RAND()`
  - **Example**: Might result in `0.726`.

- **IDENTITY**: Returns the input value without any conversion.
  - **Syntax**: `$sys.func.IDENTITY(value)`
  - **Example**: Useful for retaining the data type when assigning parameters.

- **GET_FIELD**: Retrieves a value from an object using a key.
  - **Syntax**: `$sys.func.GET_FIELD(object, key)`
  - **Example**: `$sys.func.GET_FIELD($session.params.user, "name")` might result in `"Alice"`.

- **FILTER**: Extracts values from lists or objects using JsonPath expressions.
  - **Syntax**: `$sys.func.FILTER(parameterReference, jsonPathExpression)`
  - **Example**: Can be used to filter items in a list based on certain conditions.

#### **8. Validation Functions**

- **IS_PHONE_NUMBER**: Validates if a string is a valid phone number.
  - **Syntax**: `$sys.func.IS_PHONE_NUMBER(phoneNumber, regionCode)`
  - **Example**: `$sys.func.IS_PHONE_NUMBER("650-206-5555", "US")` returns `true`.

- **IS_DATE**: Validates if a string can be parsed into a date.
  - **Syntax**: `$sys.func.IS_DATE(dateString, format, language)`
  - **Example**: `$sys.func.IS_DATE("2021-04-29", "yyyy-MM-dd")` returns `true`.

- **IS_CREDIT_CARD_NUMBER**: Checks if a number is a valid credit card number using the Luhn algorithm.
  - **Syntax**: `$sys.func.IS_CREDIT_CARD_NUMBER(cardNumber)`
  - **Example**: `$sys.func.IS_CREDIT_CARD_NUMBER("4111111111111111")` returns `true`.

---

### **Best Practices**

- **Error Handling**: Be mindful that some functions can produce errors (e.g., division by zero). Always validate inputs or use conditional functions to handle potential errors gracefully.

- **Data Types**: Ensure that the arguments passed to functions are of the expected data types. Use conversion functions like `TO_TEXT` or `TO_NUMBER` when necessary.

- **Parameter References**: When referencing parameters, use the correct syntax (e.g., `$session.params.parameterName`). Remember that if a parameter is not set, it is treated as `null`.

- **Nested Functions**: You can nest functions within other functions to perform complex operations. Ensure that nested functions are properly formatted and that their outputs are compatible with the parent function.

---

### **Examples in Practice**

**Creating a Dynamic Greeting Message:**

```plaintext
"Hello, $sys.func.UPPER($session.params.userName)! Welcome back."
```

If `$session.params.userName` is `"alice"`, the output will be:

```plaintext
"Hello, ALICE! Welcome back."
```

**Calculating Total Price with Tax:**

```plaintext
$sys.func.MULTIPLY($session.params.price, 1.08)
```

If `$session.params.price` is `50`, the total price including 8% tax will be `54`.

**Validating and Formatting a Phone Number:**

```plaintext
$sys.func.IF(
  "$sys.func.IS_PHONE_NUMBER($session.params.phoneNumber, 'US')",
  "Your number is valid.",
  "Please provide a valid phone number."
)
```

---

### **Conclusion**

System functions in Dialogflow CX empower you to create more dynamic and intelligent conversational agents. By leveraging these functions, you can manipulate data, perform calculations, and control the flow of conversations based on real-time inputs and conditions. Understanding how to effectively use system functions will enhance your agent's capabilities and improve the user experience.

If you need more specific information about each function, consider referring to the official Dialogflow CX documentation or experimenting with functions in your agent's test console.

In **Dialogflow CX**, a **conditional response** is used to dynamically generate different responses based on specific conditions during the conversation. The format allows you to implement logic similar to **if-else** statements, helping tailor responses based on the values of session parameters, user input, or other session-related data.

### **General Format of Conditional Response**
The general syntax for conditional responses is as follows:

```plaintext
if [condition]
  [response]
elif [condition]
  [response]
elif [condition]
  [response]
else
  [response]
endif
```

- **[condition]**: This is the condition that is evaluated. It follows the same format as **route conditions**, which determine whether a condition is true or false based on session parameters or other variables.
- **[response]**: This is the text or response that is returned if the condition evaluates to `true`.

### **Key Points**
- The **if** block evaluates the first condition. If it's true, the corresponding response is returned.
- If the first condition is false, the **elif** blocks (if any) are evaluated in order, and if one is true, its response is used.
- If none of the conditions are true, the **else** block (if provided) is executed.
- **`elif`** and **`else`** blocks are optional.
- You must end the conditional block with `endif`.

### **Example**

Consider an example where you want to determine if a user is old enough to enter a certain event:

```plaintext
if $session.params.user-age >= 21
  Ok, you may enter.
else
  Sorry, you cannot enter.
endif
```

- If the user's age (stored in `$session.params.user-age`) is 21 or above, the response will be:
  - **"Ok, you may enter."**
- If the user's age is below 21, the response will be:
  - **"Sorry, you cannot enter."**

### **Using System Functions in Conditions**
The condition can include system functions to dynamically generate values or evaluate more complex expressions. For example:

```plaintext
if $sys.func.LOWER($session.params.city) == "new york"
  Welcome to New York!
else
  Welcome to our site!
endif
```
Here, the **LOWER** function is used to convert the user’s input (city) to lowercase, ensuring that the condition is case-insensitive.

### **Using System Functions in Responses**
You can also use system functions to generate dynamic responses:

```plaintext
if $session.params.temperature > 30
  It’s $sys.func.TO_TEXT($session.params.temperature) degrees. Stay cool!
else
  The temperature is $sys.func.TO_TEXT($session.params.temperature) degrees. Enjoy the weather!
endif
```

In this example, **TO_TEXT** is used to convert the temperature value into a string that is included in the response.

### **Session State and Evaluation Timing**
- The **condition** is evaluated based on the **session state** at the **beginning** of the fulfillment.
- The **response** is generated after the condition is resolved, and it can use the updated session state after the fulfillment.
  
### **Multilingual Support**
- For **multilingual agents**, the **condition** is the same for all languages. 
- The **response** is specific to each language, so if you update the condition, the response for other languages will be reset (cleared), except for the language in which you updated the condition.

### **Example with Multilingual Responses**

For a multilingual agent in English and Spanish:

- **Condition** (common to both languages):
  ```plaintext
  if $session.params.user-age >= 21
  ```

- **English Response**:
  ```plaintext
  Ok, you may enter.
  ```

- **Spanish Response**:
  ```plaintext
  Está bien, puedes entrar.
  ```

If you update the condition in one language, the condition stays the same across all languages, but the response in other languages is cleared and needs to be set again.

---

### **Conclusion**

**Conditional responses** in Dialogflow CX are a powerful way to deliver dynamic, customized responses based on user input and session data. By using conditional logic and system functions, you can adapt your agent's responses to meet specific criteria and enhance the conversational experience.