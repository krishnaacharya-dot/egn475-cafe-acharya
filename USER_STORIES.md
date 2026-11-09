# Café Calle Ocho --- User Stories and Acceptance Criteria

**Course:** EGN 475\
**Assignment:** Week 2 Assignment 2.1 --- User Stories and Acceptance
Criteria\
**Student:** Krishna Acharya\
**Repository:** `egn475-cafe-acharya`\
**Technology:** Python Flask\
**Branch:** `main`

## 1. Project overview

Café Calle Ocho is a Flask-based café ordering prototype. Customers can
browse available menu items, submit orders, and check order progress.
Café staff can view incoming orders, update preparation status, and
manage menu availability.

## 2. Personas

-   **Marta Rivera --- Customer:** Needs to browse the menu, place an
    order, check its status, and review previous orders.
-   **Luis García --- Café/kitchen staff:** Needs to view active orders,
    update preparation status, and manage menu availability.

## 3. Scope assumptions

1.  After a successful order submission, the system generates a unique
    order number. A customer can use that number to look up the specific
    order.
2.  For order history, the prototype associates orders with a customer
    identifier, such as the email address supplied at checkout. The same
    identifier is used to retrieve that customer's previous orders.
3.  Staff-only actions require staff permission.
4.  The order workflow uses these statuses: **Received → Preparing →
    Ready**.

## 4. User stories and acceptance criteria

### US-01 --- Browse the menu

**Priority:** Must have

As a customer, I want to view the café's available menu items, so that I
can decide what to order.

**Acceptance criteria**

-   **AC1 --- Success:** Given the menu contains available items, when
    Marta opens the menu, then the system displays each available item's
    name, description, and price.
-   **AC2 --- Empty state:** Given no menu items are currently
    available, when Marta opens the menu, then the system displays a
    clear message that no items are available.

### US-02 --- Submit an order

**Priority:** Must have

As a customer, I want to submit an order containing items already
selected in my order cart, so that I can purchase food from the café.

**Acceptance criteria**

-   **AC1 --- Success:** Given Marta's cart contains at least one
    available item and the required checkout information is valid, when
    she submits the order, then the system creates one order, assigns it
    a unique order number, and displays an order confirmation.
-   **AC2 --- Validation/error:** Given Marta's cart is empty or
    contains an item that has become unavailable, when she attempts to
    submit the order, then the system displays a validation message,
    does not create the order, and identifies the issue that must be
    corrected.

### US-03 --- Check order status

**Priority:** Must have

As a customer, I want to see the status of my order using its unique
order number, so that I know whether it has been received, is being
prepared, or is ready for pickup.

**Acceptance criteria**

-   **AC1 --- Success:** Given Marta has a valid order number, when she
    looks up the order, then the system displays the order's current
    status as **Received**, **Preparing**, or **Ready**.
-   **AC2 --- Invalid input/privacy:** Given Marta enters an order
    number that does not match an existing order, when she looks up the
    order, then the system displays an order-not-found message and does
    not display another customer's order.

### US-04 --- View previous orders

**Priority:** Should have

As a customer, I want to view previous orders associated with my
customer identifier, so that I can review what I ordered before.

**Acceptance criteria**

-   **AC1 --- Success:** Given Marta has completed orders associated
    with the customer identifier she provides, when she opens order
    history, then the system displays those orders with their dates,
    order numbers, and totals.
-   **AC2 --- Empty state:** Given no previous orders are associated
    with the provided customer identifier, when Marta opens order
    history, then the system displays a message stating that no previous
    orders were found.

### US-05 --- View incoming orders

**Priority:** Must have

As a kitchen staff member, I want to view incoming active customer
orders in chronological order, so that I can prepare them in the order
they were received.

**Acceptance criteria**

-   **AC1 --- Success:** Given active customer orders exist, when Luis
    opens the kitchen board, then the system displays each active
    order's order number, items, submission time, and status, with the
    oldest order first.
-   **AC2 --- Empty state:** Given there are no active orders, when Luis
    opens the kitchen board, then the system displays a message
    indicating that no active orders are available.

### US-06 --- Move an order into preparation

**Priority:** Must have

As a kitchen staff member, I want to change an order's status from
**Received** to **Preparing**, so that the system reflects when staff
begin preparing it.

**Acceptance criteria**

-   **AC1 --- Success:** Given an order has the status **Received** and
    Luis has staff permission, when Luis selects **Preparing**, then the
    system changes the order status to **Preparing** and displays the
    updated status.
-   **AC2 --- Invalid transition/permission:** Given an order is not in
    **Received** status or the user does not have staff permission, when
    that user attempts this update, then the system rejects the change
    and leaves the order status unchanged.

### US-07 --- Manage menu availability

**Priority:** Should have

As a café staff member, I want to mark menu items as available or sold
out, so that customers do not order unavailable products.

**Acceptance criteria**

-   **AC1 --- Success:** Given a menu item is available and Luis has
    staff permission, when Luis marks it as sold out, then the item is
    no longer offered for new orders.
