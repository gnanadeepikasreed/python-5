
# Multi-Plan Telecommunications Cost Optimization

# Number of mobile plans
n = int(input("Enter number of mobile plans: "))

# User requirements
print("\nEnter your monthly requirements")

required_data = float(input("Enter required data in GB: "))
required_calls = int(input("Enter required call minutes: "))
required_validity = int(input("Enter required validity in days: "))
budget = float(input("Enter your budget: "))

# Lists to store plan details
plan_names = []
total_costs = []
eligible_plans = []

for i in range(n):

    print("\nEnter details of Plan", i + 1)

    name = input("Enter plan name: ")
    price = float(input("Enter plan price: "))
    data = float(input("Enter data limit in GB: "))
    calls = int(input("Enter call minutes: "))
    validity = int(input("Enter validity in days: "))

    extra_data_rate = float(
        input("Enter extra data charge per GB: ")
    )

    extra_call_rate = float(
        input("Enter extra call charge per minute: ")
    )

    # Validate plan details
    if (price < 0 or data < 0 or calls < 0 or
        validity <= 0 or extra_data_rate < 0 or
        extra_call_rate < 0):

        print("Invalid plan details!")
        continue

    # Calculate excess usage charges
    if required_data > data:
        extra_data = required_data - data
    else:
        extra_data = 0

    if required_calls > calls:
        extra_calls = required_calls - calls
    else:
        extra_calls = 0

    data_charge = extra_data * extra_data_rate
    call_charge = extra_calls * extra_call_rate

    # Calculate total cost
    total_cost = price + data_charge + call_charge

    plan_names.append(name)
    total_costs.append(total_cost)

    print("\nPlan:", name)
    print("Base Price: Rs.", price)
    print("Extra Data Charge: Rs.", data_charge)
    print("Extra Call Charge: Rs.", call_charge)
    print("Total Cost: Rs.", round(total_cost, 2))

    # Check eligibility
    if (validity >= required_validity and
        total_cost <= budget):

        print("Status: Eligible")

        # Store eligible plan as a tuple
        plan = (name, total_cost, validity)
        eligible_plans.append(plan)

    else:
        print("Status: Not Eligible")


# Find the most economical eligible plan
print("\n========== PLAN COMPARISON ==========")

if len(eligible_plans) == 0:

    print("No eligible mobile plans found.")

else:

    # Sort plans by total cost
    eligible_plans.sort(key=lambda x: (x[1], -x[2]))

    print("\nEligible Plans:")

    for name, cost, validity in eligible_plans:

        print("\nPlan Name:", name)
        print("Total Cost: Rs.", round(cost, 2))
        print("Validity:", validity, "days")

    # Display best plan
    best_plan = eligible_plans[0]

    print("\n========== BEST MOBILE PLAN ==========")
    print("Plan Name:", best_plan[0])
    print("Total Cost: Rs.", round(best_plan[1], 2))
    print("Validity:", best_plan[2], "days")

    print("This is the most economical eligible plan.")

print("\nPlan Optimization Completed!")
