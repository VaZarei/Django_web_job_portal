# Add your LinkedIn email ID and password. WARNING: KEEP THIS OFFLINE ON YOUR PC AND DO NOT COMMIT/UPLOAD.
email: enery@gmail.com
password: V2243@$

# Anti-lock default is False to prevent your PC from sleeping to allow bot to run uninterrupted.
# Set it to True if you wish to disable this functionality.
disableAntiLock: False

# Set to True if you wish to search for remote jobs only.
remote: False

# Set to True if you wish to search for jobs marked as "under 10 applicants" (default is False).
lessthanTenApplicants: False

# Set to True or False to suit your preference. Multiple True allowed.
experienceLevel:
 internship: False
 entry: True
 associate: True
 mid-senior level: True   # Check this variable there is line instead Underline or ...
 director: True
 executive: False

# Set to True or False to suit your preference. Multiple True allowed.
jobTypes:
 full-time: true
 contract: false
 part-time: False
 temporary: false
 internship: False
 other: False
 volunteer: False

# Set ONLY one as True to suit your preference.
date:
 all time: True
 month: False
 week: False
 24 hours: False

# Remove hash sign to add positions. You can add as many as you need, but preserve formatting
positions:
 - Python developer
 - Django Developer
#  - Web Developer
#  - web Aplication Developer
 #- API development
 #- Full Stack Developer

 #- ...

# Remove hash sign to add locations. You can add as many as you need including adding 'Remote' as a location but first location must be a valid country.
locations:
 - England
 #- A third location
 #- ...
 #- Remote

# Set to True if you are residing in the country of job
residentStatus: True

# Distance from the location added above. Allowed values are {0, 5, 10, 25, 50, 100}, use only one.
distance: 100

# Optional directory to save logs, does not work sometimes. Does not work sometimes, so leave it unchanged.
outputFileDirectory: F:\Python\Selenium\LinkedinBot\EasyApplyBot\Log\

# Companies you don't want to apply.
companyBlacklist:
 #- company
 #- company2

# Job titles you want to avoid applying. Use it to refine performance of bot.
titleBlacklist:
 #- word1
 #- word2

# Bot will not apply to jobs posted by black listed people.
posterBlacklist:
 #- name1
 #- name2

# Path to your CV/resume and cover letter (remove hash sign). These paths often don't work
# so apply one job manually once, bot will reuse manually uploaded CV for automating the task.
# Note: Prefer a path without spaces, i.e. instead of "Me My" to "MeMy" or "Me_My".
uploads:
 resume: F:\Python\Selenium\LinkedinBot\EasyApplyBot\Resume_Vahid_Zarei_A2.pdf
 # Cover letter is optional
 coverLetter: F:\Python\Selenium\LinkedinBot\EasyApplyBot\CoverLetter_Vahid_Zarei.pdf


# ------------ QA section -------------------

# ------------ Additional parameters: checkboxes ---------------
checkboxes:
 # Do you have a valid driver's license? (yes/no checkbox)
 driversLicence: False
 # Will you now, or in the future, require sponsorship for employment visa status (e.g. H-1B visa status)? (yes/no checkbox)
 # This is relative to the location and your citizenship applying above, and same with legallyAuthorized.
 requireVisa: False
 # Are you legally authorized to work in COUNTRY? (yes/no checkbox)
 legallyAuthorized: True
 # Do you have necessary licenses or certifications required in your profession? E.g. CPA, CA, CFA, professional license
 certifiedProfessional: True
 # We must fill this position urgently. Can you start immediately? (yes/no checkbox)
 urgentFill: True
 # Are you comfortable commuting or work on-site to this job's location? (yes/no checkbox)
 commute: True
 # Are you comfortable working in a remote environment? (yes/no checkbox)
 remote: True
 # Are you comfortable taking a drug in accordance with local/state laws? (yes/no checkbox)
 drugTest: True
 # Are you willing to complete an assessment? (yes/no checkbox)
 assessment: True
 # Do you have security clearance of [xxx] country? (yes/no checkbox)
 securityClearance: False
 # Have you completed the following level of education: DEGREE TYPE? Remove applicable # signs (yes/no checkbox)
 degreeCompleted:
  #  - High School Diploma
  - Bachelor's Degree
  # - Associate's Degree
  - Master's Degree
  - Master of Software Engineering
  # - Doctor of Philosophy
  # - Doctor of Medicine
  # - Doctor of Law
 # Are you willing to undergo a background check, in accordance with local law/regulations?
 backgroundCheck: True

# ------------ Additional parameters: universityGpa ---------------
universityGpa: 4.0

# ------------ Additional parameters: salaryMinimum ---------------
salaryMinimum: 50000

# ------------ Additional parameters: languages ---------------
languages:
 english: Native or bilingual # Allowed choices { None, Conversational, Professional, Native or bilingual }
 # arabic: Conversational
 # french: Professional

# ------------ Additional parameters: noticePeriod in weeks ---------------
noticePeriod: 3

# ------------ Additional parameters: years of experience ---------------
# How many years of work experience do you have ...? (whole numbers only)
# You may add more skills depending on your industry or profession at the bottom.
experience:
 # normal ones
 Science: 3
 Finance: 2
 IT Expert: 14
 Information and technology: 14
 linux: 2
 Training & Development: 2
 C++: 1
 C: 1
 Python: 8
 Backend: 8
 Python Developer: 8
 Backend: 8
 Django: 5
 Django Framework: 5
 Web Development: 5
 Web Applications: 5
 Full Stack Developer: 5
 Fast API: 1
 SQL Server: 8
 SQL : 8
 mysql : 8
 Microsoft SQL Server: 8
 PostgreSQL: 3
 Git: 8
 selenium: 2
 Hardware: 9
 # default to put for any industry/skill that you did not list
 default: 0

# ------------ Additional parameters: personal info ---------------
personalInfo:
 Pronouns: Mr.
 First Name: Vahid
 Last Name: Zarei
 Phone Country Code: United Kingdom (+44) # See Linkedin for your country code, must be exact according to the international platform, i.e. Italy (+39) not Italia (+39)
 Mobile Phone Number: 07900771739
 Street address: High Street
 City: Hull # Include the state/province as well!
 State: Yorkshire
 Zip: HU1
 Linkedin: www.linkedin.com/in/vahid-zareii
 Website: www.linkedin.com/in/vahid-zareii # github/website is interchangeable here
 MessageToManager: "Hi, I am interested to join your organization. Please have a look at my resume. Thank you." # Keep message short and within the quotes. This is a testing feature and may not work.

# ------------ Additional parameters: USA employment crap ---------------
eeo:
 gender: male
 race: None
 veteran: None
 disability: None
 citizenship: yes
 clearance: no
