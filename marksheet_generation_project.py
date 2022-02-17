# USER DATA

def user_data(Academic_Year,UIC,Programme,SEM,Student_Name,Mother_Name,RN,DOB,Gender):     
    return Academic_Year,UIC,Programme,SEM,Student_Name,Mother_Name,RN,DOB,Gender

AY,UIC,Pro,SEM,SN,MN,RN,DOB,Gender = user_data(input("Academic Year : "),int(input("Registration No. : ")),input("Programme : "),input("SEM : "),input("Student Name : "),input("Mother Name : "),int(input("Roll No. : ")),input("Date of Birth : "),input("Gender : "))




print('''==============================================================================================
                                                                                                    ''')

print('''Enter Student Internal Marks in Between 0 - 40                    
                                                       ''')             # TA MARKS in Between 0 - 40

while True:
    S1 = int(input("Electronics Device Marks :"))
    if S1 >= 0 and S1 <= 40:
        break
    else:
        print("Wrong Input Enter Marks in Between 0 - 40")

while True:
    S2 = int(input("Lab : Electronics Device Marks : "))
    if S2 >=0 and S2 <= 40:
        break
    else:
        print("Wrong Input Enter Marks in Between 0 - 40")

while True:
    S3 = int(input("Digital Circuit Marks :"))
    if S3 >=0 and S3 <= 40:
        break
    else:
        print("Wrong Input Enter Marks in Between 0 - 40")

while True:
    S4 = int(input("Lab : Digital Circuit Marks :"))
    if S4 >=0 and S4 <= 40:
        break
    else:
        print("Wrong Input Enter Marks in Between 0 - 40")
while True:
    S5 = int(input("Electronics Measurements & Instrumentation Marks :"))
    if S5 >=0 and S5 <= 40:
        break
    else:
        print("Wrong Input Enter Marks in Between 0 - 40")

while True:
    S6 = int(input("Lab : Electronics Measurements & Instrumentation Marks :"))
    if S6 >=0 and S6 <= 40:
        break
    else:
        print("Wrong Input Enter Marks in Between 0 - 40")

while True:
    S7 = int(input("Network Analysis Marks :"))
    if S7 >=0 and S7 <= 40:
        break
    else:
        print("Wrong Input Enter Marks in Between 0 - 40")

while True:
    S8 = int(input("Lab : Network Analysis Marks :"))
    if S8 >=0 and S8 <= 40:
        break
    else:
        print("Wrong Input Enter Marks in Between 0 - 40")

while True:
    S9 = int(input("Engineering Mathematics III Marks :"))
    if S9 >=0 and S9 <= 40:
        break
    else:
        print("Wrong Input Enter Marks in Between 0 - 40")




print('''=====================================================================================================
                                                                                                              ''')

print('''Enter Student Theory Marks in Between 0 - 60
                                                     ''')                       # SEMESTER MARKS in Between 0 - 60

while True:
    s1 = int(input("Electronics Device Marks :"))                               # 01. Electronics Device ( ED )
    if s1 >= 0 and s1 <= 60:
        break
    else:
        print("Wrong Input Enter Marks in Between 0 - 60")

while True:
    s2 = int(input("Lab : Electronics Device Marks : "))                        # 02. Lab : Electronics Device ( Lab : ED )
    if s2 >=0 and s2 <= 60:
        break
    else:
        print("Wrong Input Enter Marks in Between 0 - 60")

while True:
    s3 = int(input("Digital Circuit Marks :"))                                  # 03. Digital Circuits ( DC )
    if s3 >=0 and s3 <= 60:
        break
    else:
        print("Wrong Input Enter Marks in Between 0 - 60")

while True:
    s4 = int(input("Lab : Digital Circuit Marks :"))                            # 04. Lab : Digital Circuits ( Lab : DC )
    if s4 >=0 and s4 <= 60:
        break
    else:
        print("Wrong Input Enter Marks in Between 0 - 60")

while True:
    s5 = int(input("Electronics Measurements & Instrumentation Marks :"))       # 05. Electronics Measurements & 
    if s5 >=0 and s5 <= 60:                                                     #     Instrumentation ( EMI )
        break
    else:
        print("Wrong Input Enter Marks in Between 0 - 60")

