The AI Job Search Agent is an automated tool that helps job seekers find and apply for the most relevant positions based on their LinkedIn profile. Using advanced AI models and web scraping techniques, this agent analyzes your professional background, identifies suitable job titles, searches for matching opportunities, selects the most appropriate positions, and even generates personalized cover letters.

## Features

- **LinkedIn Profile Analysis**: Extracts and analyzes your LinkedIn profile to understand your skills, experience, and qualifications
- **Job Title Recommendation**: Suggests the most relevant job titles based on your professional background
- **Automated Job Search**: Searches LinkedIn for job opportunities matching the recommended titles
- **Intelligent Job Selection**: Selects the 5 most relevant and varied positions from the search results
- **Personalized Cover Letters**: Generates tailored cover letters for each selected job
- **Comprehensive Report**: Creates a detailed markdown report with all findings and recommendations

## Technology Stack

- **Python**: Core programming language
- **Apify**: Web scraping and data extraction
- **Pydantic AI**: Structured data validation and AI integration
- **Google Gemini AI**: Advanced language model for analysis and content generation

## Architecture

The AI Job Search Agent follows a sequential workflow:

1. **Profile Extraction**: The agent uses Crawlee and Apify's LinkedIn Profile Scraper to extract your professional data from LinkedIn.
2. **Profile Analysis**: The extracted profile data is processed and analyzed to identify key skills, experiences, and qualifications.
3. **Job Title Generation**: Based on the profile analysis, the system recommends the most suitable job titles.
4. **Job Search**: Using Crawlee and Apify's LinkedIn Job Scraper, the agent searches for positions matching the recommended titles.
5. **Job Filtering & Ranking**: The system evaluates each job opportunity against your profile, filtering and ranking them by relevance.
6. **Job Selection**: The top 5 most relevant and diverse positions are selected from the ranked results.
7. **Cover Letter Generation**: For each selected job, a personalized cover letter is generated based on your profile and the job requirements.
8. **Report Generation**: Finally, all findings and recommendations are compiled into a comprehensive markdown report.

This pipeline ensures a thorough, data-driven approach to job searching that leverages both web scraping capabilities and AI-powered analysis.

## Input Parameters

The agent requires the following input:

```json
{
  "linkedin_profile_url": "https://www.linkedin.com/in/yourprofile/"
}
```

### Output

The agent generates several outputs:

1. **LinkedIn Profile Information**: Extracted data from your LinkedIn profile
2. **Recommended Job Titles**: List of suitable job titles based on your profile
3. **Selected Jobs**: Details of the 5 most relevant jobs found
4. **Cover Letters**: Personalized cover letters for each selected job
5. **Markdown Report**: A comprehensive report summarizing all findings and recommendations

## Project Structure

```
ai-job-search-agent/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── main.py         # Main application logic
│   ├── models.py       # Pydantic data models
│   ├── prompts.py      # AI system prompts
│   └── tools.py        # LinkedIn scraping functions
```

## Key Components

### LinkedIn Profile Analyzer

The profile analyzer extracts information from a LinkedIn profile using Apify's LinkedIn Profile Scraper. It then processes this data to identify the user's skills, experience, education, and other relevant information.

### Job Title Recommender

Using the Google Gemini AI model, the system analyzes the LinkedIn profile information to recommend the 5 most suitable job titles for the user.

### LinkedIn Job Search

For each recommended job title, the system searches LinkedIn using Apify's LinkedIn Job Scraper to find relevant job opportunities.

### Job Selection and Cover Letter Generation

The AI evaluates all job opportunities and selects the 5 most relevant positions. For each selected job, it generates a personalized cover letter that highlights the user's most relevant qualifications.

### Report Generation

Finally, the system creates a comprehensive markdown report that includes the profile analysis, recommended job titles, selected jobs, personalized cover letters, and an executive summary.

## Example Output

The markdown report includes:

- Profile overview with name, headline, and location
- List of recommended job titles
- Details of each selected job including:
  - Job title and company
  - Location and job URL
  - Reason why the job was selected
  - Personalized cover letter
