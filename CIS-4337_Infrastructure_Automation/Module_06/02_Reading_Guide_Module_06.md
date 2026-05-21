# Reading Guide: Module 06 - Data Sources and Terraform Functions
## Course: CIS-4337_Infrastructure_Automation (HashiCorp Certified: Terraform Associate)

---

### Introduction
Welcome to **Module 06 - Data Sources and Terraform Functions**! This week's study material covers two powerful HCL features: **data sources**, which let you query existing infrastructure without managing it, and **built-in functions**, which let you manipulate strings, lists, maps, and numbers directly inside your configuration. Both are tested on the **HashiCorp Certified: Terraform Associate** certification exam.

As a student, you will learn how `data` blocks differ from `resource` blocks, how to reference data source outputs in resource arguments, and how to apply functions like `lookup()`, `join()`, `element()`, `file()`, and conditional expressions to write more dynamic configurations. Make sure to complete the checklists and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Data source (`data` block)**: A read-only query that fetches information from a provider or external source without creating or managing the resource. The syntax is `data "<TYPE>" "<NAME>" { ... }` and the result is referenced as `data.<TYPE>.<NAME>.<ATTRIBUTE>`. Common uses: look up an existing AMI ID, fetch a VPC ID by tag, or read a Secrets Manager value. Data sources are refreshed on every `terraform plan`.
*   **Data source vs. resource**: A `resource` block tells Terraform to create and manage an object's lifecycle. A `data` block only reads existing objects and makes their attributes available. Deleting a `data` block from config does not destroy any real infrastructure — it just stops Terraform from reading it. The exam frequently tests this distinction.
*   **`lookup(map, key, default)`**: A built-in Terraform function that retrieves the value associated with a key from a map variable. If the key does not exist, it returns the default value. Example: `lookup(var.amis, var.region, "ami-default")`. The exam tests `lookup()` as the canonical way to retrieve a value from a map with a fallback.
*   **`element(list, index)`**: Returns the item at the given index from a list. If the index is out of bounds, it wraps around using modulo arithmetic. Example: `element(["a","b","c"], 1)` returns `"b"`. This function is frequently used for round-robin resource distribution across availability zones.
*   **Conditional expression**: HCL ternary syntax: `condition ? true_value : false_value`. Example: `var.env == "prod" ? "t3.large" : "t3.micro"`. This is the Terraform equivalent of an if-else and is heavily tested for scenarios where resource sizing or naming varies by environment.

---

### 2. Certification Exam Tips
*   **Exam Domain — Use Terraform Outside the Core Workflow (Domain 6):** Functions and data sources appear throughout the Associate exam. The exam expects you to know the correct function names and signatures — `lookup`, `element`, `join`, `split`, `length`, `toset`, `tolist`, `file`, `base64encode` are the most commonly tested.
*   **`terraform console` for function testing:** The `terraform console` command launches an interactive REPL where you can test function calls directly (e.g., type `lookup({a="1"}, "a", "none")` to verify the result). The exam may ask what command you use to interactively test HCL expressions.
*   **`file()` function security trap:** The `file()` function reads a local file and returns its contents as a string. It is commonly used for `user_data` scripts. Be aware that `file()` reads at plan time from the local machine — if a path does not exist, `terraform plan` will fail. The exam may present a scenario with a missing file path.
*   **Data source refresh behavior:** By default, Terraform refreshes all data sources during `terraform plan`. This can cause issues if a data source depends on a resource that does not yet exist. In such cases, use `depends_on` inside the `data` block to sequence the dependency correctly. The exam tests this pattern.
*   **Study Resource:** The full list of built-in Terraform functions with examples is documented at [HashiCorp Terraform Documentation — Functions](https://developer.hashicorp.com/terraform/language/functions). The data sources documentation is at [HashiCorp Terraform Documentation — Data Sources](https://developer.hashicorp.com/terraform/language/data-sources).

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the data sources and functions documentation at [HashiCorp Terraform Documentation & Tutorials](https://developer.hashicorp.com/terraform/language/data-sources). The free functions reference page lists all built-in functions with examples — bookmark it for the exam.
*   **Required Video:** Watch the video lecture on **Data Sources and Functions** in the official course playlist: [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA). Focus on the sections demonstrating `data` block syntax and `terraform console` function testing.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Declare a `data` block to fetch an existing resource**: Write a `data "aws_ami" "latest"` or `data "local_file" "config"` block and reference its attribute in a resource argument. Observe that no new infrastructure is created.
*   **Test HCL functions in `terraform console`**: Launch `terraform console`, test `lookup()`, `join()`, and a conditional expression. Verify outputs match expected values before using them in resource configurations.
*   **Use a conditional expression to set an instance type based on a variable**: Write `instance_type = var.env == "prod" ? "t3.large" : "t3.micro"` and apply with different variable values to observe the result.

---

### 3. Study Checklist
*   [ ] Read the glossary terms and understand each definition well enough to explain it in your own words.
*   [ ] Read the data sources documentation at [HashiCorp Terraform Documentation & Tutorials](https://developer.hashicorp.com/terraform/language/data-sources).
*   [ ] Watch the video lecture on **Data Sources and Functions** in [HashiCorp Terraform Associate Complete Course](https://www.youtube.com/watch?v=V53S9wB5SgA).
*   [ ] Review the commands outlined in the lab instructions.
*   [ ] Proceed to the weekly hands-on lab activity.