while True:
    s6 = int(input("Lab : Electronics Measurements & Instrumentation Marks :")) # 06. Lab : Electronics Measurements &     
    if s6 >=0 and s6 <= 60:                                                     #     Instrumentation ( Lab : EMI )
        break
    else:
        print("Wrong Input Enter Marks in Between 0 - 60")

while True:
    s7 = int(input("Network Analysis Marks :"))                                 # 07. Network Analysis ( NA )
    if s7 >=0 and s7 <= 60:
        break
    else:
        print("Wrong Input Enter Marks in Between 0 - 60")

while True:
    s8 = int(input("Lab : Network Analysis Marks :"))                           # 08. Lab : Network Analysis ( Lab : NA )
    if s8 >=0 and s8 <= 60:
        break
    else:
        print("Wrong Input Enter Marks in Between 0 - 60")

while True:
    s9 = int(input("Engineering Mathematics III Marks :"))                      # 09. Engineering Mathematics III ( EM III )
    if s9 >=0 and s9 <= 60:
        break
    else:
        print("Wrong Input Enter Marks in Between 0 - 60")

# ============================================================================================================================

# Total Marks of Each Subject( Out of 100 = T) = Internal TA ( Out of 40 = S ) + Semester Exam Marks ( Out of 60 = s) =  

T1 = S1 + s1                            # 01. ED
T2 = S2 + s2                            # 02. Lab : ED 
T3 = S3 + s3                            # 03. DC
T4 = S4 + s4                            # 04. Lab : DC
T5 = S5 + s5                            # 05. EMI
T6 = S6 + s6                            # 06. Lab : EMI
T7 = S7 + s7                            # 07. NA
T8 = S8 + s8                            # 08. Lab : NA
T9 = S9 + s9                            # 09. EM III

# ============================================================================================================================

# Grades ( G ) for Range of Marks 
# T>=90:"A" , 90>T>=80:"B" , 80>T>=72:"C" , 72>T>=64:"D" , 64>T>=56:"E" , 56>T>=48:"G" , 48>T>=40:"H" , 40>T:"F"
# Grade Points ( GP ) for for Grade
# A=10 , B=9 , C=8.25 , D=7.5 , E=6.75 , G=6 , H=5 , F=0   

# 01. Electronics Device
if T1 >= 90:
    G1 = "A"
    GP1 = 10
elif T1 >= 80 and T1 < 90:
    G1 = "B"
    GP1 = 9
elif T1 >= 72 and T1 < 80:
    G1 = "C"
    GP1 = 8.25
elif T1 >= 64 and T1 < 72:
    G1 = "D"
    GP1 = 7.5
elif T1 >= 56 and T1 < 64:
    G1 = "E"
    GP1 = 6.75
elif T1 >= 48 and T1 < 56:
    G1 = "G"
    GP1 = 6
elif T1 >= 40 and T1 < 48:
    G1 = "H"
    GP1 = 5
else:
    G1 = "F"
    GP1 = 0

# 02. Lab : Electronics Device
if T2 >= 90:
    G2 = "A"
    GP2 = 10
elif T2 >= 80 and T2 < 90:
    G2 = "B"
    GP2 = 9
elif T2 >= 72 and T2 < 80:
    G2 = "C"
    GP2 = 8.25
elif T2 >= 64 and T2 < 72:
    G2 = "D"
    GP2 = 7.5
elif T2 >= 56 and T2 < 64:
    G2 = "E"
    GP2 = 6.75
elif T2 >= 48 and T2 < 56:
    G2 = "G"
    GP2 = 6
elif T2 >= 40 and T2 < 48:
    G2 = "H"
    GP2 = 5
else:
    G2 = "F"
    GP2 = 0

# 03. Digital Circuits
if T3 >= 90:
    G3 = "A"
    GP3 = 10
elif T3 >= 80 and T3 < 90:
    G3 = "B"
    GP3 = 9