-   **AC2 --- Invalid item/permission:** Given the selected menu item
    does not exist or the user lacks staff permission, when an
    availability change is attempted, then the system displays an error
    and makes no changes.

### US-08 --- Mark an order ready

**Priority:** Must have

As a kitchen staff member, I want to change an order's status from
**Preparing** to **Ready**, so that the customer knows the food is ready
for pickup.

**Acceptance criteria**

-   **AC1 --- Success:** Given an order has the status **Preparing** and
    Luis has staff permission, when Luis marks it **Ready**, then the
    system changes the status to **Ready** and makes the updated status
    available for the customer to view.
-   **AC2 --- Invalid transition/permission:** Given an order is not in
    **Preparing** status or the user does not have staff permission,
    when that user attempts to mark it **Ready**, then the system
    rejects the change and leaves the existing status unchanged.

## 5. Priority summary

  Priority      Story IDs                                    Count
  ------------- ------------------------------------------ -------
  Must have     US-01, US-02, US-03, US-05, US-06, US-08         6
  Should have   US-04, US-07                                     2
  Could have    None                                             0

## 6. INVEST review --- GitHub Copilot feedback

The following issues were reported in the Copilot review:

-   **US-02 --- Estimable / Small:** Combines selecting menu items and
    submitting an order; the boundaries of the ordering flow are
    unclear, making the scope difficult to estimate.
-   **US-03 --- Testable:** "Current status" does not specify which
    statuses customers can see or what qualifies as an order's current
    status.
-   **US-04 --- Independent / Testable:** It assumes a way to identify
    which past orders belong to the customer, but that mechanism is
    unspecified. Without it, the expected order history is unclear to
    test.
-   **US-05 --- Testable:** "Correct sequence" does not define the
    ordering rule (for example, chronological or by priority), so it is
    unclear how to verify the sequence.
-   **US-06 --- Vague / Testable:** "Preparation status" does not define
    the statuses or allowed transitions. It also overlaps with US-08,
    which specifically marks an order Ready, leaving the boundary
    between the two stories unclear.
-   **US-08 --- Independent:** Its Ready action appears to be a specific
    part of the status-updating behavior in US-06, so its relationship
    to that story is unclear.

## 7. Feedback decisions and revisions

-   **US-02 --- Accepted:** Narrowed the story to submitting a cart that
    has already been prepared. The acceptance criteria specify a
    non-empty cart, item availability, valid checkout information, and a
    generated order number. This makes the story's boundary clearer.
-   **US-03 --- Accepted:** Defined the customer-visible statuses as
    Received, Preparing, and Ready. The invalid-order-number criterion
    also verifies that another customer's order is not exposed.
-   **US-04 --- Accepted:** Specified that order history is associated
    with a customer identifier supplied by the customer. The acceptance
    criteria cover both matching orders and an empty history.
-   **US-05 --- Accepted:** Defined the queue rule as chronological
    order, oldest first, and included submission time in the displayed
    order details.
-   **US-06 --- Accepted:** Limited this story to the
    Received-to-Preparing transition and specified that invalid
    transitions and unauthorized updates are rejected.
-   **US-08 --- Partially accepted:** Retained this as a separate story
    because marking an order Ready is a distinct workflow step with a
    customer-visible result. Clarified that it covers only the
    Preparing-to-Ready transition, while US-06 covers
    Received-to-Preparing.

The revised order workflow is **Received → Preparing → Ready**. The two
staff stories cover separate transitions rather than duplicating the
same action.

## 8. Reflection questions

### Question 1: Which story did you split, and why?

I separated the original idea of placing an order and checking its
progress into **US-02 (Submit an Order)** and **US-03 (Check Order
Status)**. These are two different customer goals. Submitting an order
creates a new transaction, while checking its status retrieves
information about an existing transaction. Keeping them separate makes
each story easier to estimate, implement, and test independently.

### Question 2: Which story was hardest to write acceptance criteria for, and why?

**US-02 (Submit an Order)** was the hardest story because a successful
order depends on several conditions: the cart must contain at least one
item, the items must still be available, and the required checkout
information must be valid. The system must also prevent an invalid or
empty order from being created. Writing separate success and error
criteria helped make these conditions clear and testable.

## 9. Final repository and submission checklist

-   [ ] Save this file in the repository root as `USER_STORIES.md`.
-   [ ] Verify the stories, priorities, and acceptance criteria match
    the final assignment.
-   [ ] Keep the actual GitHub Copilot Chat review response as
    assignment evidence or in the course-required AI log.
-   [ ] Commit and push the file to the `main` branch.
-   [ ] Submit the repository link and the assignment document/PDF
    through Online Campus.

**Repository URL:**
`https://github.com/krishnaacharya-dot/egn475-cafe-acharya`

**Important:** This file records the Copilot feedback supplied for the
review. Confirm that the original Copilot response is retained as
evidence, and do not mark the GitHub upload or push checklist items
complete until you have actually done them.
