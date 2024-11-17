import csv

# Data for the US Civil War Q&A
questions_answers = [
    ["Question", "Answer"],
    ["What years did the Cold War span?", "1947 to 1991"],
    ["What were the two main opposing powers during the Cold War?", "The United States and the Soviet Union"],
    ["What ideological conflict defined the Cold War?", "Capitalism vs. Communism"],
    ["What event symbolized the start of the Cold War?", "The Truman Doctrine and the Iron Curtain speech"],
    ["What major conflict occurred in Vietnam during the Cold War?", "The Vietnam War"],
    ["Which country did the US support in the Vietnam War?", "South Vietnam"],
    ["What was the main objective of the Viet Cong?", "To unify Vietnam under communist rule"],
    ["What was the Tet Offensive?", "A major coordinated attack by North Vietnamese forces in 1968"],
    ["Why did the US withdraw from Vietnam?", "Due to mounting public pressure and high costs"],
    ["What was the result of the Vietnam War?", "Vietnam was unified under communist rule in 1975"],
    ["What was the Soviet-Afghan War?", "A conflict where the USSR invaded Afghanistan to support a communist government"],
    ["What was the role of the US in the Soviet-Afghan War?", "The US supported Afghan mujahideen rebels"],
    ["What impact did the Soviet-Afghan War have on the USSR?", "It weakened the Soviet economy and morale, contributing to its collapse"],
    ["Who were the mujahideen?", "Afghan guerrilla fighters opposed to the Soviet invasion"],
    ["What was the result of the Soviet-Afghan War?", "The Soviet Union withdrew, and Afghanistan fell into civil war"],
    ["What were the proxy wars in South America during the Cold War?", "Conflicts in countries like Nicaragua, El Salvador, and Chile"],
    ["What was Operation Condor?", "A campaign by South American dictatorships to suppress left-wing movements"],
    ["Who were the Contras?", "US-backed rebel groups fighting the Sandinista government in Nicaragua"],
    ["What was the US's involvement in Chile during the Cold War?", "The US supported the coup against President Salvador Allende"],
    ["What was the Cuban Missile Crisis?", "A standoff over Soviet missiles in Cuba in 1962"],
    ["How was the Cuban Missile Crisis resolved?", "The USSR agreed to remove missiles in exchange for US concessions"],
    ["What was the Berlin Airlift?", "A US-led operation to supply West Berlin during the Soviet blockade"],
    ["What was the significance of the Berlin Wall?", "It symbolized the division between East and West during the Cold War"],
    ["When was the Berlin Wall constructed?", "1961"],
    ["When did the Berlin Wall fall?", "1989"],
    ["What was the purpose of NATO during the Cold War?", "To counter Soviet influence in Europe"],
    ["What was the Warsaw Pact?", "A military alliance of communist states led by the USSR"],
    ["What was the Korean War?", "A conflict between North and South Korea, involving the US and China"],
    ["Why did the US intervene in the Korean War?", "To stop the spread of communism"],
    ["What was the outcome of the Korean War?", "An armistice that divided Korea at the 38th parallel"],
    ["What was the Space Race?", "A competition between the US and USSR for dominance in space exploration"],
    ["Who launched the first artificial satellite?", "The USSR, with Sputnik in 1957"],
    ["What was the US's response to Sputnik?", "The creation of NASA and increased investment in science education"],
    ["What was the role of espionage during the Cold War?", "Both sides used spies to gather intelligence"],
    ["What was the U-2 incident?", "A US spy plane was shot down over the USSR in 1960"],
    ["What was détente?", "A period of eased tensions between the US and USSR in the 1970s"],
    ["What was the Strategic Arms Limitation Treaty (SALT)?", "An agreement to limit nuclear weapons"],
    ["What was the impact of the Cold War on developing nations?", "Many were drawn into proxy wars or forced to align with a superpower"],
    ["What was the Reagan Doctrine?", "A policy of supporting anti-communist insurgencies"],
    ["What role did the United Nations play during the Cold War?", "It mediated conflicts and provided a platform for diplomacy"],
    ["What was the Arms Race?", "A competition to build more advanced and numerous nuclear weapons"],
    ["What was the significance of the Marshall Plan?", "US aid to rebuild Europe and counter communism"],
    ["What was the role of propaganda during the Cold War?", "Both sides used media to promote their ideologies"],
    ["What was the Iron Curtain?", "A metaphorical division between Eastern and Western Europe"],
    ["What was the Prague Spring?", "A 1968 movement in Czechoslovakia for political liberalization, crushed by the USSR"],
    ["How did the Cold War end?", "The dissolution of the Soviet Union in 1991"],
    ["What was Glasnost?", "A policy of openness introduced by Mikhail Gorbachev"],
    ["What was Perestroika?", "A policy of economic restructuring in the USSR"],
    ["What is meant by 'Cold War by proxy'?", "Conflicts where the superpowers supported opposing sides without direct confrontation"],
]

# Creating the CSV file
csv_file_path = "D:/csv file creator/Cold_war_qs.csv"
with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Question", "Answer"])
    writer.writerows(questions_answers)

csv_file_path