elif T3 >= 72 and T3 < 80:
    G3 = "C"
    GP3 = 8.25
elif T3 >= 64 and T3 < 72:
    G3 = "D"
    GP3 = 7.5
elif T3 >= 56 and T3 < 64:
    G3 = "E"
    GP3 = 6.75
elif T3 >= 48 and T3 < 56:
    G3 = "G"
    GP3 = 6
elif T3 >= 40 and T3 < 48:
    G3 = "H"
    GP3 = 5
else:
    G3 = "F"
    GP3 = 0

# 04. Lab : Digital Circuits
if T4 >= 90:
    G4 = "A"
    GP4 = 10
elif T4 >= 80 and T4 < 90:
    G4 = "B"
    GP4 = 9
elif T4 >= 72 and T4 < 80:
    G4 = "C"
    GP4 = 8.25
elif T4 >= 64 and T4 < 72:
    G4 = "D"
    GP4 = 7.5
elif T4 >= 56 and T4 < 64:
    G4 = "E"
    GP4 = 6.75
elif T4 >= 48 and T4 < 56:
    G4 = "G"
    GP4 = 6
elif T4 >= 40 and T4 < 48:
    G4 = "H"
    GP4 = 5
else:
    G4 = "F"
    GP4 = 0

# 05. Electronics Measurements & Instrumentation
if T5 >= 90:
    G5 = "A"
    GP5 = 10
elif T5 >= 80 and T5 < 90:
    G5 = "B"
    GP5 = 9
elif T5 >= 72 and T5 < 80:
    G5 = "C"
    GP5 = 8.25
elif T5 >= 64 and T5 < 72:
    G5 = "D"
    GP5 = 7.5
elif T5 >= 56 and T5 < 64:
    G5 = "E"
    GP5 = 6.75
elif T5 >= 48 and T5 < 56:
    G5 = "G"
    GP5 = 6
elif T5 >= 40 and T5 < 48:
    G5 = "H"
    GP5 = 5
else:
    G5 = "F"
    GP5 = 0

# 06. Lab : Electronics Measurements & Instrumentation
if T6 >= 90:
    G6 = "A"
    GP6 = 10
elif T6 >= 80 and T6 < 90:
    G6 = "B"
    GP6 = 9
elif T6 >= 72 and T6 < 80:
    G6 = "C"
    GP6 = 8.25
elif T6 >= 64 and T6 < 72:
    G6 = "D"
    GP6 = 7.5
elif T6 >= 56 and T6 < 64:
    G6 = "E"
    GP6 = 6.75
elif T6 >= 48 and T6 < 56:
    G6 = "G"
    GP6 = 6
elif T6 >= 40 and T6 < 48:
    G6 = "H"
    GP6 = 5
else:
    G6 = "F"
    GP6 = 0

# 07. Network Analysis
if T7 >= 90:
    G7 = "A"
    GP7 = 10
elif T7 >= 80 and T7 < 90:
    G7 = "B"
    GP7 = 9
elif T7 >= 72 and T7 < 80:
    G7 = "C"
    GP7 = 8.25
elif T7 >= 64 and T7 < 72:
    G7 = "D"
    GP7 = 7.5
elif T7 >= 56 and T7 < 64:
    G7 = "E"
    GP7 = 6.75
elif T7 >= 48 and T7 < 56:
    G7 = "G"
    GP7 = 6
elif T7 >= 40 and T7 < 48:
    G7 = "H"
    GP7 = 5
else:
    G7 = "F"
    GP7 = 0

# 08. Lab : Network Analysis
if T8 >= 90:
    G8 = "A"
    GP8 = 10
elif T8 >= 80 and T8 < 90:
    G8 = "B"
    GP8 = 9
elif T8 >= 72 and T8 < 80:
    G8 = "C"
    GP8 = 8.25
elif T8 >= 64 and T8 < 72:
    G8 = "D"
    GP8 = 7.5
elif T8 >= 56 and T8 < 64:
    G8 = "E"
    GP8 = 6.75
elif T8 >= 48 and T8 < 56:
    G8 = "G"
    GP8 = 6
