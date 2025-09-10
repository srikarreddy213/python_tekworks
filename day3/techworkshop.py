def tech_report():
    n1 = int(input("Enter number of members day1: "))
    l1 = [input() for _ in range(n1)]

    n2 = int(input("Enter number of members day2: "))
    l2 = [input() for _ in range(n2)]

    n3 = int(input("Enter number of members day3: "))
    l3 = [input() for _ in range(n3)]

    s1, s2, s3 = set(l1), set(l2), set(l3)

    exactly_one_day = (s1 - s2 - s3) | (s2 - s1 - s3) | (s3 - s1 - s2)
    day1_day2 = s1 & s2
    day2_day3 = s2 & s3
    day1_day3 = s1 & s3

    print("\n--- Attendance Report ---")
    print(f"Attendees who attended exactly one day ({len(exactly_one_day)}): {sorted(exactly_one_day)}")
    print(f"Day1 & Day2 overlap ({len(day1_day2)}): {sorted(day1_day2)}")
    print(f"Day2 & Day3 overlap ({len(day2_day3)}): {sorted(day2_day3)}")
    print(f"Day1 & Day3 overlap ({len(day1_day3)}): {sorted(day1_day3)}")
    print(f"Attendees all 3 days ({len(s1 & s2 & s3)}): {sorted(s1 & s2 & s3)}")
    print(f"Total unique attendees across all days ({len(s1 | s2 | s3)}): {sorted(s1 | s2 | s3)}")

tech_report()