- Executive summary with job search strategy insights


JSON output:
```json
{
  "linkedin_profile_info": {
    "firstName": "Louis",
    "lastName": "Deconinck",
    "headline": "Freelance Data Consultant & Apify Data Scraper",
    "addressCountryOnly": "Belgium",
    "addressWithoutCountry": "Kortrijk, Flemish Region",
    "about": "Looking for freelance / contract (ZZP) business intelligence or data analysis work. \n\nData Engineer & Data Analyst: Power BI, SQL, Python, Azure Cloud, Excel, VBA, Fabric, Power Query, SAS, Git, Data Modelling, Data Governance & Business Intelligence",
    "experiences": [
      {
        "title": "Business Intelligence Expert",
        "subtitle": "ABN AMRO Bank N.V. · Freelance",
        "caption": "Nov 2023 - Present · 1 yr 5 mos",
        "description": "ABN Amro is the third largest bank in The Netherlands. I trained 14 in-house data stewards on Microsoft Power BI (DAX), Power Query (M-code), and data modeling. I played an important role in the setup of a Belgian branch data warehouse in Azure Databricks (Apache Spark) by performing data quality monitoring on Azure Data Factory migration pipelines from operational systems toward a data lake."
      },
      {
        "title": "Web Scraping Developer",
        "subtitle": "Apify · Self-employed",
        "caption": "Oct 2024 - Present · 6 mos",
        "description": "Developed over 50 custom built B2B lead generation web scrapers in Typescript & Python using Crawlee & Apify with over 400 monthly active users. Scraped over 10,000,000 pages avoiding advanced anti-scraping measures."
      }
    ],
    "educations": [
      {
        "title": "University of Oxford",
        "subtitle": "Undergraduate Advanced Diploma, IT Systems Analysis & Design",
        "caption": "2020 - 2021",
        "description": "I followed courses on software development, project management, data management and business & functional analysis together with international IT experts. I achieved the highest possible grade of Distinction. The University of Oxford is the highest-ranked university in the world according to Times Higher Education."
      },
      {
        "title": "Ghent University",
        "subtitle": "Master of Science - MS, Business Administration: Finance & Risk",
        "caption": "2015 - 2019",
        "description": "My master dissertation's topic was: \"Acquisition by private equity vs industrial holding: impact on performance\" under the supervision of Rudy Aernoudt, Chief Economist of the European Commission. My team won the Business Strategy Game by McGraw-Hill during our course Strategic Management. Ghent University is the highest ranked Belgian university according to the Shanghai ranking."
      }
    ],
    "licenseAndCertificates": [
      {
        "title": "Fabric Analytics Engineer (DP-600)",
        "subtitle": "Microsoft",
        "caption": "Issued Jun 2024"
      },
      {
        "title": "CS50: Programming, Python, SQL & Web Development",
        "subtitle": "Harvard University",
        "caption": "Issued Mar 2024"
      }
    ],
    "honorsAndAwards": [
      {
        "title": "Winner AFC Data Challenge",
        "subtitle": "Issued by Academics for Companies · Mar 2022",
        "description": "Out of 11 teams, our team won first place in the AFC Data Challenge. We formulated data-driven business solutions for an online retail player using Power BI & Python."
      },
      {
        "title": "Winner Business Strategy Game",
        "subtitle": "Issued by McGraw-Hill · Feb 2019",
        "description": "BSG is a business simulation. Our team was able to secure the first position in our industry."
      }
    ],
    "languages": [
      {
        "title": "Dutch",
        "caption": "Native or bilingual proficiency"
      },
      {
        "title": "English",
        "caption": "Native or bilingual proficiency"
      }
    ],
    "volunteerAndAwards": [
      {
        "title": "Math & Statistics Tutor",
        "subtitle": "Superprof",
        "caption": "Jan 2020 - Present · 5 yrs 3 mos"
      },
      {
        "title": "Reasearch Analyst",
        "subtitle": "Curvo",
        "caption": "Jun 2023 - Dec 2023 · 7 mos"
      }
    ],
    "projects": [
      {
        "title": "Credit Risk Modelling: Probability of Default",
        "subtitle": "Aug 2023 - Aug 2023",
        "description": "Developed two statistical credit risk models for probability of default (PD) in Python with Scikit-learn and XGBoost: logistic regression versus gradient boosted trees. I performed data cleaning, compared and improved model performance and calculated expected loss (EL) using exposure at default (EAD) and loss given default (LGD)."
      },
      {
        "title": "Boat Sales Data Analysis",
        "subtitle": "Sep 2022 - Sep 2022",
        "description": "Analyzing listings for a boat sales newsletter. Performed data exploration, cleaning and analysis in Python using libraries: Pandas, Numpy, Matplotlib and Seaborn. Formulated business recommendations to increase newsletter readership."
      }
    ],
    "publications": [
      {
        "title": "Diagnosis and monitoring denosumab therapy of giant cell tumors of bone: radiologic-pathologic correlation",
        "subtitle": "Skeletal Radiology · Jul 29, 2023",
        "description": "Helped perform data analysis for this medical paper on the correlation between radiology and pathology for bone tumors."
      },
      {
        "title": "Acquisition by Private Equity Player versus Holding: Impact on Performance",
        "subtitle": "Ghent University · Jun 6, 2019",
        "description": "Master's dissertation on acquisitions by private equity players and holdings under the supervision of professor Rudy Aernoudt, Chief Economist of the European Commission."
      }
    ],
    "skills": [
      "Apify",
      "Web Crawling",
      "TypeScript",
      "Excel",
      "Power BI",
      "MySQL",
      "Transact-SQL (T-SQL)",
      "Python",
      "Data Analysis"
    ],
    "linkedinUrl": "https://www.linkedin.com/in/louisdeconinck/"
  },
  "selected_job_titles": [
    "Data Consultant",
    "Business Intelligence Consultant",
    "Data Analyst",
    "Data Engineer",
    "Web Scraping Developer"
  ],
  "selected_jobs": [
    {
      "job_id": "4181413685",
      "job_title": "Corporate Finance Consultant – Financiële en Fiscale Due Diligence",
      "job_description": "...",
      "company_name": "Titeca Pro Accountants & Experts",
      "company_url": "https://be.linkedin.com/company/titeca-pro",
      "location": "Roeselare, Flemish Region, Belgium",
      "time_posted": "1 week ago",
      "num_applicants": "Be among the first 25 applicants",
      "salary_range": null,
      "job_url": "https://be.linkedin.com/jobs/view/corporate-finance-consultant-%E2%80%93-financi%C3%ABle-en-fiscale-due-diligence-at-titeca-pro-accountants-experts-4181413685",
      "apply_url": "https://www.titeca.be/nl/vacature/corporate-finance-consultant-financiele-en-fiscale-due-diligence/",
      "seniority_level": "Mid-Senior level",
      "employment_type": "Full-time",
      "job_function": "Finance and Sales",
      "industries": "Accounting",
      "reason": "This role aligns perfectly with Louis's finance and risk background, M&A experience, and data analysis skills. His experience with financial data analysis, risk assessment, and due diligence makes him a strong candidate.",
      "cover_letter": "Dear Hiring Manager,\n\nI am writing to express my interest in the Corporate Finance Consultant position at Titeca Pro Accountants & Experts, as advertised on LinkedIn. With my Master's degree in Business Administration: Finance & Risk from Ghent University and my advanced diploma in IT Systems Analysis & Design from the University of Oxford, combined with my experience in business intelligence and data analysis, I am confident I possess the skills and expertise to excel in this role.\n\nIn my previous role as a Business Intelligence Expert at ABN AMRO Bank N.V., I trained data stewards on Microsoft Power BI and data modeling, and contributed to the setup of a data warehouse in Azure Databricks. As a Senior Credit Risk Analyst at Argenta, I analyzed financial bank data using SAS, SQL, Excel, and Power Query, and guided a data migration as a Data Steward. These experiences have equipped me with a strong understanding of financial, accounting, and fiscal data analysis, as well as corporate finance principles.\n\nI am particularly drawn to Titeca Pro's commitment to providing clear and substantiated insights to clients, and I am eager to contribute my analytical skills to help clients make informed strategic decisions. I am proficient in MS Office and data analysis tools, and I am confident in my ability to identify critical risks and opportunities within M&A transactions.\n\nThank you for considering my application. I am excited about the opportunity to contribute to Titeca Pro Accountants & Experts and look forward to discussing my qualifications further.\n\nSincerely,\nLouis Deconinck"
    }
  ],
  "summary": "The job selection strategy focuses on roles that leverage Louis's existing skills in data analysis, business intelligence, and financial modeling, while also providing opportunities for growth and variety. The selected positions span different industries (finance, retail, manufacturing, staffing) and seniority levels (entry-level to mid-senior), ensuring a diverse set of opportunities. Key themes include data analysis, Power BI, SQL, and Azure Cloud, aligning with Louis's core competencies. Prioritization should be given to the mid-senior level roles at Hays and Valiuz, as they offer the best combination of experience utilization and career advancement potential. The Young Graduate Analytics Consultant position at Unilin is also a strong contender due to Unilin's focus on innovation and sustainability, which may appeal to Louis's values. The DataKhi role provides an opportunity to apply his skills in a startup environment, which could be a good fit if Louis is looking for a more entrepreneurial experience. Finally, the Corporate Finance Consultant role at Titeca Pro directly utilizes his finance background and offers a unique opportunity to apply his data skills in the M&A space.",
  "markdown_report": "..."
}
```