elif T8 >= 40 and T8 < 48:
    G8 = "H"
    GP8 = 5
else:
    G8 = "F"
    GP8 = 0   

# 09. Engineering Mathematics III
if T9 >= 90:
    G9 = "A"
    GP9 = 10
elif T9 >= 80 and T9 < 90:
    G9 = "B"
    GP9 = 9
elif T9 >= 72 and T9 < 80:
    G9 = "C"
    GP9 = 8.25
elif T9 >= 64 and T9 < 72:
    G9 = "D"
    GP9 = 7.5
elif T9 >= 56 and T9 < 64:
    G9 = "E"
    GP9= 6.75
elif T9 >= 48 and T9 < 56:
    G9 = "G"
    GP9 = 6
elif T9 >= 40 and T9 < 48:
    G9 = "H"
    GP9 = 5
else:
    G9 = "F"
    GP9 = 0

# ========================================================================================================

# Course Credits Per Subjects
# if Total Marks less than 40 -> Grade = F -> Course Credits = 0
# if Total Marks more than 40 -> Grade = A, B, C, D, E, G, H -> Course Credits as per Subject or Course

# 01. Electronics Device
if G1 == "F":
    C1 = 0
else:                
    C1 = 4           

# 02. Lab : Electronics Device
if G2 == "F":
    C2 = 0
else:
    C2 = 1

# 03. Digital Circuits
if G3 == "F":
    C3 = 0
else:
    C3 = 4

# 04. Lab : Digital Circuits
if G4 == "F":
    C4 = 0
else:
    C4 = 1

# 05. Electronics Measurements & Instrumentation
if G5 == "F":
    C5 = 0
else:
    C5 = 3

# 06. Lab : Electronics Measurements & instrumentation
if G6 == "F":
    C6 = 0
else:
    C6 = 1

# 07. Network Analysis
if G7 == "F":
    C7 = 0
else:
    C7 = 4

# 08. Lab : Network Analysis
if G8 == "F":
    C8 = 0
else:
    C8 = 1

# 09. Engineering Mathematics III
if G9 == "F":
    C9 = 0
else:
    C9 = 4

# ============================================================================================================

# Calculations :

TC = C1 + C2 + C3 + C4 + C5 + C6 + C7 + C8 + C9        # Total Credits ( TC )


# Total Grade Points ( TGP = GP = equal )
GP = GP1 * C1 + GP2 * C2 + GP3 * C3 + GP4 * C4 + GP5 * C5 + GP6 * C6 + GP7 * C7 + GP8 * C8 + GP9 * C9   # GP = ( GPi * Ci ) -> i = 1-9
TGP = "{:.2f}".format(GP)           # Two Decimal Points Format ( string )


# Semester Grade Point Average ( SGPA1 = SGPA = equal ) 
SGPA1 =  GP / TC                       
SGPA = "{:.2f}".format(SGPA1)       # Two Decimal Points Format ( string )


# Percentage ( P1 = P = equal )
P1 = ( SGPA1 - 0.75 ) * 10
P = "{:.2f}".format(P1)             # Two Decimal Points Format ( string )


# Result
# if Grade = F -> Fail otherwise Pass
G = [G1,G2,G3,G4,G5,G6,G7,G8,G9]

for i in range(len(G)):
    if G[i] == "F":
        R = "Fail"
    else:
        R = "Pass"


# ==========================================================================================================================

# ============================================= MARKSHIT GENERATION ========================================================

print('''    





                                                                                                                        ''')


print("                                            Nagar Yuwak Shikshan Sanstha's                                           ") 
print("                                       YESHWANTRAO CHAVAN COLLEGE OF ENGINEERING                                     ")
print("                             Hingna Road, Wanadongri, Nagpur - 441 110 (INDIA), www.ycce.edu                         ")
print("                                    ( An Autonomous Institution under UGC Act 1956 )                                 ") 
print("---------------------------------------------------------------------------------------------------------------------")
print("                          Affiliated to Rashtrasant Tukadoji Maharaj Nagpur University, Nagpur                       ")  
print("---------------------------------------------------------------------------------------------------------------------")
print("                                                SEMESTER GRADE REPORT                                                ")
print("                                              Academic Year :",AY,"                                                  ")
print("                                                                                                                     ")
print("  Programme    :",Pro,"                                                                                                ")
print("  Semester     :",SEM,"                                                                                              ")
print("  Unique Identification Code :",UIC,"                                                                                ")
print("  Student Name :",SN,"                                                                                               ")
print("  Mother Name  :",MN,"                                                               Exam Roll No.  :",RN,"          ")
print("  Date of Birth:",DOB,"                                                          Gender         :",Gender,"          ")
print("                                                                                                                     ")
print("=====================================================================================================================")
print("| Current Semester Courses :                                                                                        |")
print("|===================================================================================================================|")
print("|    |                                                     |              MARKS                 |          |        |")
print("| Sr.|                     Course Name                     | Internal  |  Theory   |   Total    |   Grade  | Course |")
print("| No.|                                                     | Out of 40 | Out of 60 | Out of 100 | Obtained | Credit |")
print("|===================================================================================================================|")
print("| 1. | Electronics Device                                  |    ",S1,"   |    ",s1,"   |    ",T1,"    |    ",G1,"   |  ",C1,"   |")
print("|-------------------------------------------------------------------------------------------------------------------|")
print("| 2. | Lab : Electronics Device                            |    ",S2,"   |    ",s2,"   |    ",T2,"    |    ",G2,"   |  ",C2,"   |")
print("|-------------------------------------------------------------------------------------------------------------------|")
print("| 3. | Digital Circuits                                    |    ",S3,"   |    ",s3,"   |    ",T3,"    |    ",G3,"   |  ",C3,"   |")
print("|-------------------------------------------------------------------------------------------------------------------|")
print("| 4. | Lab : Digital Circuits                              |    ",S4,"   |    ",s4,"   |    ",T4,"    |    ",G4,"   |  ",C4,"   |")
print("|-------------------------------------------------------------------------------------------------------------------|")
print("| 5. | Electronics Measurements & Instrumentation          |    ",S5,"   |    ",s5,"   |    ",T5,"    |    ",G5,"   |  ",C5,"   |")
print("|-------------------------------------------------------------------------------------------------------------------|")
print("| 6. | Lab :  Electronics Measurements & Instrumentation   |    ",S6,"   |    ",s6,"   |    ",T6,"    |    ",G6,"   |  ",C6,"   |")
print("|-------------------------------------------------------------------------------------------------------------------|")
print("| 7. | Network Analysis                                    |    ",S7,"   |    ",s7,"   |    ",T7,"    |    ",G7,"   |  ",C7,"   |")
print("|-------------------------------------------------------------------------------------------------------------------|")
print("| 8. | Lab : Network Analysis                              |    ",S8,"   |    ",s8,"   |    ",T8,"    |    ",G8,"   |  ",C8,"   |")
print("|-------------------------------------------------------------------------------------------------------------------|")
print("| 9. | Engineering Mathematics III                         |    ",S9,"   |    ",s9,"   |    ",T9,"    |    ",G9,"   |  ",C9,"   |")
print("=====================================================================================================================")
print("                                                                                                                     ")
print(" Grade Ponits for Grade : A = 10, B = 09, C = 8.25, D = 7.5, E = 6.75, G = 6, H = 5, F = 0                           ")
print("                                                                                                                     ")
print("                          ===============================================================                            ")
print("                          |                Current Semester Record                      |                            ")
print("                          |-------------------------------------------------------------|                            ")
print("                          | Earned  |    Earned    |  SGPA  |  Percentage  |   Result   |                            ")
print("                          | Credits | Grade Points |        |              |            |                            ")
print("                          |=============================================================|                            ")
print("                          |   ",TC ,"  |   ",TGP,"   | ",SGPA," |    ",P,"   |   ",R,"   |                           ")
print("                          ===============================================================                            ")
print("                                                                                                                     ")
print(" percentage = ( SGPA - 0.75 ) * 10                                                                                   ")
print("---------------------------------------------------------------------------------------------------------------------")