Markdown output: 
```markdown
# Job Search Report for Louis Deconinck
Generated on 2025-03-17 21:31:17

## Profile Overview
- **Current Headline**: Freelance Data Consultant & Apify Data Scraper
- **Location**: Kortrijk, Flemish Region, Belgium
- **LinkedIn URL**: https://www.linkedin.com/in/louisdeconinck/

## Suggested Job Titles
Based on your profile analysis, here are the most relevant job titles for your background:

- Data Consultant
- Business Intelligence Consultant
- Data Analyst
- Data Engineer
- Web Scraping Developer

## Selected Job Opportunities

### Corporate Finance Consultant – Financiële en Fiscale Due Diligence at Titeca Pro Accountants & Experts
**Location**: Roeselare, Flemish Region, Belgium
**Job ID**: [4181413685](https://be.linkedin.com/jobs/view/corporate-finance-consultant-%E2%80%93-financi%C3%ABle-en-fiscale-due-diligence-at-titeca-pro-accountants-experts-4181413685)

#### Why This Role?
This role aligns perfectly with Louis's finance and risk background, M&A experience, and data analysis skills. His experience with financial data analysis, risk assessment, and due diligence makes him a strong candidate.

#### Cover Letter
Dear Hiring Manager,

I am writing to express my interest in the Corporate Finance Consultant position at Titeca Pro Accountants & Experts, as advertised on LinkedIn. With my Master's degree in Business Administration: Finance & Risk from Ghent University and my advanced diploma in IT Systems Analysis & Design from the University of Oxford, combined with my experience in business intelligence and data analysis, I am confident I possess the skills and expertise to excel in this role.

In my previous role as a Business Intelligence Expert at ABN AMRO Bank N.V., I trained data stewards on Microsoft Power BI and data modeling, and contributed to the setup of a data warehouse in Azure Databricks. As a Senior Credit Risk Analyst at Argenta, I analyzed financial bank data using SAS, SQL, Excel, and Power Query, and guided a data migration as a Data Steward. These experiences have equipped me with a strong understanding of financial, accounting, and fiscal data analysis, as well as corporate finance principles.

I am particularly drawn to Titeca Pro's commitment to providing clear and substantiated insights to clients, and I am eager to contribute my analytical skills to help clients make informed strategic decisions. I am proficient in MS Office and data analysis tools, and I am confident in my ability to identify critical risks and opportunities within M&A transactions.

Thank you for considering my application. I am excited about the opportunity to contribute to Titeca Pro Accountants & Experts and look forward to discussing my qualifications further.

Sincerely,
Louis Deconinck

---
### DATA ANALYST at DataKhi
**Location**: Tourcoing, Hauts-de-France, France
**Job ID**: [3462720209](https://fr.linkedin.com/jobs/view/data-analyst-at-datakhi-3462720209)

#### Why This Role?
This role is a good fit because it requires Power BI and SQL skills, which Louis possesses. The job also mentions Azure Cloud, which aligns with his experience. It provides an opportunity to apply his skills in a startup environment.

#### Cover Letter
Dear Hiring Manager,

I am writing to express my interest in the Data Analyst position at DataKhi, as advertised on LinkedIn. With my experience in data analysis, Power BI, SQL, and Azure Cloud, I am confident I possess the skills and expertise to excel in this role and contribute to your dynamic startup.

In my previous roles, I have developed a strong foundation in data analysis and business intelligence. As a Business Intelligence Expert at ABN AMRO Bank N.V., I trained data stewards on Microsoft Power BI and data modeling. As a Senior Credit Risk Analyst at Argenta, I analyzed financial bank data using SAS, SQL, Excel, and Power Query. These experiences have equipped me with the skills to analyze business problems, manipulate data, create dashboards, and ensure data flow accuracy.

I am particularly drawn to DataKhi's focus on data expertise and sustainable development, and I am eager to contribute my analytical skills to help your company make data-driven decisions. I am proficient in Power BI, SQL, and Azure Cloud, and I am confident in my ability to create new data flows and participate in the development of your startup.

Thank you for considering my application. I am excited about the opportunity to contribute to DataKhi and look forward to discussing my qualifications further.

Sincerely,
Louis Deconinck

---
### Young Graduate Analytics Consultant at Unilin
**Location**: Waregem, Flemish Region, Belgium
**Job ID**: [4158765196](https://be.linkedin.com/jobs/view/young-graduate-analytics-consultant-at-unilin-4158765196)

#### Why This Role?
This role is suitable for a recent graduate and aligns with Louis's data analysis skills, Power BI proficiency, and interest in building data platforms. The focus on Azure and PowerBI matches his experience.

#### Cover Letter
Dear Hiring Manager,

I am writing to express my interest in the Young Graduate Analytics Consultant position at Unilin, as advertised on LinkedIn. With my Master's degree in Business Administration: Finance & Risk from Ghent University and my advanced diploma in IT Systems Analysis & Design from the University of Oxford, combined with my strong affinity for data analysis and reporting tools, I am confident I possess the skills and expertise to excel in this role.

In my previous role as a Business Intelligence Expert at ABN AMRO Bank N.V., I trained data stewards on Microsoft Power BI and data modeling, and contributed to the setup of a data warehouse in Azure Databricks. As a Senior Credit Risk Analyst at Argenta, I analyzed financial bank data using SAS, SQL, Excel, and Power Query. These experiences have equipped me with a strong understanding of data analysis, reporting, and the translation of data into actionable insights.

I am particularly drawn to Unilin's enthusiasm for new talent and the opportunity to contribute to the development of the Azure and PowerBI dataplatform. I am eager to analyze reporting needs, set up solutions, and share new trends with the Unilin Data & Analytics community. I am also excited about the potential to work with new technologies such as machine learning and AI.

Thank you for considering my application. I am excited about the opportunity to contribute to Unilin and look forward to discussing my qualifications further.

Sincerely,
Louis Deconinck

---
### Data Analyst Retail Media at Valiuz
**Location**: Lille, Hauts-de-France, France
**Job ID**: [4164107331](https://fr.linkedin.com/jobs/view/data-analyst-retail-media-at-valiuz-4164107331)

#### Why This Role?
This role requires experience with SQL, Python, and data visualization, all of which Louis possesses. The focus on retail media provides a different industry context, adding variety to the job selection.

#### Cover Letter
Dear Hiring Manager,

I am writing to express my interest in the Data Analyst Retail Media position at Valiuz, as advertised on LinkedIn. With my experience in data analysis, SQL, Python, and data visualization tools like Tableau, I am confident I possess the skills and expertise to excel in this role and contribute to the performance of your retail media campaigns.

In my previous roles, I have developed a strong foundation in data analysis and business intelligence. As a Business Intelligence Expert at ABN AMRO Bank N.V., I trained data stewards on Microsoft Power BI and data modeling. As a Senior Credit Risk Analyst at Argenta, I analyzed financial bank data using SAS, SQL, Excel, and Power Query. These experiences have equipped me with the skills to measure campaign effectiveness, provide actionable insights, and work with data scientists and product teams.

I am particularly drawn to Valiuz's focus on stimulating collective intelligence and making data an asset for new commerce models. I am eager to analyze campaign performance, identify success factors, and test new approaches to improve ROAS. I am also excited about the opportunity to work with your modern data stack, including Google Big Query, Databricks, and Tableau.

Thank you for considering my application. I am excited about the opportunity to contribute to Valiuz and look forward to discussing my qualifications further.

Sincerely,
Louis Deconinck

---
### Data Analyst at Hays
**Location**: West Flanders, Flemish Region, Belgium
**Job ID**: [4170759037](https://be.linkedin.com/jobs/view/data-analyst-at-hays-4170759037)

#### Why This Role?
This role requires 4+ years of experience and proficiency in Azure, SQL, Power BI, and Python, all of which Louis has. It offers a mid-senior level position, providing an opportunity for career advancement.

#### Cover Letter
Dear Hiring Manager,

I am writing to express my interest in the Data Analyst position at Hays, as advertised on LinkedIn. With over four years of relevant experience and knowledge of Azure, SQL, Power BI, and Python, I am confident I possess the skills and expertise to excel in this role and contribute to your team's success.

In my previous roles, I have developed a strong foundation in data analysis and business intelligence. As a Business Intelligence Expert at ABN AMRO Bank N.V., I trained data stewards on Microsoft Power BI and data modeling. As a Senior Credit Risk Analyst at Argenta, I analyzed financial bank data using SAS, SQL, Excel, and Power Query. These experiences have equipped me with the skills to develop data solutions, analyze business systems, and maintain BI stacks.

I am particularly drawn to Hays's reputation as a market leader in the production of food supplements and vitamins, and I am eager to contribute my analytical skills to help your organization make data-driven decisions. I am proficient in Azure, SQL, Power BI, and Python, and I am confident in my ability to advise on improvements, support users, and ensure data integrity.

Thank you for considering my application. I am excited about the opportunity to contribute to Hays and look forward to discussing my qualifications further.

Sincerely,
Louis Deconinck

---

## Executive Summary
The job selection strategy focuses on roles that leverage Louis's existing skills in data analysis, business intelligence, and financial modeling, while also providing opportunities for growth and variety. The selected positions span different industries (finance, retail, manufacturing, staffing) and seniority levels (entry-level to mid-senior), ensuring a diverse set of opportunities. Key themes include data analysis, Power BI, SQL, and Azure Cloud, aligning with Louis's core competencies. Prioritization should be given to the mid-senior level roles at Hays and Valiuz, as they offer the best combination of experience utilization and career advancement potential. The Young Graduate Analytics Consultant position at Unilin is also a strong contender due to Unilin's focus on innovation and sustainability, which may appeal to Louis's values. The DataKhi role provides an opportunity to apply his skills in a startup environment, which could be a good fit if Louis is looking for a more entrepreneurial experience. Finally, the Corporate Finance Consultant role at Titeca Pro directly utilizes his finance background and offers a unique opportunity to apply his data skills in the M&A space.
```

## Configuration

The behavior of the AI models can be adjusted by modifying the system prompts in `src/prompts.py` and the model settings in `src/main.py`.

## Limitations

- The agent relies on the availability and accuracy of LinkedIn profile and job data
- The quality of recommendations depends on how complete and up-to-date your LinkedIn profile is

## License

This project is licensed under the MIT License.
